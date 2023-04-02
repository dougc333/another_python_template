import pandas as pd
from dataclasses import dataclass
import logging
from typing import Tuple
import sys

#@dataclass
#class OutOfOrderException(frozen=True):
#    message: str
    

@dataclass
class State:
    df: pd.DataFrame = None
    clean_df: pd.DataFrame = None
    final_df: pd.DataFrame = None

@dataclass
class DataStats:
    """CLI: enter in filename from CLI. verify clean data in print output"""
    num_blank: int = 0
    num_na: int = 0
    num_nulls: int = 0
    num_rows: int = 0
    memory_total: int = 0
    memory_by_column: pd.Series = None
    dtypes_by_column: pd.Series = None
    def percent_memory_saved(self):
        return ((self.df_memory_by_columnm_orig - self.df_memory_total_after_clean)/self.df_memory_by_columnm_orig)*100.0

    
@dataclass
class ReadCSV:
    """input: filename, output: statistics of datacleaning and memory saved after type conversion"""
    """CLI: enter in filename from CLI. verify clean data in print output"""
    """read csv file and drop rows with NA and 1 space strings"""
    #df: pd.DataFrame = None
    #clean_df: pd.DataFrame = None
    #final_df: pd.DataFrame = None
    state: State = State()
    before_clean_stats: DataStats = None
    after_clean_stats: DataStats = None
    
    def __init__(self,file_name):
        self.file_name=file_name
        self.read_csv()
        self.num_na_null_blank(self.state.df)
        self.print_memory_usage(self.state.df)
        self.clean(self.state.df)
        self.convert_object_types(self.clean_df)

    def populate_stats(self,df):
        data_stats = DataStats()
        data_stats.num_rows = df.shape[0]
        data_stats.num_nulls = df.isnull().sum().sum()
        data_stats.num_na = df.isnull().sum().sum()
        data_stats.num_blank = (df.values == " ").sum()
        data_stats.memory_total = df.memory_usage().sum()
        data_stats.memory_by_column = df.memory_usage()
        data_stats.dtypes_by_column = df.dtypes
    
    def read_csv(self)->None:
        if (self.state.clean_df is None) and (self.state.final_df is None) and (self.state.df is None):
            try:
                df = pd.read_csv(self.file_name)
                print("number of na, nulls and blanks in df before cleaning")
                self.before_clean_stats = self.populate_stats(df)
            except OSError as e:
                print(f"Unable to open {self.file_name}: {e}", file=sys.stderr)
                return
            self.state.df = df
        else: 
            print("Invalid initial dataframe state read_csv")
            
    
    
    def print_memory_usage(self,df):
        print(f"memory usage by column:{df.memory_usage()}")
        print(f"total memory usage:{df.memory_usage().sum()}")
        
    def clean(self,df)->None:
        """cleans nulls, 
           1 space strings, 
           empty spaces, 
           na
        """
        if (self.state.df is not None) and (self.state.clean_df is None) and (self.state.final_df is None):
            print("df shape before na drop:",df.shape)
            df.dropna(inplace=True)
            print("df shape after na drop:",df.shape)
            print("df shape before removing one space strings:",df.shape)
            print("shape of blanks",df[df.values == ' '].shape)
            df.drop(df[df.values == ' '].index,inplace=True)
            print("df shape after removing one space strings:",df.shape)
            self.after_clean_stats = self.populate_stats(df)
            self.state.clean_df = df
            self.state.df = None
        else:
            print("Invalid dataframe state clean")
    
    def num_na_null_blank(self,df)->Tuple[int,int,int]:
        """Input dataframe
           Output tuple, 
           1) number of NA in dataframe
           2) number of null in dataframe
           3) number of one space strings, deliberately ignore 2 space or more strings
        """
        print("number of na:",df.isna().sum().sum())
        print("number of null:", df.isnull().sum().sum() )
        print("number of one space empty strings:",(df.values==' ').sum())
        #prints column sum of nulls. We want entire dataframe vs by column summary?
        return ( df.isna().sum().sum(), df.isnull().sum().sum(), (df.values==' ').sum())
    
    def convert_object_types(self,df)->None:
        """convert object to native types this isn't automated
           leave hard coded for this version
           this needs input from the web UI to figure which columns to covert and the types
        """
        if (self.state.df is None) and (self.state.clean_df is not None) and (self.state.final_df is None):
            df = df.convert_dtypes()
            df["CESD2000Total"]=df["CESD2000Total"].astype("category")
            df["CESDTotal2000cutpt"]=df["CESDTotal2000cutpt"].astype("category")
            df["RelAt2000cat2"]=df["RelAt2000cat2"].astype("category")
            df["Marital2000c5"]=df["Marital2000c5"].astype("category")
            df["WorkTimeHrsperWkPastCalYr2000cat4"]=df["WorkTimeHrsperWkPastCalYr2000cat4"].astype("category")
            self.print_memory_usage(df)
            print("verify columns are category and not object or string")
            print(df.dtypes)
            self.after_clean_stats = self.populate_stats(df)
            self.state.final_df = df
            self.state.clean_df = None
        else:
            print("invalid dataframe state convert_object_types")
    
    def run_regression(self, formula):
        """which features and how to choose x and y run regression """
        """save result sets in class"""
        if self.state.df is None and self.state.clean_df is None and self.state.final_df is not None:
            print("running regression" )
            
            
        
#test file permission wrong, file not there, path not present, path wrong, file name worng, 
#isDirectoryError, fileNotFound error, permission error
rc = ReadCSV('./data/NLSY.csv')

#print(rc.df)
#dataclass for state, statistics
#private methods, do we still need state if no public members? 
