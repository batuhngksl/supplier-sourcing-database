"""
Supplier Sourcing Database — Filter Script
==========================================
Filter suppliers by category, city, or keyword.

Usage:
    python filter_suppliers.py --category "Cotton Rugs"
    python filter_suppliers.py --city "Gaziantep"
    python filter_suppliers.py --keyword "tufting"
    python filter_suppliers.py --list-categories
"""

import argparse
import pandas as pd
import sys
import os


DATA_FILE = os.path.join(os.path.dirname(__file__), "..", "data", "suppliers.csv")


def load_data():
    """Load supplier database from CSV."""
    try:
        df = pd.read_csv(DATA_FILE, encoding="utf-8")
        return df
    except FileNotFoundError:
        print(f"Error: suppliers.csv not found at {DATA_FILE}")
        print("Make sure the data/ folder contains suppliers.csv")
        sys.exit(1)


def print_results(df, title="Results"):
    """Pretty print supplier results."""
    print(f"\n{'='*60}")
    print(f"  {title}  ({len(df)} suppliers found)")
    print(f"{'='*60}")

    if df.empty:
        print("  No suppliers found matching your criteria.")
        return

    for _, row in df.iterrows():
        print(f"\n  Company  : {row.get('Company Name', 'N/A')}")
        print(f"  Contact  : {row.get('Representative', 'N/A')} — {row.get('Title', '')}")
        print(f"  Email    : {row.get('Email', 'N/A')}")
        print(f"  Phone    : {row.get('Phone', 'N/A')}")
        print(f"  Products : {row.get('Products', 'N/A')}")
        print(f"  City     : {row.get('City', 'N/A')}")
        print(f"  Category : {row.get('Category', 'N/A')}")
        print(f"  {'-'*55}")


def main():
    parser = argparse.ArgumentParser(
        description="Filter the B2B supplier sourcing database."
    )
    parser.add_argument("--category", type=str, help="Filter by product category")
    parser.add_argument("--city", type=str, help="Filter by city")
    parser.add_argument("--keyword", type=str, help="Keyword search across all fields")
    parser.add_argument(
        "--list-categories", action="store_true", help="List all available categories"
    )
    parser.add_argument("--export", type=str, help="Export results to CSV file")

    args = parser.parse_args()
    df = load_data()

    # List categories
    if args.list_categories:
        categories = df["Category"].dropna().unique()
        print("\nAvailable Categories:")
        for cat in sorted(categories):
            count = len(df[df["Category"] == cat])
            print(f"  - {cat} ({count} suppliers)")
        return

    results = df.copy()

    # Apply filters
    if args.category:
        results = results[
            results["Category"].str.contains(args.category, case=False, na=False)
        ]

    if args.city:
        results = results[
            results["City"].str.contains(args.city, case=False, na=False)
        ]

    if args.keyword:
        mask = results.apply(
            lambda row: row.astype(str)
            .str.contains(args.keyword, case=False, na=False)
            .any(),
            axis=1,
        )
        results = results[mask]

    # Build title
    filters = []
    if args.category:
        filters.append(f"Category: {args.category}")
    if args.city:
        filters.append(f"City: {args.city}")
    if args.keyword:
        filters.append(f"Keyword: '{args.keyword}'")
    title = " | ".join(filters) if filters else "All Suppliers"

    print_results(results, title)

    # Optional CSV export
    if args.export:
        results.to_csv(args.export, index=False, encoding="utf-8")
        print(f"\n  ✓ Exported {len(results)} records to: {args.export}")


if __name__ == "__main__":
    main()
