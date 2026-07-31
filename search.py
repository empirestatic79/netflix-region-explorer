"""
search.py
Fuzzy matching helpers: region selection (with typo tolerance) and
movie/show title search within a region, plus cross-region lookups.
"""

import pandas as pd
from rapidfuzz import process, fuzz
from src.data_loader import REGION_FILES, load_region_csv


def select_region():
    """
    Prompts the user for a region code. Handles case and minor typos
    via rapidfuzz. Returns (region_code, DataFrame) once a valid region
    is confirmed.
    """
    while True:
        user_input = input("Select region (US, IN, UK, JP): ").strip().upper()

        if user_input in REGION_FILES:
            region = user_input
        else:
            match = process.extractOne(user_input, REGION_FILES.keys(), scorer=fuzz.ratio)
            if match and match[1] >= 60:
                confirm = input(f"Did you mean {match[0]} (y/n)? ").strip().lower()
                region = match[0] if confirm == "y" else None
            else:
                region = None

        if region:
            print(f"Region set to {region}")
            df = load_region_csv(region)
            return region, df
        else:
            print("Region not recognized. Try again.\n")


def search_movie(df, threshold=75):
    """
    Presents a menu: search for a title, or view the full catalog.
    Returns (query, result_df) where result_df is None if no close match found.
    """
    while True:
        question = input("To search Movie/Show Enter 1, or to see the entire list Enter 2: ").strip()

        if question == "1":
            query = input("Enter Movie/Show title to search: ").strip()
            titles = df["show_title"].tolist()

            matches = process.extract(query, titles, scorer=fuzz.WRatio, limit=5)
            good_matches = [m for m in matches if m[1] >= threshold]

            if not good_matches:
                return query, None

            matched_titles = [m[0] for m in good_matches]
            result_df = df[df["show_title"].isin(matched_titles)]
            return query, result_df

        elif question == "2":
            pd.set_option('display.colheader_justify', 'center')
            print(df[["category", "show_title", "season_title"]].to_string(index=False))

        else:
            print("Enter a valid choice.")


def search_other_regions(query, exclude_region, threshold=90):
    """
    Checks every region EXCEPT exclude_region for a close match to query.
    Returns a dict of {region_code: matching_df} for regions where it was found.
    """
    found = {}

    for region_code, filepath in REGION_FILES.items():
        if region_code == exclude_region:
            continue

        df = load_region_csv(region_code)
        titles = df["show_title"].tolist()
        matches = process.extract(query, titles, scorer=fuzz.WRatio, limit=3)
        good_matches = [m for m in matches if m[1] >= threshold]

        if good_matches:
            matched_titles = [m[0] for m in good_matches]
            found[region_code] = df[df["show_title"].isin(matched_titles)]

    return found
