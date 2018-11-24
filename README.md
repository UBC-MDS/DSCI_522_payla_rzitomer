# Parameters for Predicting WineEnthusiast<sup>1</sup> Ratings


## Overview

WineEnthusiast<sup>1</sup> is a magazine that reviews wines and provides a score based off of a taste test. This analysis evaluated WineEnthusiast<sup>1</sup> rating data with a machine learning algorithm to evaluate the importance of price, country, province and variety on ratings greater than or equal to 90 points. A decision tree model was used to evaluate the highest valued parameters. The threshold of 90 points was chosen as it is the line between very good and excellent wine.

## Scripts

To reproduce this analysis run the scripts in the order shown:
```{bash}
python src/load_data.py input_file output_file   
python src/explore_data.py input_file output_folder     
python src/decision_tree.py input_file output_file     
python src/result_plots.py input_file output_folder        
Rscript -e "rmarkdown::render('output_file')"   
```
Example of the scripts with the file names from the repo:    

```{bash}
python src/load_data.py data/winemag-data-130k-v2.csv.zip data/wine_data_cleaned.csv    
python src/explore_data.py data/wine_data_cleaned.csv results/viz_    
python src/decision_tree.py data/wine_data_cleaned.csv results/rank.csv     
python src/result_plots.py results/rank.csv results/results_     
Rscript -e "rmarkdown::render('docs/results.Rmd')"     
```

## Proposal

#### 1. Choose a public data set from the web that you are interested in to carry out a small data analysis. You may also use any data set we have previously worked with in MDS. Prove to us that you can load the data set into R or Python (this could be demonstrating by writing a script that downloads the data and saves a snippet of it, for example).

Data set: https://www.kaggle.com/zynicide/wine-reviews   
First 100 rows of data is here: https://github.com/UBC-MDS/DSCI_522_payla_rzitomer/blob/master/docs/wine_data_first_100_rows.csv.   

#### 2. With that data set, identify a question you would like to ask from it that could be answered by some simple analysis and visualization (more on this below). State what kind of question it is (it should be one of the 6 types discussed in lecture 1).

What are the strongest three predictors that a consumer has access to that will indicate if a wine will receive a WineEnthusiast<sup>1</sup> rating of 90 or greater?
Type of question: predictive


#### 3. Make a plan of how you will analyze the data (report an estimate and confidence intervals? hypothesis test? classification with a decision tree?). Choose something you know how to do (report an estimate and confidence intervals, a two-group hypothesis), or will learn how to do in the first week of block 3 (ANOVA, classification with a decision tree).

step 1:
- import data/load data set from kaggle

step 2:
- feature engineering
    - Drop features we don't plan on using because they would not be good predictors (e.g. >90% of the wines have different
    titles so that column won't generalize to new data points) or they're not relevant to the spirit of our question (e.g.
    the twitter handler of the WineEnthusiast taster who wrote the review could end up being predictive of review score,
    but it won't help an audience understand which wine to buy).
    - Convert categorical variables to a format that can be used for decision trees
        - We chose to do this by one_hot_encoding (due to the limitations of the decision tree classifier in scikit-learn,
        which can't handle categorical variables)
- make a binary column based on points as the dependent variable to be predicted
    - Make a column called `greater_than_90`
    - if the points column is 90 or greater then label the value for the row to be `True`
    - if the points column is less than 90 points then label the value for the row to be `False`

step 3:
- drop rows with Null values in them so they can be classified by the decision tree

step 4:
- break data into a training(80%) and test set(20%)

step 5:
- train the decision tree model to classify if the wine is 'greater_than_90' or 'not greater_than_90'

step 6:
- evaluate test accuracy to determine optimal tree depth, value with max depth will be used for hyperparameter of max depth

step 7:
- look at the top predictors out of country, price, province, variety and winery



#### 4. Suggest how you might summarize the data to show this as a table or a number, as well as how you might show this as a visualization.

- look at accuracy score
- look at the ranking of the predictors and find the top 3
- rank of top predictors can go in a table
- visualization of the decision tree model
- visualization of predictors (bar plot or point plot)



### References

1. WineEnthusiast https://www.winemag.com/. Accessed November 2018
