# result_plots.py
# Richie Zitomer and Ayla Pearson, Nov 2018
#
# This script loads in the ranking data for each parameter,
# creates a bar plot of the top 20 predictors. It also creates a bar plot
# zoomed in with the top 19 predictors. 


# Usage: python src/result_plots.py input_file output_file_directory
# Example: python src/result_plots.py results/model_rank.csv results/

#Python Version 3.7.0

import pandas as pd             #Version 0.23.4
import matplotlib.pyplot as plt #Version 2.2.3
import argparse                 #Version 1.1

parser = argparse.ArgumentParser()
parser.add_argument('input_file')
parser.add_argument('output_file_prefix')
args = parser.parse_args()



def main():
    
    # reads in feature ranking csv
    data = pd.read_csv(args.input_file)
    
    # sorts the csv so higher ranked feature are first
    sorted_by_rank = data.sort_values(by = 'rank_value', ascending = False)
    
    # creates lists of the top 20 features and the top 20 without the 1st feature
    top_20 = sorted_by_rank[:20]
    top_19 = top_20[1:20]
    
    # creates dataframe of top 3 results and writes it to a csv 
    top_3 = top_20[:3]
    top_3.to_csv(args.output_file_prefix + "top3.csv")
    
    
    # creates bar plot of the top 20 and top 19 features, it creates them side-by-side as subplots
    fig, ax = plt.subplots(ncols=1, nrows=2, figsize=(8,9))
    top_20_plot = top_20.plot.bar(y='rank_value', 
                                 x='predictor',  
                                 color = "maroon", 
                                 legend = None, 
                                 ax=ax[0], 
                                 title = "Top 20 Parameters")
    top_19_plot = top_19.plot.bar(y='rank_value', 
                                  x='predictor', 
                                  color = "maroon", 
                                  legend = None, 
                                  ax=ax[1], 
                                  title = "Zoomed View: Top 20 Features with Price Removed")
    
     
    top_20_plot.set_ylabel("Rank Value")
    top_20_plot.set_xlabel("")
    top_19_plot.set_ylabel("Rank Value")
    top_19_plot.set_xlabel("")
    plt.tight_layout()
    plt.rc('axes', titlesize=24)     # fontsize title
    plt.rc('axes', labelsize= 17)    # fontsize axis labels
    plt.rc('xtick', labelsize=17)    # fontsize xtick labels
    plt.rc('ytick', labelsize=13)    # fontsize ytick labels
    
    
    
    
    # writes the plots to file, this is the output of the script
    plt.savefig(args.output_file_prefix + "rank_plots.png")
    

if __name__ == "__main__":
    main()


