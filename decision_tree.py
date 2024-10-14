import csv
import random

# Function to load data from CSV file
def load_data(filename):
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        data = [row for row in reader]
    return data

# Preprocess the data
def preprocess_data(data):
    for row in data:
        row['age'] = {'youth': 0, 'middle_aged': 1, 'senior': 2}[row['age']]
        row['income'] = {'low': 0, 'medium': 1, 'high': 2}[row['income']]
        row['student'] = {'no': 0, 'yes': 1}[row['student']]
        row['credit_rating'] = {'fair': 0, 'excellent': 1}[row['credit_rating']]
        row['class_buys_computer'] = {'no': 0, 'yes': 1}[row['class_buys_computer']]
    return data

# Function to calculate entropy
def entropy(data):
    from math import log2
    total = len(data)
    if total == 0:
        return 0
    count_yes = sum(int(row['class_buys_computer']) for row in data)
    count_no = total - count_yes
    p_yes = count_yes / total
    p_no = count_no / total
    entropy_yes = -p_yes * log2(p_yes) if p_yes > 0 else 0
    entropy_no = -p_no * log2(p_no) if p_no > 0 else 0
    return entropy_yes + entropy_no

# Function to calculate information gain
def information_gain(data, attribute, value):
    subset1 = [row for row in data if int(row[attribute]) <= value]
    subset2 = [row for row in data if int(row[attribute]) > value]
    total_entropy = entropy(data)
    subset1_entropy = entropy(subset1)
    subset2_entropy = entropy(subset2)
    weighted_entropy = (len(subset1) / len(data)) * subset1_entropy + (len(subset2) / len(data)) * subset2_entropy
    return total_entropy - weighted_entropy

# Function to split the dataset
def split_data(data, attribute, value):
    subset1 = [row for row in data if int(row[attribute]) <= value]
    subset2 = [row for row in data if int(row[attribute]) > value]
    return subset1, subset2

# Function to find the best split
def best_split(data):
    best_gain = 0
    best_attribute = None
    best_value = None
    for attribute in ['age', 'income', 'student', 'credit_rating']:
        values = set(int(row[attribute]) for row in data)
        for value in values:
            gain = information_gain(data, attribute, value)
            if gain > best_gain:
                best_gain = gain
                best_attribute = attribute
                best_value = value
    return best_attribute, best_value

# Class for the decision tree node
class DecisionTreeNode:
    def __init__(self, attribute=None, value=None, true_branch=None, false_branch=None, prediction=None):
        self.attribute = attribute
        self.value = value
        self.true_branch = true_branch
        self.false_branch = false_branch
        self.prediction = prediction

# Function to build the decision tree
def build_tree(data):
    if len(data) == 0:
        return DecisionTreeNode()
    if all(int(row['class_buys_computer']) == int(data[0]['class_buys_computer']) for row in data):
        return DecisionTreeNode(prediction=int(data[0]['class_buys_computer']))
    attribute, value = best_split(data)
    if attribute is None:
        return DecisionTreeNode(prediction=max(set(int(row['class_buys_computer']) for row in data), key=lambda v: sum(int(row['class_buys_computer']) == v for row in data)))
    true_branch, false_branch = split_data(data, attribute, value)
    return DecisionTreeNode(attribute=attribute, value=value, true_branch=build_tree(true_branch), false_branch=build_tree(false_branch))

# Function to make predictions with the decision tree
def predict(tree, row):
    if tree.prediction is not None:
        return tree.prediction
    if int(row[tree.attribute]) <= tree.value:
        return predict(tree.true_branch, row)
    else:
        return predict(tree.false_branch, row)

# Load the data
data = load_data('data/data.csv')

# Preprocess the data
data = preprocess_data(data)

# Split the data into training and testing sets
random.shuffle(data)
split_index = int(0.7 * len(data))
train_data = data[:split_index]
test_data = data[split_index:]

# Train the decision tree
tree = build_tree(train_data)

# Make sample predictions
sample_predictions = [predict(tree, row) for row in test_data[:5]]
print(f'Sample Predictions: {sample_predictions}')

