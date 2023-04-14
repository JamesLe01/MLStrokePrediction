from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import confusion_matrix
from sklearn.metrics import f1_score

class MyLogisticRegression:
    def __init__(self, X_train, X_test, y_train, y_test):
        self.X_train = X_train  # Design Matrix
        self.X_test = X_test  # Design Matrix
        self.y_train = y_train  # Label
        self.y_test = y_test  # Label
        
        parameters = {'C': [10**x for x in range(-4, 5)]}
        self.clf = GridSearchCV(LogisticRegression(max_iter=100000, solver='saga'), param_grid=parameters, n_jobs=-1)
    
    def train(self) -> float:
        self.clf.fit(self.X_train, self.y_train)
        print(f'Best Hyperparameters: {self.clf.best_params_}')
        return self.clf.score(self.X_test, self.y_test)
    
    def get_confusion_matrix(self):
        print(confusion_matrix(self.y_test, self.clf.predict(self.X_test)))
        print(f'f1-score: {f1_score(self.y_test, self.clf.predict(self.X_test))}')