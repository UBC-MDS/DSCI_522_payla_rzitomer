# load_data.py
# Richie Zitomer and Ayla Pearson, Nov 2018
#
# This script loads in the data, gets rid of irrelevant features,
# makes dummy variables, makes target variable, and outputs the
# cleaned dataframe to a csv.
#
# Usage: python src/explore_data.py input_file output_file_prefix
# Example usage: python src/explore_data.py 'data/wine_data_cleaned.csv' 'results/viz_'
import pandas as pd
import argparse
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser()
parser.add_argument('input_file')
parser.add_argument('output_file_prefix')
args = parser.parse_args()

# Load data
wine_data_cleaned = pd.read_csv(args.input_file)

## Look at by country
france = wine_data_cleaned[wine_data_cleaned.country_France==1]
us = wine_data_cleaned[wine_data_cleaned.country_US==1]
italy = wine_data_cleaned[wine_data_cleaned.country_Italy==1]
spain = wine_data_cleaned[wine_data_cleaned.country_Spain==1]
portugal = wine_data_cleaned[wine_data_cleaned.country_Portugal==1]

x = ['USA', 'France', 'Italy', 'Spain', 'Portugal']
y = [100*sum(us.greater_than_90)/len(us),
     100*sum(france.greater_than_90)/len(france),
     100*sum(italy.greater_than_90)/len(italy),
     100*sum(spain.greater_than_90)/len(spain),
     100*sum(portugal.greater_than_90)/len(portugal)
    ]

fig, ax = plt.subplots()

plt.bar(x, y)
plt.axhline(100*sum(wine_data_cleaned.greater_than_90)/len(wine_data_cleaned),
            c='r', label="Overall Average")

# Also plot an average
ax.set_ylabel('Proportion of Wines With a Rating >= 90 Points (%)')
ax.set_xlabel('Country')
ax.set_title('Wine Quality for Top 5 Most Common Countries in the Dataset')
ax.legend()

plt.savefig(args.output_file_prefix + 'countries.png')


# Look at by price
greater = wine_data_cleaned[wine_data_cleaned.greater_than_90]
less_than = wine_data_cleaned[~wine_data_cleaned.greater_than_90]

fig, ax = plt.subplots()
plt.boxplot([less_than.price, greater.price],showfliers=False)
plt.xticks([1, 2], ['< 90', '>= 90'])

ax.set_ylabel('Price')
ax.set_xlabel('WineEnthusiast Rating')
ax.set_title('Price of Wine Segmented by Quality')

plt.savefig(args.output_file_prefix + 'price_boxplot.png')

greater = wine_data_cleaned[wine_data_cleaned.greater_than_90]
less_than = wine_data_cleaned[~wine_data_cleaned.greater_than_90]

# Look at histogram of price < 100
fig, ax = plt.subplots()

less_than[less_than.price<100].price.hist(bins=20, label='< 90')
greater[greater.price<100].price.hist(bins=20, alpha=.8, label='>= 90')

ax.set_ylabel('Count')
ax.set_xlabel('Bottle Price')
ax.set_title('Price of Wine Segmented by Quality for Wine Cheaper than $100')
ax.legend()

plt.savefig(args.output_file_prefix + 'price_less_than_100_hist.png')

# Look at by variety
pinot_noir = wine_data_cleaned[wine_data_cleaned['variety_Pinot Noir']==1]
chardonnay = wine_data_cleaned[wine_data_cleaned['variety_Chardonnay']==1]
cabernet_sauvignon = wine_data_cleaned[wine_data_cleaned['variety_Cabernet Sauvignon']==1]
red_blend = wine_data_cleaned[wine_data_cleaned['variety_Red Blend']==1]
bordeaux_style_red_blend = wine_data_cleaned[wine_data_cleaned['variety_Bordeaux-style Red Blend']==1]

x = ['Pinot Noir','Chardonnay','Caberney Sauvignon','Red Blend','Bordeaux Style Red Blend']
y = [100*sum(pinot_noir.greater_than_90)/len(pinot_noir),
     100*sum(chardonnay.greater_than_90)/len(chardonnay),
     100*sum(cabernet_sauvignon.greater_than_90)/len(cabernet_sauvignon),
     100*sum(red_blend.greater_than_90)/len(red_blend),
     100*sum(bordeaux_style_red_blend.greater_than_90)/len(bordeaux_style_red_blend)
    ]

fig, ax = plt.subplots()

plt.bar(x,y)
plt.axhline(100*sum(wine_data_cleaned.greater_than_90)/len(wine_data_cleaned),
            c='r', label="Overall Average")

# Also plot an average
ax.set_ylabel('Proportion of Wines With a Rating >= 90 Points (%)')
ax.set_xlabel('Variety')
ax.set_title('Wine Quality for Top 5 Most Common Varieties of Wine')
ax.legend()

plt.xticks(rotation=90)

plt.savefig(args.output_file_prefix + 'variety.png', bbox_inches="tight")
