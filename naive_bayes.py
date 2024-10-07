import pandas as pd
import numpy as np

data = pd.read_csv('data/naive_bayes.csv')

label_encoders = {}
for column in data.columns:
    if data[column].dtype == 'object':
        le = {label: idx for idx, label in enumerate(data[column].unique())}
        data[column] = data[column].map(le)
        label_encoders[column] = le

X = data.drop('class_buys_computer', axis=1).values
y = data['class_buys_computer'].values

def train_test_split(X, y, test_size=0.3, random_state=42):
    np.random.seed(random_state)
    indices = np.random.permutation(len(X))
    test_size = int(len(X) * test_size)
    test_indices = indices[:test_size]
    train_indices = indices[test_size:]
    return X[train_indices], X[test_indices], y[train_indices], y[test_indices]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

class NaiveBayes:
    def fit(self, X, y):
        self.classes = np.unique(y)
        self.mean = {}
        self.var = {}
        self.priors = {}
        
        for c in self.classes:
            X_c = X[y == c]
            self.mean[c] = np.mean(X_c, axis=0)
            self.var[c] = np.var(X_c, axis=0)
            self.priors[c] = X_c.shape[0] / X.shape[0]
    
    def _calculate_likelihood(self, mean, var, x):
        eps = 1e-6  # to avoid division by zero
        coeff = 1.0 / np.sqrt(2.0 * np.pi * var + eps)
        exponent = np.exp(- (x - mean) ** 2 / (2 * var + eps))
        return coeff * exponent
    
    def _calculate_posterior(self, x):
        posteriors = []
        for c in self.classes:
            prior = np.log(self.priors[c])
            likelihood = np.sum(np.log(self._calculate_likelihood(self.mean[c], self.var[c], x)))
            posterior = prior + likelihood
            posteriors.append(posterior)
        return self.classes[np.argmax(posteriors)]
    
    def predict(self, X):
        return np.array([self._calculate_posterior(x) for x in X])

nb = NaiveBayes()
nb.fit(X_train, y_train)

y_pred = nb.predict(X_test)

accuracy = np.mean(y_pred == y_test)
print(f'Accuracy: {accuracy}')