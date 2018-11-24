# load_data.py
# Richie Zitomer and Ayla Pearson, Nov 2018
#
# This script loads in the data, gets rid of irrelevant features,
# makes dummy variables, makes target variable, and outputs the
# cleaned dataframe to a csv.
#
# Usage: python src/load_data.py input_file output_file
# Example usage: python src/load_data.py 'data/winemag-data-130k-v2.csv.zip' 'data/wine_data_cleaned.csv'

import pandas as pd
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('input_file')
parser.add_argument('output_file')
args = parser.parse_args()


def main():
    # Load in the data
    wine_data = pd.read_csv(args.input_file, index_col=0)

    # Drop features and rows not used in analysis
    wine_data_relev_features = wine_data.drop(
        ['region_1','description', 'taster_name', 'taster_twitter_handle', 'title', 'designation', 'region_2', 'winery'], axis=1)
    wine_data_cleaned = wine_data_relev_features.dropna()

    # Feature Engineering
    wine_data_cleaned_with_dummies = pd.get_dummies(wine_data_cleaned)
    wine_data_cleaned_with_dummies['greater_than_90'] = wine_data_cleaned_with_dummies['points'] >= 90
    wine_data_cleaned_with_dummies = wine_data_cleaned_with_dummies.drop('points', axis=1)

    # Output file
    wine_data_cleaned_with_dummies.to_csv(args.output_file, index=False)


if __name__ == '__main__':
    main()
