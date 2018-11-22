# load_data.py
# Richie Zitomer and Ayla Pearson, Nov 2018
#
# This script loads in the data, gets rid of irrelevant features,
# makes dummy variables, makes target variable, and outputs the
# cleaned dataframe to a csv.
#
# Usage: python src/explore_data.py input_file output_file
# Example usage: python load_data.py '../data/winemag-data-130k-v2.csv.zip' '../data/wine_data_cleaned.csv'
import pandas as pd
import matplotlib.pyplot as plt

file_name = 'data/wine_data_cleaned.csv'
output_file_prefix = 'results/viz_'

# Load data
wine_data_cleaned = pd.read_csv(file_name, index_col=0)

## Look at by country
france = wine_data_cleaned[wine_data_cleaned.country_France==1]
us = wine_data_cleaned[wine_data_cleaned.country_US==1]
italy = wine_data_cleaned[wine_data_cleaned.country_Italy==1]
spain = wine_data_cleaned[wine_data_cleaned.country_Spain==1]
portugal = wine_data_cleaned[wine_data_cleaned.country_Portugal==1]

x = ['USA','France','Italy','Spain','Portugal']
y = [100*sum(us.greater_than_90)/len(us),
     100*sum(france.greater_than_90)/len(france),
     100*sum(italy.greater_than_90)/len(italy),
     100*sum(spain.greater_than_90)/len(spain),
     100*sum(portugal.greater_than_90)/len(portugal)
    ]

fig, ax = plt.subplots()

plt.bar(x,y)
plt.axhline(100*sum(wine_data_cleaned.greater_than_90)/len(wine_data_cleaned),
            c='r', label="Overall Average")
# Also plot an average

ax.set_ylabel('Wines With a Rating > 90 Points (%)')
ax.set_xlabel('Country')
ax.set_title('Wine Quality for Top 5 Most Common Country')
ax.legend()

plt.savefig(output_file_prefix + 'countries.png')

# Look at by price
greater = wine_data_cleaned[wine_data_cleaned.greater_than_90]
less_than = wine_data_cleaned[~wine_data_cleaned.greater_than_90]

fig, ax = plt.subplots()
plt.boxplot([less_than.price,greater.price],showfliers=False)
plt.xticks([1, 2], ['<= 90', '> 90'])

ax.set_ylabel('Price')
ax.set_xlabel('WineEnthusiast Rating')
ax.set_title('Wine Quality by Price')

plt.savefig(output_file_prefix + 'price_boxplot.png')

greater = wine_data_cleaned[wine_data_cleaned.greater_than_90]
less_than = wine_data_cleaned[~wine_data_cleaned.greater_than_90]

# Look at histogram of price < 100
fig, ax = plt.subplots()

less_than[less_than.price<100].price.hist(bins=20, label='<= 90')
greater[greater.price<100].price.hist(bins=20, alpha=.8, label='> 90')

ax.set_ylabel('Price')
ax.set_xlabel('WineEnthusiast Rating')
ax.set_title('Wine Quality by Price')
ax.legend()

plt.savefig(output_file_prefix + 'price_less_than_100_hist.png')