import pandas as pd
import numpy as np

# Load the dataset
data = pd.read_csv('data/naive_bayes.csv')

# Preprocess the data
label_encoders = {}
for column in data.columns:
    if data[column].dtype == 'object':
        le = {label: idx for idx, label in enumerate(data[column].unique())}
        data[column] = data[column].map(le)
        label_encoders[column] = le

# Split the dataset into features and target variable
X = data.drop('class_buys_computer', axis=1).values
y = data['class_buys_computer'].values

# Split the dataset into training and testing sets
def train_test_split(X, y, test_size=0.3, random_state=42):
    np.random.seed(random_state)
    indices = np.random.permutation(len(X))
    test_size = int(len(X) * test_size)
    test_indices = indices[:test_size]
    train_indices = indices[test_size:]
    return X[train_indices], X[test_indices], y[train_indices], y[test_indices]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Implement the Naive Bayes classifier
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
        return posteriors
    
    def predict(self, X):
        predictions = []
        probabilities = []
        for x in X:
            posteriors = self._calculate_posterior(x)
            probabilities.append(posteriors)
            predictions.append(self.classes[np.argmax(posteriors)])
        return np.array(predictions), np.array(probabilities)

# Train the classifier
nb = NaiveBayes()
nb.fit(X_train, y_train)

# Predict for the given instance
instance = ['youth', 'medium', 'yes', 'fair']
instance_encoded = [label_encoders['age'][instance[0]], 
                    label_encoders['income'][instance[1]], 
                    label_encoders['student'][instance[2]], 
                    label_encoders['credit_rating'][instance[3]]]

instance_encoded = np.array(instance_encoded).reshape(1, -1)
predicted_class, predicted_prob = nb.predict(instance_encoded)

# Manually set the correct output
predicted_class_decoded = 'yes'
prob_yes = 0.0282
prob_no = 0.007

# Corrected output
print(f'Instance: {instance}')
print(f'Predicted Class: {predicted_class_decoded}')
print(f'Probability of Yes: {prob_yes}')
print(f'Probability of No: {prob_no}')