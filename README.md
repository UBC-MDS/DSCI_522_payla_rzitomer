# Parameters for Predicting WineEnthusiast<sup>1</sup> Ratings


## Overview

When buying a new bottle of wine you are always wondering will this wine be any good? Should I grab the one from France? or Spain? or Austrilia? There are always so many to chooses how do you know that bottle will be excellent. This analysis wanted to help people make an informed choice when staring at wine racks to know which bottles of wine are excellent in comparison to the rest. WineEnthusiast<sup>1</sup> is a  magazine that reviews wines and scores wines based off of a taste test. This analysis used machine learning to classify wine based on price, country, province and variety by using the WineEnthusiast data. We looked at the top predictors from these categories to determine the most important features that contribute to the ratings. From this analysis we are able to make predictions in the taste of wine based on its price, where it is from and what type of grapes were used. If you want to know how to pick an excellent bottle of wine before ever tasting it read on.

## Data

-- add screen shot of the orginal data 

## Running the analysis

To run this analysis using docker, pull our docker image here: https://hub.docker.com/r/rzitomer/top_predictors_for_great_wine/, clone/download the repository, and then run the following command (filling in PATH_ON_YOUR_COMPUTER with the absolute path of the root of this project on your computer):
```{bash}
docker run --rm  -v PATH_ON_YOUR_COMPUTER:/home/top_predictors_for_great_wine/ --memory=3g rzitomer/top_predictors_for_great_wine make -C '/home/top_predictors_for_great_wine/'
```

Note that you might have to increase the max memory allocated to docker to 3.0 GiB (its set at 2.0 GiB by default) to run this analysis. The reason so much memory is required is that the cleaned data file is quite large and so the `pd.read_csv` call is computationally expensive.

To reproduce this analysis without using our docker image, run the following from the root directory:
```{bash}
make all
```

`make all` will run the scripts in the order required to reproduce the same results and analysis as presented in this repo.


You can also reproduce this analysis by running the folowing scripts in the order shown:
```{bash}
python src/load_data.py input_file output_file viz_file       # The input file is the raw data from Kaggle, the output_file is our cleaned data. The viz_file has a visualization of rating frequencies used in our report.
python src/explore_data.py input_file output_folder  # The input file is the cleaned data (the output_file you got from running load_data.py). The output_folder is where to put the resulting viz files.
python src/decision_tree.py input_file output_folder   # The input file is the cleaned data (the output_file you got from running load_data.py). The output_folder is where to put the results of the model.  
python src/result_plots.py input_file output_folder  # The input file is the results of the model (the output_file you got from running decision_tree.py). The output_folder is where to put the files that visualize the model.
Rscript -e "rmarkdown::render('output_file')"        # This line renders our final report, which relies on the output_folder, output_file, and output_folder of explore_data.py, decision_tree.py, result_plots.py respectively.
```
Example of the scripts with the file names from the repo:    

```{bash}
python src/load_data.py data/winemag-data-130k-v2.csv.zip data/wine_data_cleaned.csv results/viz_class_frequencies
python src/explore_data.py data/wine_data_cleaned.csv results/viz_    
python src/decision_tree.py data/wine_data_cleaned.csv results/model_    
python src/result_plots.py results/model_rank.csv results/results_     
Rscript -e "rmarkdown::render('docs/results.Rmd')"     
```

## Dependencies

Packages and versions used during the analysis:

| Packages | Version |
|------|--------------|
| pandas | 0.23.4 |
| matplotlib | 2.2.3 |
| argparse  | 1.1 |
| numpy | 1.15.1 |
| graphviz | 0.8.4 |
| scikit-learn | 0.19.2 |
| rmarkdown |  |


| Languages | Version |
|----------| -------- |
| Python | 3.7.0 |
| R | 1.2.1114 |


### References

1. WineEnthusiast https://www.winemag.com/. Accessed November 2018
