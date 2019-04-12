# IDS-Project

Abhishek Goyal
16UCS009

Akash Agrawal
16UCS020

Akshat Sharma
16UCS023

Animesh Gupta
16UCS038


## Objective: Apply ML Classification algorithms on a data set and get inferences from the data. Also show the algorithm and concept behind it.

## Dataset : Breast Cancer Wisconsin (Diagnostic) Data Set  link 

Source of dataset : Kaggle

Motive for choosing the dataset : Analysis of the data and predicting whether the cancer is Benign or Malignant using the features given in the dataset.

Data Analysis :

Shape of the dataset :  (569, 32)
Rows - 569 ,  Columns - 32

Features : 'id', 'diagnosis', 'radius_mean', 'texture_mean', 'perimeter_mean', 'area_mean', 'smoothness_mean', 'compactness_mean', 'concavity_mean',
'concave points_mean', 'symmetry_mean', 'fractal_dimension_mean',
'radius_se', 'texture_se', 'perimeter_se', 'area_se', 'smoothness_se', 'compactness_se', 'concavity_se', 'concave points_se', 'symmetry_se',
'fractal_dimension_se', 'radius_worst', 'texture_worst', 'perimeter_worst', 'area_worst', 'smoothness_worst', 'compactness_worst', 'concavity_worst', 'concave points_worst', 'symmetry_worst', 'fractal_dimension_worst’

Data types for features : 
id                               int64
diagnosis                       object

and more...

Target Feature :  ‘diagnosis’
Prediction of the Diagnosis - B or M,   B - Benign
                          M - Malignant
Number of occurrences :  B - 357
                     M - 212

Data Cleaning : Features that can be dropped, i.e features that doesn’t contribute in the analysis - ‘id’.
Reason : 
‘id’ column contains the id of all the samples taken in the dataset for recognition but it is not helpful in the analysis and prediction, so we will drop it.
Duplicate entries are also dropped if any.

The target feature ‘diagnosis’ is a categorical feature. We have used One hot encoding technique here using LabelEncoder() in python as many machine learning algorithms cannot operate on label data directly. They require all input variables and output variables to be numeric.
For categorical variables where no such ordinal relationship exists, the integer encoding is not enough. Thus, we have to encode it to 0 and 1 numericals in order to analyse it.
Now, B = 0
         M = 1
We have made a new column ‘diagnosis_enc’ with data type - int64 containing the encoded diagnosis made from one hot encoding.
 
We have to search for any missing or wrong values present in the dataset. Missing values creates problems in the analysis and should be handled accordingly.

Methods to handle missing data - 
Drop missing values - If there are very less missing values compared to the size of the dataset, then we can drop them because it will not much effect in our analysis.
Fill according to previous data - If there are large number of missing values in the dataset then we cannot drop them. Filling them using previous data could be a solution. For example - We can take either mean or median of the whole data of that column and fill missing values with it.

In our dataset there are no missing values and we can continue further our analysis.

Statistical Analysis - Calculation of Mean, Median, quartiles, total count, minimum and maximum values of all the features.
Here is the statistical analysis of the ‘radius_mean’ feature :

Analysis
Count
Mean
Std
Min
25%
50%
75%
Max
Radius_Mean
569.00
14.127
3.524
6.981
11.700
13.370
15.780
28.110

## Plots -

1. Histogram of mean radius :




2. Histogram of Mean texture : 
 


Plot of all the features :
Problem : Here as we have 32 features, so while plotting all of them at the same time they get overlapped and we cannot get much inference from it.

Plot of all the features using log scale :



Here as we have used log scale now we can see the plots of each feature more clearly and get inferences from it.

Reason : log scales allow a large range to be displayed without small values being compressed down into bottom of the graph.


Box plot of ‘texture_worst’ feature grouped by our target feature ‘diagnosis’ :




Scatter plot between mean radius and diagnosis : 




0 denotes B(Benign)
1 denotes M(Malignant)    

Inference - A Scatter plot depicts the relation between two quantitative variables.  Mean radius of benign are less than that of malignant. This is a very important feature as in further prediction we can say that for higher values of mean radius predicted diagnosis could be M(Malignant).
Thus, Mean Radius seems a good predictor of the outcome variable.

Scatter Plot between mean radius and mean perimeter :


Relationship between mean radius and mean perimeter can be seen through this scatter plot. 

Splitting of data in Test and Training set -

First we assign X as the whole dataset containing all the required features but dropping the encoded diagnosis feature and using that feature as target feature Y.

Then we split the data by 20% between test and train set resulting in :  X_train, X_test, Y_train, Y_test which will be used for training and testing our ML Classification algorithms.

Accuracy and other metrics for computing the goodness of the algorithm -

Accuracy is the most common metric used, however it does not guarantee it will always show correctly the goodness of the model as our dataset can be biased and imbalanced. The problem starts when the actual costs that we assign to every error are not equal. If we deal with a rare but fatal disease like cancer, the cost of failing to diagnose the disease of a sick person is much higher than the cost of sending a healthy person to more tests. Precision, Recall and F-score are other metrics which can be calculated. Cross-validation is a technique to evaluate predictive models by partitioning the original sample into a training set to train the model, and a test set to evaluate it. 

Machine Learning Classification Algorithms - 

