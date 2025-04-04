import pandas as pd
import numpy as np

# overview of data
def view_data(data): 
    print(f"Data has {data.shape[0]} rows and {data.shape[1]} columns with these data types:")
    print()
    print(data.dtypes)
    print()
    print("Data row sample and full columns:")
    return data.sample(5)

# checks for dupplicates, NaN & empty spaces
# and returns the number of duplicates, NaN & empty spaces
def check_data(data):
    duplications = data.duplicated().sum()
    nan_values = data.isna().sum()
    empty_spaces = data.eq(' ').sum()
    print(f"There are {duplications} duplicate rows, {nan_values.values.sum()} empty rows and {empty_spaces.values.sum()} empty spaces")
    if duplications > 0:
        print("Duplicate Rows:")
        print(data[data.duplicated(keep=False)])
    if nan_values.values.sum() > 0:
        print("NaN Rows:")
        for x in nan_values[nan_values > 0].index:
            perc = str(round(data[x].isna().sum() / len(data) * 100, 2))
            print(f"{perc}% of NaNs in the {x} column")
    if empty_spaces.values.sum() > 0:
        print("Empty Rows:")

# given a dataframe a function to create a subset of columns
def create_subset(data, columns):
    subset = data[columns]
    return subset
