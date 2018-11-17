# Proposal

1.Choose a public data set from the web that you are interested in to carry out a small data analysis. You may also use any data set we have previously worked with in MDS. Prove to us that you can load the data set into R or Python (this could be demonstrating by writing a script that downloads the data and saves a snippet of it, for example).

Data set:
https://www.kaggle.com/zynicide/wine-reviews


2. With that data set, identify a question you would like to ask from it that could be answered by some simple analysis and visualization (more on this below). State what kind of question it is (it should be one of the 6 types discussed in lecture 1).

type of question: predictive

Can we use decision trees to predict if a wine has a WineEnthusiast rating above 90 point based on country, price, province, region, variety and winery?

3. Make a plan of how you will analyze the data (report an estimate and confidence intervals? hypothesis test? classification with a decision tree?). Choose something you know how to do (report an estimate and confidence intervals, a two-group hypothesis), or will learn how to do in the first week of block 3 (ANOVA, classification with a decision tree).

steps 1:
import data/load data set from kaggle

step 2:
feature engineering
- make a binary column based on points
- if greater than 90 then great rating
- if less than 90 not great rating

step 3:
- convert categorical variables to some format that can be used for decision trees

step 4:
- break data into a train and test set

step 5:
- train the decision tree model to classify if the wine is great or not great

step 6:
- look at accuracy score

step 7:
- tune hyperparameters if needed (from test set)

step 8:
- evaluate a final accuracy score, if the accuracy is above some threshold to conclude that we can use the given inputs to predict the WineEnthusiast rating is above 90.

- could we find a model that is accurate

4. Suggest how you might summarize the data to show this as a table or a number, as well as how you might show this as a visualization.

- look at accuracy score
- visualization of the decision tree model
