"""
cli.py
The interactive command-line interface. Ties region selection, search,
and cross-region fallback together into a usable program.
"""

from src.search import select_region, search_movie, search_other_regions


def main():
    print("=== Netflix Region Explorer ===")
    region, df = select_region()

    while True:
        query, result = search_movie(df)

        if result is not None:
            print(f"Found in {region}")
            print(result[["show_title", "season_title", "category"]])
        else:
            print(f"{query} not found in {region}")
            check_others = input("Search other regions? (y/n): ").strip().lower()

            if check_others == "y":
                found = search_other_regions(query, exclude_region=region)
                if found:
                    for r, matches in found.items():
                        print(f"Found in {r}:")
                        print(matches[["show_title", "season_title", "category"]])
                else:
                    print("Not found in any regions")

        again = input("Search another title? (y/n): ").strip().lower()
        if again != "y":
            break


if __name__ == "__main__":
    main()
