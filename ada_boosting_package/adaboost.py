import numpy as np
import argparse
import pandas as pd
import math
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt

def parse_argument():
    """
    Code for parsing arguments
    """
    parser = argparse.ArgumentParser(description='Parsing a file.')
    parser.add_argument('--train', nargs=1, required=True)
    parser.add_argument('--test', nargs=1, required=True)
    parser.add_argument('--numTrees', nargs=1, required=True)
    args = vars(parser.parse_args())
    return args

def conversion(x_array):
    return np.array([1 if x == 1 else 0 for x in x_array])

def adaboost(X, y, num_iter):
    """Given an numpy matrix X, a array y and num_iter return trees and weights 
   
    Input: X, y, num_iter
    Outputs: array of trees from DecisionTreeClassifier
             trees_weights array of floats
    Assumes y is in {-1, 1}^n
    """
    trees = []
    trees_weights = []
    N = X.shape[0]  # N=9
    w = np.ones(N) / N  # initiate w  =[1/9,1/9,1/9...]
    for i in range(num_iter):  # number of trees

        t = DecisionTreeClassifier(max_depth=1)
        t.fit(X, y, sample_weight=w)
        trees.append(t)
        G=t.predict(X)
        err = np.sum(w * (G != y)) / (np.sum(w))
        try:
            alpha = math.log((1 - err) / (err))
        except:
            alpha=math.log((1 - err) / 0.0000000000001)
        trees_weights.append(alpha)

        result = conversion(G != y)
        w = w * np.exp(alpha * result)

    return trees, trees_weights


def adaboost_predict(X, trees, trees_weights):
    """Given X, trees and weights predict Y
    assume Y in {-1, 1}^n
    """

    G=0
    for m in range(len(trees)):
        h=trees[m].predict(X)
        h=np.array(new_label(h))
        G += trees_weights[m] * h

    Yhat=[1 if g > 0 else 0 for g in G]

    return Yhat


def parse_spambase_data(filename):
    """ Given a filename return X and Y numpy arrays

    X is of size number of rows x num_features
    Y is an array of size the number of rows
    Y is the last element of each row.
    """

    df = pd.read_csv(filename, header=None)
    X = df.iloc[:, 0:-1].as_matrix()
    Y = df.iloc[:, -1].as_matrix()

    return X, Y


def new_label(Y):
    """ Transforms a vector od 0s and 1s in -1s and 1s.
    """
    return [-1. if y == 0. else 1. for y in Y]



def accuracy(y, pred):
    return np.sum(y == pred) / float(len(y))


def main():
    """
    This code is called from the command line via
    
    python adaboost_erin2.py --train [path to filename] --test [path to filename] --numTrees
    """
    args = parse_argument()
    train_file = args['train'][0]
    test_file = args['test'][0]
    num_trees = int(args['numTrees'][0])
    print train_file, test_file, num_trees

    X_train, Y_train = parse_spambase_data(train_file)
    X_test, Y_test = parse_spambase_data(test_file)

    trees, trees_weights=adaboost(X_train, Y_train,num_iter=num_trees)

    Yhat_test=adaboost_predict(X_test, trees,trees_weights)
    Yhat_train = adaboost_predict(X_train, trees,trees_weights)

    acc_test = accuracy(Y_test, Yhat_test)
    acc = accuracy(Y_train, Yhat_train)
    print("Train Accuracy %.4f" % acc)
    print("Test Accuracy %.4f" % acc_test)
    df=pd.read_csv(test_file, header=None)
    df.ix[:,'prediction']=Yhat_test
    df.to_csv('prediction.txt')


def get_best_numtrees():
    
    train_file='spambase.train'
    test_file='spambase.test'
    X_train, Y = parse_spambase_data(train_file)
    X_test, Y_test = parse_spambase_data(test_file)

    train_accuracy=[]
    test_accuracy=[]
    M = range(1,500,50)
    for num_trees in M:

        trees, trees_weights=adaboost(X_train, Y,num_iter=num_trees)

        Yhat_test=adaboost_predict(X_test, trees,trees_weights)
        Yhat = adaboost_predict(X_train, trees,trees_weights)

        acc_test = accuracy(Y_test, Yhat_test)
        acc = accuracy(Y, Yhat)
        train_accuracy.append(acc)
        test_accuracy.append(acc_test)

    plt.plot(M,train_accuracy,'g-', label='Training Accuracy')
    plt.plot(M,test_accuracy, 'b-', label='Val Accuracy')
    plt.legend()
    plt.ylabel('Accuracy rate')
    plt.xlabel('Number of trees')
    plt.ylim(0.8,1.03)
    plt.show()

    return


if __name__ == '__main__':
    main()







