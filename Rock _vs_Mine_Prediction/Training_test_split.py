from sklearn.model_selection import train_test_split


class train_test():

    def test_train_split(self,X,y,test_size,stratify):
        x_train, x_test, y_train, y_test = train_test_split(X ,y, test_size=test_size, stratify=stratify)
        return x_train, x_test, y_train, y_test