K-nearest neighbors algorithm(KNN) - In KNN, K is the number of nearest neighbors. The number of neighbors is the core deciding factor. When K=1, then the algorithm is known as the nearest neighbor algorithm. Suppose P1 is the point, for which label needs to predict. First, you find the k closest point to P1 and then classify points by majority vote of its k neighbors. Each object votes for their class and the class with the most votes is taken as the prediction. For finding closest similar points, you find the distance between points using distance measures such as Euclidean distance, Hamming distance, Manhattan distance and Minkowski distance. KNN has the following basic steps:
Calculate distance
Find closest neighbors
Vote for labels

Here we have used 10 neighbors in our model. We then fit our model on to the training data, learning the data and its patterns and complexity. After the model has been trained we can start predicting on the test set(X_test). 

Predictions - [0 1 1 0 0 1 1 1 0 0 0 1 0 0 0 1 0 0 0 1 1 0 1 0 0 0 0 0 0 1 0 0 0 0 0 0 1
 0 1 0 0 1 0 0 0 0 0 0 0 0 1 1 0 0 0 0 0 1 0 0 0 1 1 0 0 0 1 1 0 0 1 1 0 0
 0 0 0 1 0 0 1 0 0 1 1 1 1 1 0 0 0 0 0 0 0 0 1 1 0 1 1 0 1 1 0 0 0 1 0 0 1
 0 0 1]

Accuracy Score - 0.9649122807017544

Our model has predicted on the new data with an accuracy of 96.49 %



Confusion Matrix -            
71
0
4
39

    True Positive (TP) - 39
    True Negative (TN) - 71
    False Positive (FP) - 0
    False Negative (FN) - 4

Precision, Recall, F1-Score :  Precision (P) = TP / (TP + FP)
                                  Recall  (R)  =  TP / (TP + FN)
                       F-score  =  2PR / (P + R)




Precision
Recall
F1- score
Support
B [0]
0.95
1.00
0.97
71
M [1]
1.00
0.91
0.95
43
Avg / total
0.97
0.96
0.96
114




Decision Tree Classifier - Decision tree builds classification or regression models in the form of a tree structure. 
    
We have taken criteria of classification as ‘gini index’ and the depth of the tree = 3 and minimum leaf = 5

Predictions - [0 1 1 0 0 1 1 1 0 0 0 1 0 0 0 1 0 0 0 1 1 0 1 0 0 0 0 0 0 1 0 0 0 0 0 0 1
 0 1 0 0 1 0 0 0 0 0 0 0 0 1 1 0 0 0 0 0 1 0 0 0 1 1 0 0 0 1 1 0 0 1 1 0 0
 0 0 0 1 0 0 1 0 0 1 1 1 1 1 0 0 0 0 0 0 0 0 1 1 0 1 1 0 1 1 0 0 0 1 0 0 1
 0 0 1]

Accuracy Score - 0.9473684210526315
This model is having an accuracy of 94.73 %






Confusion Matrix -            
69
2
4
39

    True Positive (TP) - 39
    True Negative (TN) - 69
    False Positive (FP) - 2
    False Negative (FN) - 4

Precision, Recall, F1-Score :




Precision
Recall
F1- score
Support
B [0]
0.95
0.97
0.96
71
M [1]
0.95
0.91
0.93
43
Avg / total
0.95
0.95
0.95
114



Logistic Regression - Logistic Regression is a binary classification algorithm which uses sigmoid function for calculating probability of happening of an event.

First we train the model on training set and then predict on test set.

Predictions - [0 1 1 0 0 1 1 1 0 0 0 1 0 1 0 1 0 0 0 1 0 0 1 0 0 0 0 0 0 1 0 0 0 0 0 0 1
 0 1 0 0 1 0 0 0 0 0 0 0 0 1 1 0 0 0 0 0 1 0 0 0 1 1 0 0 0 1 1 0 0 1 1 0 1
 0 0 0 0 0 0 1 0 0 1 1 1 1 1 0 0 0 0 0 0 0 0 1 1 0 1 1 0 1 1 0 0 0 1 0 0 1
 0 1 1]

Accuracy Score - 0.956140350877193
This model is having an accuracy of 95.61 %




Confusion Matrix -            
70
1
4
39

    True Positive (TP) - 39
    True Negative (TN) - 70
    False Positive (FP) - 1
    False Negative (FN) - 4

Precision, Recall, F1-Score :




Precision
Recall
F1- score
Support
B [0]
0.95
0.99
0.97
71
M [1]
0.97
0.91
0.94
43
Avg / total
0.95
0.96
0.96
114


//How does precision/recall and f-score is useful?
Plot of k-fold cross-validation scores comparing different classification algorithms -

We have 10 fold cross validation.

Cross-validation Scores
Max (Standard Deviation)
LR
0.953661 (0.035158)
KNN
0.920419 (0.049233)
DTC
0.929554 (0.042547)


Maximum cv-score - Logistic Regression


LR - Logistic Regression
KNN - K Neighbor Classifier
DTC - Decision Tree Classifier



## CONCLUSION - 

KNN Classifier can predict with highest accuracy of 96.49%
Logistic Regression predicts better than KNN and DTC on a small sample size, from the results we’ve received from cross-validation.

