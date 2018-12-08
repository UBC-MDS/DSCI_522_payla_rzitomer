# load_data.py
# Richie Zitomer and Ayla Pearson, Nov 2018
#
# This script loads in the data, gets rid of irrelevant features,
# makes dummy variables, makes target variable, and outputs the
# cleaned dataframe to a csv.
#
# Usage: python src/load_data.py input_file output_file viz_file
# Example usage: python src/load_data.py 'data/winemag-data-130k-v2.csv.zip' 'data/wine_data_cleaned.csv' 'results/viz_class_frequencies.png'

import pandas as pd   # Version 0.23.4
import argparse       # Version 1.1
import matplotlib.pyplot as plt  # Version 2.2.3

parser = argparse.ArgumentParser()
parser.add_argument('input_file')
parser.add_argument('output_file')
parser.add_argument('viz_file')
args = parser.parse_args()


def main():
    # Load in the data
    wine_data = pd.read_csv(args.input_file, index_col=0)

    # Drop features and rows not used in analysis
    wine_data_relev_features = wine_data.drop(
        ['region_1','description', 'taster_name', 'taster_twitter_handle', 'title', 'designation', 'region_2', 'winery'], axis=1)
    wine_data_cleaned = wine_data_relev_features.dropna()

    # Output image of value counts of categorical ratings
    fig, ax = plt.subplots()

    cat_ratings = wine_data_cleaned.points.apply(get_price_cats)
    cat_ratings_freq = cat_ratings.value_counts()
    cat_ratings_freq = cat_ratings_freq.loc[['Classic', 'Superb', 'Excellent', 'Very Good', 'Good ', 'Acceptable']]
    plt.bar(cat_ratings_freq.index, cat_ratings_freq)
    ax.set_ylabel('Count')
    ax.set_xlabel('WineEnthusiast Rating')
    ax.set_title("Counts of WineEnthusiast Ratings by Class")
    plt.xticks(rotation=90)
    plt.savefig(args.viz_file, bbox_inches="tight")

    # Feature Engineering
    wine_data_cleaned_with_dummies = pd.get_dummies(wine_data_cleaned)
    wine_data_cleaned_with_dummies['greater_than_90'] = wine_data_cleaned_with_dummies['points'] >= 90
    wine_data_cleaned_with_dummies = wine_data_cleaned_with_dummies.drop('points', axis=1)

    # Output file
    wine_data_cleaned_with_dummies.to_csv(args.output_file, index=False)


def get_price_cats(points):
    "Convert WineEnthusiast point value to its categorical rating"
    if points>= 98:
        return 'Classic'
    elif points>= 94 and points<98:
        return 'Superb'
    elif points>= 90 and points<94:
        return 'Excellent'
    elif points>= 87 and points<90:
        return 'Very Good'
    elif points>= 83 and points<87:
        return 'Good '
    elif points<83:
        return 'Acceptable'
    else:
        return None

if __name__ == '__main__':
    main()
