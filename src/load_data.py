# load_data.py
# Richie Zitomer and Ayla Pearson, Nov 2018
#
# This script outputs the first 100 rows of our input data on wine into
# the docs/ directory. It takes no arguements.
#
# Usage: python load_data.py

import pandas as pd

input_file = '../data/winemag-data-130k-v2.csv.zip'
output_file = '../data/wine_data_cleaned.csv'

def main():
    wine_data = pd.read_csv(input_file, index_col=0)
    wine_data_relev_features = wine_data.drop(
        ['description', 'taster_name', 'taster_twitter_handle', 'title', 'designation', 'region_2', 'winery'], axis=1)
    wine_data_cleaned = wine_data_relev_features.dropna()
    wine_data_cleaned_with_dummies = pd.get_dummies(wine_data_cleaned)
    wine_data_cleaned_with_dummies['greater_than_90'] = wine_data_cleaned_with_dummies['points'] >= 90
    wine_data_cleaned_with_dummies.to_csv(output_file, index=False)



if __name__ == '__main__':
    main()
