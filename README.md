# Parameters for Predicting WineEnthusiast Ratings

## Proposal

#### 1. Choose a public data set from the web that you are interested in to carry out a small data analysis. You may also use any data set we have previously worked with in MDS. Prove to us that you can load the data set into R or Python (this could be demonstrating by writing a script that downloads the data and saves a snippet of it, for example).

Data set: https://www.kaggle.com/zynicide/wine-reviews   
First 100 rows of data is here: https://github.com/UBC-MDS/DSCI_522_payla_rzitomer/blob/master/docs/wine_data_first_100_rows.csv.   
Downloaded using this script: https://github.com/UBC-MDS/DSCI_522_payla_rzitomer/blob/master/src/load_data.py   


#### 2. With that data set, identify a question you would like to ask from it that could be answered by some simple analysis and visualization (more on this below). State what kind of question it is (it should be one of the 6 types discussed in lecture 1).

What are the strongest three predictors that a consumer has access to that will indicate if a wine will receive more than 90 points on WineEnthusiast?   
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
    - if the points column is less than or equal to 90 points then label the value for the row to be `False`

step 3:
- drop rows with Null values in them so they can be classified by the decision tree

step 4:
- break data into a train and test set

step 5:
- train the decision tree model to classify if the wine is 'Classic' or 'not Classic'

step 6:
- look at accuracy score

step 7:
- tune hyperparameters if needed (using test set)

step 8:
- evaluate a final accuracy score
- look at the top 3 predictors out of country, price, province, region, variety and winery



#### 4. Suggest how you might summarize the data to show this as a table or a number, as well as how you might show this as a visualization.

- look at accuracy score
- look at the ranking of the predictors and find the top 3
- accuracy score, and rank of top predictors can go in a table
- visualization of the decision tree model
- visualization of predictors (bar plot or point plot)
