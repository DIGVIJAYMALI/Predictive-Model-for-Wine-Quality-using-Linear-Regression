"""
Do not change the input and output format.
If our script cannot run your code or the format is improper, your code will not be graded.

The only functions you need to implement in this template is linear_regression_noreg, linear_regression_invertible，regularized_linear_regression,
tune_lambda, test_error and mapping_data.
"""

import numpy as np
import pandas as pd

###### Q1.1 ######
def mean_absolute_error(w, X, y):
    """
    Compute the mean absolute error on test set given X, y, and model parameter w.
    Inputs:
    - X: A numpy array of shape (num_samples, D) containing test feature.
    - y: A numpy array of shape (num_samples, ) containing test label
    - w: a numpy array of shape (D, )
    Returns:
    - err: the mean absolute error
    """
    #####################################################
    # TODO 1: Fill in your code here #
    #####################################################
 
    res=np.float64(np.dot(X,w))
    #res=res.transpose()
    diff=0
    for i in range(len(y)):
        diff+=np.absolute(y[i]-res[i])
    err=np.float64(diff/len(y))
    return err

###### Q1.2 ######
def linear_regression_noreg(X, y):
  """
  Compute the weight parameter given X and y.
  Inputs:
  - X: A numpy array of shape (num_samples, D) containing feature.
  - y: A numpy array of shape (num_samples, ) containing label
  Returns:
  - w: a numpy array of shape (D, )
  """
  #####################################################
  #	TODO 2: Fill in your code here #
  #####################################################		
  Xt=X.transpose()
  w=np.dot(np.dot(np.linalg.inv(np.dot(Xt,X)),Xt),y)
  return w

###### Q1.3 ######
def linear_regression_invertible(X, y):
    """
    Compute the weight parameter given X and y.
    Inputs:
    - X: A numpy array of shape (num_samples, D) containing feature.
    - y: A numpy array of shape (num_samples, ) containing label
    Returns:
    - w: a numpy array of shape (D, )
    """
    #####################################################
    # TODO 3: Fill in your code here #
    #####################################################
    Xt=X.transpose()
    Xnew=np.dot(Xt,X)
    w, v = np.linalg.eig(Xnew)
    while min(w)<10**(-5):
        Xnew=Xnew+10**(-1)*np.identity(len(Xnew))
        w, v = np.linalg.eig(Xnew)
    w=np.dot(np.dot(np.linalg.inv(Xnew),Xt),y)
    return w


###### Q1.4 ######
def regularized_linear_regression(X, y, lambd):
    """
    Compute the weight parameter given X, y and lambda.
    Inputs:
    - X: A numpy array of shape (num_samples, D) containing feature.
    - y: A numpy array of shape (num_samples, ) containing label
    - lambd: a float number containing regularization strength
    Returns:
    - w: a numpy array of shape (D, )
    """
  #####################################################
  # TODO 4: Fill in your code here #
  #####################################################		
    Xt=X.transpose()
    Xnew=np.dot(Xt,X)
    w=np.dot(np.dot(np.linalg.inv(Xnew+lambd*np.identity(len(Xnew))),Xt),y)
    return w

###### Q1.5 ######
def tune_lambda(Xtrain, ytrain, Xval, yval):
    """
    Find the best lambda value.
    Inputs:
    - Xtrain: A numpy array of shape (num_training_samples, D) containing training feature.
    - ytrain: A numpy array of shape (num_training_samples, ) containing training label
    - Xval: A numpy array of shape (num_val_samples, D) containing validation feature.
    - yval: A numpy array of shape (num_val_samples, ) containing validation label
    Returns:
    - bestlambda: the best lambda you find in lambds
    """
    #####################################################
    # TODO 5: Fill in your code here #
    #####################################################		
    x=-19
    ordlamda=10
    lambd=ordlamda**(x)
    minmae=np.inf
    while lambd<=10**(19):
        w=regularized_linear_regression(Xtrain,ytrain,lambd)
        m=mean_absolute_error(w, Xval, yval)
        if(m<minmae):
            minmae=m
            bestlambda=lambd
        x+=1    
        lambd=ordlamda**x
    return bestlambda
    

###### Q1.6 ######
def mapping_data(X, power):
    """
    Mapping the data.
    Inputs:
    - X: A numpy array of shape (num_training_samples, D) containing training feature.
    - power: A integer that indicate the power in polynomial regression
    Returns:
    - X: mapped_X, You can manully calculate the size of X based on the power and original size of X
    """
    #####################################################
    # TODO 6: Fill in your code here #
    #####################################################
    Xtemp=X
    for p in range(2,power+1):    
        X=np.concatenate((X,np.power(Xtemp,p)),axis=1)
    return X


