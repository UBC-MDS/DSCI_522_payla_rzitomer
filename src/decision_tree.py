# decision_tree.py
# Richie Zitomer and Ayla Pearson, Nov 2018
#
# This script loads in the cleaned data and trains the decision tree model,
# determines the optimal depth based on maximum test accuracy,
# runs the final model on all the data. 
# It outputs the graph of training and test accuracy, decision tree with depth 3,
# and a csv with the ranking of all the parameters.  


# Usage: python src/decision_tree.py input_file output_file
# Example: python src/decision_tree.py data/wine_data_cleaned.csv results/rank.csv


import pandas as pd
import numpy as np
import argparse

import matplotlib.pyplot as plt
import graphviz 

from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn.model_selection import train_test_split 


parser = argparse.ArgumentParser()
parser.add_argument('input_file')
parser.add_argument('output_file')
args = parser.parse_args()


def main():

    data = pd.read_csv(args.input_file)
        
    column_names = list(data.columns)
    column_names_X = list(column_names[:-1])
    
    X = data.loc[:, column_names_X]
    y = data.greater_than_90
    
    Xtrain, Xtest, ytrain, ytest = train_test_split(X,y,test_size=0.2)
    
        
    
    test_accuracy = []
    depths = range(2, 50, 2)
    for max_depth in depths:      
        model_training = model_fit(Xtrain, ytrain, depth=max_depth)
        test_accuracy.append(model_training.score(Xtest,ytest))
        
    plt.plot(depths, test_accuracy, label = "Test")
    plt.xlabel("Tree Depth")
    plt.ylabel("Accuracy")
    plt.legend()
    plt.title("Decision Tree Test Accuracy from Depth 2 to 50")
    plt.savefig("results/depth_decision.png");
    
    max_test_accuracy = depths[np.argmax(test_accuracy)]
    
    # creates the final model with the depth determined from the fine tuning
    model_final = model_fit(X, y, max_test_accuracy)
    
    # creates pdf of the decision tree, depth 3
    
    dot_data = export_graphviz(model_final, out_file=None, 
                             feature_names= column_names_X ,  
                             class_names=["Rating less than 90", "Rating greater than 90"],  
                             filled=False, rounded=True,  
                             special_characters=True, 
                             max_depth = 3)  

    graph = graphviz.Source(dot_data) 
    graph.format = 'png'
    graph.render("decision_tree_depth_3", directory = 'results', view=True) 
    
    
    rank_parameters = model_final.feature_importances_
    
    d = {'predictor': column_names_X, 'rank_value': rank_parameters}
    df_rank = pd.DataFrame(data=d)
    df_rank.to_csv(args.output_file)
    


def model_fit(inputs, output, depth=None):
    
    model = DecisionTreeClassifier(max_depth=depth)
    model.fit(inputs, output)
    return model
    

if __name__ == "__main__":
    main()
 