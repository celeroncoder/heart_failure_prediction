from sklearn.linear_model import LogisticRegression
from utils.globals import X_train, y_train


class baseline_model:
    def getModel(self):
        lr_clf = LogisticRegression(max_iter=1000)
        lr_clf.fit(X_train, y_train)

        return lr_clf

    def get_prediction(self, X_test):
        model = self.getModel()
        prediction = model.predict(X_test)

        return prediction
