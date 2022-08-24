from sklearn.linear_model import LogisticRegression
import pandas as pd
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report

training_data = pd.read_csv('./Rock _vs_Mine_Prediction/Training_data.csv')
test_data = pd.read_csv('./Rock _vs_Mine_Prediction/Test_data.csv')

x_train = training_data.iloc[:,:-1]
y_train = training_data.iloc[:,-1]

x_test = test_data.iloc[:,:-1]
y_test = test_data.iloc[:,-1]

lg_regresssion = LogisticRegression()
lg_regresssion.fit(x_train,y_train)

y_test_pred = lg_regresssion.predict(x_test)

print(f'Accuracy on test data is {accuracy_score(y_test, y_test_pred)}')
print(f'Confusion_matrix ::\n{confusion_matrix(y_test, y_test_pred)}')
print(f'Classification report ::\n{classification_report(y_test, y_test_pred)}')
