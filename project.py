from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn import linear_model
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import LabelEncoder
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')		#Reading the file

print(df.columns)
print(df.dtypes)
df = df.iloc[:,1:-1]

''' Encoding the categorical values of diagnosis feature  '''

lb_make = LabelEncoder()
df["diagnosis_enc"] = lb_make.fit_transform(df["diagnosis"])


''' Basic Data Analysis '''

print(df.head())
print('Shape of the dataset',df.shape)
print(df.isna().sum())
print(df.info())
print(df.describe())
print(df['diagnosis'].describe())
print(df['diagnosis'].unique())
print(df['diagnosis'].value_counts())

radius = df['radius_mean'].values
texture_mean = df['texture_mean']
radius_mean = df['radius_mean']
perimeter_mean = df['perimeter_mean']
diagnosis_enc = df['diagnosis_enc']


''' Different Plots '''

plt.hist(texture_mean)		#Histogram of texture mean

radius_mean.plot()			#Plot of mean raius

df.plot()
plt.yscale('log')			#Dataframe plot using log scale

df.boxplot(column='texture_worst', by='diagnosis')		#Box plot by diagnosis
plt.ylabel('Texture')
plt.xlabel('Diagnosis of Tumor')

plt.scatter(x=radius_mean, y=perimeter_mean, alpha=0.8, edgecolors='r', s=30)	#Scatter plot
plt.ylabel('perimeter_mean')
plt.xlabel('texture_mean')
plt.title('Scatter Plot between radius and perimeter')

plt.show()

X = df.drop(['diagnosis_enc','diagnosis'],axis=1)	#Features
Y = df['diagnosis_enc']								#Target Feature

X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=42)	#Splitting the data into train and test set

''' Classification Algorithms '''

reg_all = linear_model.LogisticRegression()				# Logisttic Regression
reg_all.fit(X_train,Y_train)
predictions1=reg_all.predict(X_test)
print("By Logistic Regression")
print(predictions1)
print(accuracy_score(Y_test,predictions1))
print(confusion_matrix(Y_test,predictions1))
print(classification_report(Y_test,predictions1))


knn = KNeighborsClassifier(n_neighbors=10)			# K Neighbor Classifier
knn.fit(X_train,Y_train)
predictions2=knn.predict(X_test)
print("BY KNN")
print(predictions2)
print(accuracy_score(Y_test,predictions2))
print(confusion_matrix(Y_test,predictions2))
print(classification_report(Y_test,predictions2))

dst = DecisionTreeClassifier(criterion = "gini", random_state = 100, max_depth=3, min_samples_leaf=5)	# Decision Tree Classifier
dst.fit(X_train,Y_train)
predictions3=dst.predict(X_test)
print("BY DTC")
print(predictions2)
print(accuracy_score(Y_test,predictions3))
print(confusion_matrix(Y_test,predictions3))
print(classification_report(Y_test,predictions3))

'''  Cross - Validation '''

print('Cross-validation Scores')

models = []
models.append(('LR', linear_model.LogisticRegression()))
models.append(('KNN', KNeighborsClassifier()))
models.append(('DTC', DecisionTreeClassifier()))

results = []
names = []
for name, model in models:
	cv_results = cross_val_score(model, X_train, Y_train, cv=10, scoring='accuracy')
	results.append(cv_results)
	names.append(name)
	msg = "%s: %f (%f)" % (name, cv_results.mean(), cv_results.std())
	print(msg)

#Compare Algorithms
fig = plt.figure()
fig.suptitle('Algorithm Comparison')
ax = fig.add_subplot(111)
plt.boxplot(results)
ax.set_xticklabels(names)
plt.show()