# load_data.py
# Richie Zitomer and Ayla Pearson, Nov 2018
#
# This script loads in the data, gets rid of irrelevant features,
# makes dummy variables, makes target variable, and outputs the
# cleaned dataframe to a csv.
#
# Usage: python src/load_data.py input_file output_file viz_file describe_prefix
# Example usage: python src/load_data.py data/winemag-data-130k-v2.csv.zip data/wine_data_cleaned.csv results/viz_class_frequencies.png results/describe_

import pandas as pd   # Version 0.23.4
import argparse       # Version 1.1
import matplotlib.pyplot as plt  # Version 2.2.3

parser = argparse.ArgumentParser()
parser.add_argument('input_file')
parser.add_argument('output_file')
parser.add_argument('viz_file')
parser.add_argument('describe_prefix')
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

    # Output csvs describing the variables
    variety_describe = wine_data.variety.describe()
    variety_describe = variety_describe[['unique', 'top', 'freq']]
    variety_describe.index = ['Unique Values', 'Most Frequent Value', 'Count of Most Freq. Value']
    variety_describe = variety_describe.reset_index()
    variety_describe.columns = ['Statistic', 'Value']
    variety_describe.to_csv(args.describe_prefix + 'variety.csv', index=False)

    country_describe = wine_data.country.describe()
    country_describe = country_describe[['unique', 'top', 'freq']]
    country_describe.index = ['Unique Values', 'Most Frequent Value', 'Count of Most Freq. Value']
    country_describe = country_describe.reset_index()
    country_describe.columns = ['Statistic', 'Value']
    country_describe.to_csv(args.describe_prefix + 'country.csv', index=False)

    province_describe = wine_data.province.describe()
    province_describe = province_describe[['unique', 'top', 'freq']]
    province_describe.index = ['Unique Values', 'Most Frequent Value', 'Count of Most Freq. Value']
    province_describe = province_describe.reset_index()
    province_describe.columns = ['Statistic', 'Value']
    province_describe.to_csv(args.describe_prefix + 'province.csv', index=False)

    price_describe = wine_data.price.describe()
    price_describe = price_describe[['mean', 'std', 'min', '50%', 'max']]
    price_describe.index = ['Mean', 'Std Dev.', 'Min', 'Median', 'Max']
    price_describe = price_describe.reset_index()
    price_describe.columns = ['Statistic', 'Value']
    price_describe.to_csv(args.describe_prefix + 'price.csv', index=False)

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
