import pandas as pd
import statsmodels.api as sm
from dataclasses import dataclass, field


@dataclass(frozen=True)
class Regression:
    dataframe: pd.DataFrame = field(default_factory=pd.DataFrame)
