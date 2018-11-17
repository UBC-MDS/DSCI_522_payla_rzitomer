import pandas as pd

# Usage python load_data.property
# This will output the first 100 rows of our data in the docs/ directory

def main():
    wine_data = pd.read_csv('../data/winemag-data-130k-v2.csv.zip',
                compression='zip',
                index_col=0) # Should I hardcode filename here or make it an arg?
    wine_data.head(100).to_csv('../docs/wine_data_first_100_rows.csv',
                                index=False)

if __name__ == '__main__':
    main()
