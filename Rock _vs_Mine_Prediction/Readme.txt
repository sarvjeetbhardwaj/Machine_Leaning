Statistical Analysis of Data ::

1.The DataSet provided is balanced.
2.There are no missing values that need to be dealt with.
3.There are a lot of outliers as seen from the box plot.
4.Based on the grouped-by data, there is a significant difference in rock and mine size.
5.We don't need to perform any kind of scaling as the data provided is already scaled.
7.On checking the correlation between various features , we found that no features are strongly correlated to any other feature.
  Hence keeping all the features intact.


Observations on Training models::

We have trained our dataset using the default parameters with LogisticRegression,SupportVectorClassifier,RandomForestClassifier
AdaBoostClassifier and GradientBoostingClassifier

For LogisticRegression()
    The accuracy is 0.8373493975903614
    Confusion_matrix ::
    [[79 10]
     [17 60]]
    Classification report ::
                precision    recall  f1-score   support

            M       0.82      0.89      0.85        89
            R       0.86      0.78      0.82        77

        accuracy                           0.84       166
        macro avg       0.84      0.83      0.84       166
        weighted avg    0.84      0.84      0.84       166

For SVC()
    The accuracy is 0.8493975903614458
    Confusion_matrix ::
    [[86  3]
    [15 62]]
    Classification report ::
                precision    recall  f1-score   support

            M       0.80      0.97      0.87        89
            R       0.95      0.71      0.81        77

        accuracy                            0.85       166
        macro avg       0.87      0.84      0.84       166
        weighted avg    0.87      0.85      0.85       166

For RandomForestClassifier()
    The accuracy is 1.0
    Confusion_matrix ::
    [[89  0]
    [ 0 77]]
    Classification report ::
                precision    recall  f1-score   support

            M       1.00      1.00      1.00        89
            R       1.00      1.00      1.00        77

        accuracy                                1.00       166
        macro avg           1.00      1.00      1.00       166
        weighted avg        1.00      1.00      1.00       166

For AdaBoostClassifier()
    The accuracy is 1.0
    Confusion_matrix ::
    [[89  0]
    [ 0 77]]
    Classification report ::
                precision    recall  f1-score   support

            M       1.00      1.00      1.00        89
            R       1.00      1.00      1.00        77

        accuracy                               1.00       166
        macro avg          1.00      1.00      1.00       166
        weighted avg       1.00      1.00      1.00       166

For GradientBoostingClassifier()
    The accuracy is 1.0
    Confusion_matrix ::
    [[89  0]
    [ 0 77]]
    Classification report ::
            M       1.00      1.00      1.00        89
            R       1.00      1.00      1.00        77

        accuracy                               1.00       166
        macro avg          1.00      1.00      1.00       166
        weighted avg       1.00      1.00      1.00       166


We observed that RandomForestClassifier,AdaBoostClassifier and GradientBoostingClassifier will have the  of overfitting as the 
accuracy score is 1.Hence we discard these ML models for training or dataset.

We will choose LogisticRegression to get the output of the test data(although SupportVectorClassifier has higher accuracy) because precision
and recall values donot have significant difference between Mine & Rock classes and their values are well balanced.