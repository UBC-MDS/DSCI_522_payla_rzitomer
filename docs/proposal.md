# Proposal

#### 1. Choose a public data set from the web that you are interested in to carry out a small data analysis. You may also use any data set we have previously worked with in MDS. Prove to us that you can load the data set into R or Python (this could be demonstrating by writing a script that downloads the data and saves a snippet of it, for example).

Data set: https://www.kaggle.com/zynicide/wine-reviews   
First 100 rows of data is here: https://github.com/UBC-MDS/DSCI_522_payla_rzitomer/blob/master/docs/wine_data_first_100_rows.csv.   
Downloaded using this script: https://github.com/UBC-MDS/DSCI_522_payla_rzitomer/blob/master/src/load_data.py   


#### 2. With that data set, identify a question you would like to ask from it that could be answered by some simple analysis and visualization (more on this below). State what kind of question it is (it should be one of the 6 types discussed in lecture 1).

What are the strongest three predictors to indicate if a wine is a Classic(WineEnthusiast rating) wine?   
type of question: predictive


#### 3. Make a plan of how you will analyze the data (report an estimate and confidence intervals? hypothesis test? classification with a decision tree?). Choose something you know how to do (report an estimate and confidence intervals, a two-group hypothesis), or will learn how to do in the first week of block 3 (ANOVA, classification with a decision tree).

step 1:
- import data/load data set from kaggle

step 2:
- feature engineering
- make a binary column based on points
  - if 98 points or greater then assign Classic rating
  - if less than 98 points assign not Classic rating

step 3:
- convert categorical variables to format that can be used for decision trees

step 4:
- break data into a train and test set

step 5:
- train the decision tree model to classify if the wine is Classic or not Classic

step 6:
- look at accuracy score

step 7:
- tune hyperparameters if needed (from test set)

step 8:
- evaluate a final accuracy score
- look at the top 3 predictors out of country, price, province, region, variety and winery



#### 4. Suggest how you might summarize the data to show this as a table or a number, as well as how you might show this as a visualization.

- look at accuracy score
- look at the ranking of the predictors and find the top 3
- accuracy score, and rank of top predictors can go in a table 
- visualization of the decision tree model
- visualization of predictors (bar plot or point plot)
