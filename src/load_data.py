# load_data.py
# Richie Zitomer and Ayla Pearson, Nov 2018
#
# This script outputs the first 100 rows of our input data on wine into
# the docs/ directory. It takes no arguements.
#
# Usage: python load_data.py

import pandas as pd

def main():
    wine_data = pd.read_csv('../data/winemag-data-130k-v2.csv.zip',
                compression='zip',
                index_col=0)
    wine_data.head(100).to_csv('../docs/wine_data_first_100_rows.csv',
                                index=False)

if __name__ == '__main__':
    main()
