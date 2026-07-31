"""
data_loader.py
Handles mapping region codes to their CSV files and loading them into DataFrames.
"""

import pandas as pd

REGION_FILES = {
    "US": "data/USA.csv",
    "IN": "data/India.csv",
    "UK": "data/United_Kingdom.csv",
    "JP": "data/Japan.csv",
}


def load_region_csv(region_code):
    """
    Loads the CSV for a given region code into a DataFrame.
    Assumes region_code is already validated against REGION_FILES.
    """
    return pd.read_csv(REGION_FILES[region_code])
