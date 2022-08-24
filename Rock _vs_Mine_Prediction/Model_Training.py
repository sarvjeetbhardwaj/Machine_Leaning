from sklearn.metrics import accuracy_score,confusion_matrix,classification_report

class model_train():

    def train_model(self,model,x_train,y_train):
        model.fit(x_train,y_train)
        y_train_predictions = model.predict(x_train)
        print(f'For {model}\n')
        print(f'The accuracy is {accuracy_score(y_train, y_train_predictions)}')
        print(f'Confusion_matrix :: \n{confusion_matrix(y_train, y_train_predictions)}')
        print(f'Classification report :: \n{classification_report(y_train, y_train_predictions)}')
        
