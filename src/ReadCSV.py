import pandas as pd
import os
from dataclasses import dataclass
import logging

@dataclass(frozen=True)
class State:
    df: pd.DataFrame = None
    clean_df: pd.DataFrame = None
    final_df: pd.DataFrame = None

@dataclass
class DataStats:
    """CLI: enter in filename from CLI. verify clean data in print output"""
    num_blanks_orig: int = 0
    num_na_orig: int = 0
    num_nulls_orig: int = 0
    num_rows_orig: int = 0
    num_rows_removed: int = 0
    df_memory_total_orig: int = 0
    df_memory_total_after_clean: int = 0
    df_memory_by_column_orig: pd.Series = None
    df_memory_by_column_after_clean: pd.Series = None
    
    def percent_memory_saved(self):
        return ((self.df_memory_by_columnm_orig - self.df_memory_total_after_clean)/self.df_memory_by_columnm_orig)*100.0

    
@dataclass
class ReadCSV:
    """input: filename, output: statistics of datacleaning and memory saved after type conversion"""
    """CLI: enter in filename from CLI. verify clean data in print output"""
    """read csv file and drop rows with NA and 1 space strings"""
    df: pd.DataFrame = None
    clean_df: pd.DataFrame = None
    final_df: pd.DataFrame = None
    clean_data_stats: CleanDataStats = None
    
    def __init__(self,file_name):
        self.file_name=file_name
        self.read_csv()
        self.num_na_null_blank(self.df)
        self.print_memory_usage(self.df)
        self.clean(self.df)
        self.convert_object_types(self.clean_df)
    
    def populate_stats(self,df):
        data_stats = DataStats()
        data_stats.num_rows_orig = df.shape[0]
        
        print(self.num_na_null_blank(df))
    
    def read_csv(self)->None:
        if (self.clean_df is None) and (self.final_df is None) and (self.df is None):
            try:
                df = pd.read_csv(self.file_name)
                print("number of na, nulls and blanks in df before cleaning")
                self.populate_stats(df)
            except OSError as e:
                print(f"Unable to open {file_name}: {e}", file=sys.stderr)
                return
            self.df = df
        else: 
            print("Invalid initial dataframe state read_csv")
            
    
    
    def print_memory_usage(self,df):
        print(f"memory usage by column:{df.memory_usage()}")
        print(f"total memory usage:{df.memory_usage().sum()}")
        
    def clean(self,df)->None:
        if (self.df is not None) and (self.clean_df is None) and (self.final_df is None):
            print("df shape before na drop:",df.shape)
            df.dropna(inplace=True)
            print("df shape after na drop:",df.shape)
            print("df shape before removing one space strings:",df.shape)
            print("shape of blanks",df[df.values == ' '].shape)
            df.drop(df[df.values == ' '].index,inplace=True)
            print("df shape after removing one space strings:",df.shape)
            self.clean_df = df
            self.df=None
        else:
            print("Invalid dataframe state clean")
    
    def num_na_null_blank(self,df)->Tuple(int,int,int):
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
        """convert object to native types"""
        if (self.df is None) and (self.clean_df is not None) and (self.final_df is None):
            df = df.convert_dtypes()
            df["CESD2000Total"]=df["CESD2000Total"].astype("category")
            df["CESDTotal2000cutpt"]=df["CESDTotal2000cutpt"].astype("category")
            df["RelAt2000cat2"]=df["RelAt2000cat2"].astype("category")
            df["Marital2000c5"]=df["Marital2000c5"].astype("category")
            df["WorkTimeHrsperWkPastCalYr2000cat4"]=df["WorkTimeHrsperWkPastCalYr2000cat4"].astype("category")
            self.print_memory_usage(df)
            print("verify columns are category and not object or string")
            print(df.dtypes)
            self.final_df = df
            self.clean_df = None
        else:
            print("invalid dataframe state convert_object_types")
    
    def run_regression(self):
        """which features and how to choose x and y run regression """
        """save result sets in class"""
        pass
        
#test file permission wrong, file not there, path not present, path wrong, file name worng, 
#isDirectoryError, fileNotFound error, permission error
rc = ReadCSV('./data/NLSY.csv')

#print(rc.df)
#dataclass for state, statistics
#private methods, do we still need state if no public members? 
