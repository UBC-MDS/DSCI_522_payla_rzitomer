# Parameters for Predicting WineEnthusiast<sup>1</sup> Ratings

When buying a new bottle of wine you are always wondering will this wine be any good? Should I grab the one from France? or Spain? or Australia? There are always so many to chooses how do you know that bottle will be excellent. This analysis wanted to help people make an informed choice when trying to choose a wine. WineEnthusiast<sup>1</sup> magazine reviews wines and scores wines based off of a blind taste test. This analysis used machine learning to classify wine based on price, country, province and variety by using the WineEnthusiast<sup>1</sup> data. We looked at the top predictors from these categories to determine the most important features in the classification. If you want to know how to pick an excellent bottle of wine before ever tasting it read on.

The question this project aims to answer: **What are the strongest three predictors that a consumer has access to that will indicate if a wine will receive a WineEnthusiast rating of 90 or greater?**

## Dataset

The dataset<sup>2</sup> used in this analysis is from [Kaggle](https://www.kaggle.com/zynicide/wine-reviews/home) and is under an Attribution-ShareAlike License. The data was web scrapped from WineEnthusiast<sup>1</sup> on November 22nd, 2017.

## Reproducibility

This analysis has both a dockerfile and makefile and can be run reproducibility from either.

To run this analysis using docker, pull our docker image here: https://hub.docker.com/r/rzitomer/top_predictors_for_great_wine/, clone/download the repository, and then run the following command (filling in PATH_ON_YOUR_COMPUTER with the absolute path of the root of this project on your computer) from the root directory of this project:
```{bash}
docker run --rm  -v PATH_ON_YOUR_COMPUTER:/home/top_predictors_for_great_wine/ --memory=3g rzitomer/top_predictors_for_great_wine make -C '/home/top_predictors_for_great_wine/'
```

Note that you might have to increase the max memory allocated to docker to 3.0 GiB (its set at 2.0 GiB by default) to run this analysis. The reason so much memory is required is that the cleaned data file is quite large and so the `pd.read_csv` call is computationally expensive.

To clean up the analysis type:
```{bash}
docker run --rm  -v PATH_ON_YOUR_COMPUTER:/home/top_predictors_for_great_wine/ --memory=3g rzitomer/top_predictors_for_great_wine make -C '/home/top_predictors_for_great_wine/' clean
```

To reproduce this analysis with our makefile, clone or download the repository and then run the following from the root directory of this project:
```{bash}
make all
```
`make all` will run the scripts in the required order to reproduce the same results and analysis as presented. A list of the dependencies are below and in each script in the src directory.

To remove all the outputs and run the analysis clean run this from the root directory of this project:
```{bash}
make clean
```
`make clean` will remove all of the files and figures for the analysis and restart the analysis at unzipping and reading in the original file.


## Data Analysis Pipeline

To reproduce the analysis manually the scripts should be run own in the order shown:
```{bash}
python src/load_data.py input_file output_file viz_file       # The input file is the raw data from Kaggle, the output_file is our cleaned data. The viz_file has a visualization of rating frequencies used in our report.
python src/explore_data.py input_file output_folder  # The input file is the cleaned data (the output_file you got from running load_data.py). The output_folder is where to put the resulting viz files.
python src/decision_tree.py input_file output_folder   # The input file is the cleaned data (the output_file you got from running load_data.py). The output_folder is where to put the results of the model.  
python src/result_plots.py input_file output_folder  # The input file is the results of the model (the output_file you got from running decision_tree.py). The output_folder is where to put the files that visualize the model.
Rscript -e "rmarkdown::render('output_file')"        # This line renders our final report, which relies on the output_folder, output_file, and output_folder of explore_data.py, decision_tree.py, result_plots.py respectively.
```
Example of the scripts with the file names from the repo:    

```{bash}
python src/load_data.py data/winemag-data-130k-v2.csv.zip data/wine_data_cleaned.csv results/viz_class_frequencies.png
python src/explore_data.py data/wine_data_cleaned.csv results/viz_    
python src/decision_tree.py data/wine_data_cleaned.csv results/model_    
python src/result_plots.py results/model_rank.csv results/results_     
Rscript -e "rmarkdown::render('docs/results.Rmd')"     
```

## Dependencies

| Programs/Languages | Version |
|----------| -------- |
| Python | 3.7.0 |
| R | 1.2.1114 |
| Make | 4.2.1 |


| Packages | Version |
|------|--------------|
| `pandas` | 0.23.4 |
| `matplotlib` | 2.2.3 |
| `argparse`  | 1.1 |
| `numpy` | 1.15.1 |
| `graphviz` | 0.8.4 |
| `scikit-learn` | 0.19.2 |
| `rmarkdown` | 1.10 |
| `tidyverse` | 1.2.1 |
| `knitr` | 1.20 |


### References

1. WineEnthusiast https://www.winemag.com/. Accessed November 2018

2. Thoutt, Z. (2017, Nov). Wine Reviews, Version 2. Retrieved November 15, 2018 from https://www.kaggle.com/zynicide/wine-reviews/home.
