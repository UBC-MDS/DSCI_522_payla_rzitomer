# result_plots.py
# Richie Zitomer and Ayla Pearson, Nov 2018
#
# This script loads in the ranking for each parameter,
# creates a bar plot of the top 20 predictors. It also creates a bar plot
# zoomed in with the top 19 predictors. 
# 

# Usage: python src/result_plots.py input_file output_file_directory
# Example: python src/result_plots.py results/rank.csv results/


import pandas as pd
import matplotlib.pyplot as plt
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('input_file')
parser.add_argument('output_file')
args = parser.parse_args()

def main():
    
    data = pd.read_csv(args.input_file)
    sorted_by_rank = data.sort_values(by = 'rank_value', ascending = False)
    top_20 = sorted_by_rank[:20]
    top_19 = top_20[1:20]
    
    fig, ax = plt.subplots(ncols=2, figsize=(14,6))
    top_20_plot = top_20.plot.bar(y='rank_value', 
                                 x='predictor',  
                                 color = "maroon", 
                                 legend = None, 
                                 ax=ax[0], 
                                 title = "Top 20 Parameters for Predicting a WineEnthusiast rating")
    top_19_plot = top_19.plot.bar(y='rank_value', 
                                  x='predictor', 
                                  color = "maroon", 
                                  legend = None, 
                                  ax=ax[1], 
                                  title = "Zoomed View: Top 20 Predictors with Price Removed")
    
    top_20_plot.set_ylabel("Rank Value")
    top_20_plot.set_xlabel("Predictors")
    top_19_plot.set_ylabel("Rank Value")
    top_19_plot.set_xlabel("Predictors")
    plt.tight_layout()
    plt.savefig(args.output_file + "rank_plots.png")
    


if __name__ == "__main__":
    main()



