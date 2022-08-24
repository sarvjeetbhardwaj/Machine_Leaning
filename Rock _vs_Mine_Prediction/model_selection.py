from Data_collection import read_data
from Basic_Eda_Statistical_Analysis import statistical_analysis
from Independent_and_Dependent_features import independent_dependent_features
from sklearn.model_selection import train_test_split
from Model_Training import model_train
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier,AdaBoostClassifier,GradientBoostingClassifier
import pandas as pd

data_file = read_data().read_data_file(header=None)

statistical_analysis(data_file)

X, y = independent_dependent_features().idv(data=data_file)

x_train, x_test, y_train, y_test = train_test_split(X ,y, test_size=0.2, stratify=y,random_state=42)

training_data=pd.concat([x_train,y_train],axis = 1)
training_data.to_csv('./Rock _vs_Mine_Prediction/Training_data.csv',index=False)

test_data=pd.concat([x_test,y_test],axis = 1)
test_data.to_csv('./Rock _vs_Mine_Prediction/Test_data.csv',index=False)

models_to_tested = [LogisticRegression(),SVC(),RandomForestClassifier(),AdaBoostClassifier(),GradientBoostingClassifier()]

for models in models_to_tested:
       model_train().train_model(model=models,x_train=x_train, y_train=y_train)









