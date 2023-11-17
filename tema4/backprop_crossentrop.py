import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

# Read the data
file_path = "https://archive.ics.uci.edu/ml/machine-learning-databases/00236/seeds_dataset.txt"
columns = ["area", "perimeter", "compactness", "length_of_kernel", "width_of_kernel", "asymmetry_coefficient", "length_of_kernel_groove", "class"]
data = pd.read_csv(file_path, header=None, names=columns, sep='\t+', engine='python')
data = data.sample(frac=1, random_state=42).reset_index(drop=True)  #shuffle

#split data in atributes and class
x = data.drop('class', axis=1).values
y = data['class'].values
#split the data into train and test sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)

#initialize the parameters
input_size = x_train.shape[1]
hidden_layer = 64
output_layer = 3
learning_rate = 0.001
nr_epochs = 10000

#Initialize weights
np.random.seed(42)
weights_hidden = np.random.randn(input_size, hidden_layer)
weights_output = np.random.randn(hidden_layer, output_layer) 

def one_hot_encode(labels, num_classes):
    return np.eye(num_classes)[labels - 1]

y_train_onehot = one_hot_encode(y_train, output_layer)
print(y_train_onehot)
y_test_onehot = one_hot_encode(y_test, output_layer)
print(y_test_onehot)

# Activation functions and derivatives
def sigmoid(x):
    return 1.0 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return sigmoid(x) * (1 - sigmoid(x))

def softmax(x):
    exp_x = np.exp(x - np.max(x, axis=-1, keepdims=True))
    return exp_x / np.sum(exp_x, axis=-1, keepdims=True)

# Error function and its derivative
def mean_squared_error(predicted, target):
    return np.mean(np.square(np.array(predicted).reshape(-1, 1) - np.array(target)))

def mean_squared_error_derivative(predicted, target):
    return 2 * (predicted - target.reshape(-1, 1)) / len(target)

def crossentropy(predicted, target):
    return -np.sum(target * np.log(predicted)) / len(target)

def crossentropy_derivative(predicted, target):
    return predicted - target

# Forward propagation
def forward_propagation(x, weights_hidden, weights_output):
    hidden_activation = sigmoid(np.dot(x, weights_hidden))
    output_activation = softmax(np.dot(hidden_activation, weights_output))
    return hidden_activation, output_activation


sample_indices = np.random.choice(len(x_train), size=5, replace=False)
x_sample = x_train[sample_indices]

# Forward propagation
hidden_activation, output_activation = forward_propagation(x_sample, weights_hidden, weights_output)

# Print the results
print("Input:")
print(x_sample)
#print("\nHidden Layer Activation:")
#print(hidden_activation)
print("\nOutput Layer Activation:")
print(output_activation)
# Back propagation
def back_propagation(x, y, weights_hidden, weights_output, learning_rate):
    hidden, outputs = forward_propagation(x, weights_hidden, weights_output)

    output_errors = crossentropy_derivative(outputs, np.array(y))  # error for output layer
    hidden_errors = np.dot(output_errors, weights_output.T) * sigmoid_derivative(np.array(hidden))  # error for hidden layer

    weights_output -= learning_rate * np.dot(np.array(hidden).T, output_errors) / len(x)  # update weights output layer
    weights_hidden -= learning_rate * np.dot(np.array(x).T, hidden_errors) / len(x)  # update weights hidden layer

    return weights_hidden, weights_output

# Training
for epoch in range(nr_epochs):
    weights_hidden, weights_output = back_propagation(x_train, y_train_onehot, weights_hidden, weights_output, learning_rate)
    _, train_outputs = forward_propagation(x_train, weights_hidden, weights_output)


# testare retea antrenata
_, test_outputs = forward_propagation(x_test, weights_hidden, weights_output)

test_error = mean_squared_error(test_outputs, y_test)
print(f"Test Error: {test_error}") # 1.58

def accuracy_score(y_test, predictions):
    correct_predictions = np.sum(y_test == predictions)
    return correct_predictions / len(y_test)
predictions = np.argmax(test_outputs, axis=1) + 1

print(predictions)
print(y_test)

print("\nfor 5th line:")
print(f"Atributres: {x_test[4]} \t Class: {y_test[4]}")
print(f"Output layer weights : {test_outputs[4]}")
print(f"Network prediciton: {predictions[4]}")
accuracy = accuracy_score(y_test, predictions)
print(f"\nAccuracy on the test set: {accuracy}") # 0.38