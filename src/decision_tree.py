# decision_tree.py
# Richie Zitomer and Ayla Pearson, Nov 2018
#
# This script loads in the cleaned data, trains the decision tree model, determines 
# the optimal depth based on maximum test accuracy, and re-runs the final model on all 
# the data. It outputs the graph of training and test accuracy vs max depth, an image 
# of the decision tree with depth 3, and a csv with the feature ranking of all the parameters.  


# Usage: python src/decision_tree.py input_file output_folder
# Example: python src/decision_tree.py data/wine_data_cleaned.csv results/model_

# Python Version 3.7.0

import pandas as pd               #Version 0.23.4
import numpy as np                #Version 1.15.1
import argparse                   #Version 1.1
import matplotlib.pyplot as plt   #Version 2.2.3
import graphviz                   #Version 0.8.4
from sklearn.tree import DecisionTreeClassifier, export_graphviz  #Version 0.19.2
from sklearn.model_selection import train_test_split              #Version 0.19.2


parser = argparse.ArgumentParser()
parser.add_argument('input_file')
parser.add_argument('output_file_prefix')
args = parser.parse_args()


def main():
    # reads in cleaned csv file, which is an input to the function
    data = pd.read_csv(args.input_file)
    
    # gets column names from the input file for the input parameters of the model    
    column_names = list(data.columns)
    column_names_X = list(column_names[:-1])
    
    # assigns the input and output parameters for the model
    X = data.loc[:, column_names_X]
    y = data.greater_than_90
    
    #splits data into train set 80% and test set 20%
    Xtrain, Xtest, ytrain, ytest = train_test_split(X,y,test_size=0.2)
    
        
    #generates the plot of test and training accuracy vs max depth for the range of 2 to 50 in steps of 2
    test_accuracy = []
    train_accuracy = []
    depths = range(2, 50, 2)
    for max_depth in depths:      
        model_training = model_fit(Xtrain, ytrain, depth=max_depth)
        test_accuracy.append(model_training.score(Xtest,ytest))
        train_accuracy.append(model_training.score(Xtrain,ytrain))
        
    plt.plot(depths, test_accuracy, label = "Test")
    plt.plot(depths, train_accuracy, label = "Training")
    plt.xlabel("Tree Depth")
    plt.ylabel("Accuracy")
    plt.legend()
    plt.title("Decision Tree Accuracies from Depth 2 to 50")
    plt.savefig(args.output_file_prefix + "depth_decision.png");
    
    #finds the depth with the highest accurac
    max_test_accuracy = depths[np.argmax(test_accuracy)]
    
    # creates the final model with the depth determined from the test accuracy plot
    model_final = model_fit(X, y, max_test_accuracy)
    
    # creates png of the decision tree, depth 3
    dot_data = export_graphviz(model_final, out_file=None, 
                             feature_names= column_names_X ,  
                             class_names=["Rating less than 90", "Rating greater than 90"],  
                             filled=False, rounded=True,  
                             special_characters=True,
                             rotate = True,
                             max_depth = 3)  

    graph = graphviz.Source(dot_data) 
    graph.format = 'png'
    graph.render(args.output_file_prefix + "decision_tree_depth_3") 
    
    # creates list of feature ranking values
    rank_parameters = model_final.feature_importances_
    
    # creates a dataframe with feature names and feature ranking
    d = {'predictor': column_names_X, 'rank_value': rank_parameters}
    df_rank = pd.DataFrame(data=d)
    df_rank['predictor'] = df_rank['predictor'].str.replace("_", " ")
    
    # writes the feature ranking dataframe to the output file
    df_rank.to_csv(args.output_file_prefix + "rank.csv")
    


def model_fit(inputs, output, depth=None):
    '''
    fits the decision tree model with an input, output and depth. Depth is an optional
    parameter, if not include it chooses the default value for DecisionTreeClassifier
    '''
    model = DecisionTreeClassifier(max_depth=depth, random_state = 10)
    model.fit(inputs, output)
    return model
    

if __name__ == "__main__":
    main()
 