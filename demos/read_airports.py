import pandas as pd
from pathlib2 import Path
import os

data_dir = Path.cwd().parent.joinpath("data")
filename = "airports.csv"
airport_data = data_dir.joinpath(filename)

if __name__ == "__main__":
    df = pd.read_csv(airport_data, sep=",")
    print(df)
    print(df["name"])

