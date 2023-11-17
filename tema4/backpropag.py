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
nr_epochs = 10

#Initialize weights
np.random.seed(42)
weights_hidden = np.random.randn(input_size, hidden_layer)
weights_output = np.random.randn(hidden_layer, output_layer) 
print(len(x_test))

# Activation functions and derivatives
def sigmoid(x):
    return 1.0 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return sigmoid(x) * (1 - sigmoid(x))

# Error function and its derivative
def mean_squared_error(predicted, target):
    return np.mean(np.square(np.array(predicted).reshape(-1, 1) - np.array(target)))

def mean_squared_error_derivative(predicted, target):
    return 2 * (predicted - target.reshape(-1, 1)) / len(target)

# Forward propagation
def forward_propagation(x_samples, weights_hidden, weights_output):
    outputs = []
    hidden = []
    for x_sample in x_samples:
        hidden_activation = sigmoid(np.dot(x_sample, weights_hidden))
        output_activation = sigmoid(np.dot(hidden_activation, weights_output))
        hidden.append(hidden_activation)
        outputs.append(output_activation)
    return outputs, hidden


sample_indices = np.random.choice(len(x_train), size=5, replace=False)
x_sample = x_train[sample_indices]

outputs, hidden = forward_propagation(x_sample, weights_hidden, weights_output)

print("Input layer")
print(x_sample)
# print("Output of the neurons for hidden layer:")
# print(np.array(hidden))
print("Output of the neurons for output layer")
print(np.array(outputs))

# Back propagation
def back_propagation(x_samples, y_samples, weights_hidden, weights_output, learning_rate):
    outputs, hidden = forward_propagation(x_samples, weights_hidden, weights_output)

    output_errors = mean_squared_error_derivative(np.array(outputs), np.array(y_samples)) # eroare output layer
    hidden_errors = np.dot(output_errors, weights_output.T) * sigmoid_derivative(np.array(hidden)) # eroare hidden layer

    weights_output -= learning_rate * np.dot(np.array(hidden).T, output_errors) / len(x_samples) # update weights output layer
    weights_hidden -= learning_rate * np.dot(np.array(x_samples).T, hidden_errors) / len(x_samples) # update weights hidden layer

    return weights_hidden, weights_output

# Training
for epoch in range(nr_epochs):
    weights_hidden, weights_output = back_propagation(x_train, y_train, weights_hidden, weights_output, learning_rate)

    # squared error on the training set
    train_outputs, _ = forward_propagation(x_train, weights_hidden, weights_output)
    train_error = mean_squared_error(train_outputs, y_train)
    #print(f"Epoch {epoch + 1}/{nr_epochs}, Train Error: {train_error}")

# testare retea antrenata
test_outputs, _ = forward_propagation(x_test, weights_hidden, weights_output)

test_error = mean_squared_error(test_outputs, y_test)
print(f"Test Error: {test_error}") # 1.58

def accuracy_score(y_test, predictions):
    correct_predictions = np.sum(y_test == predictions)
    return correct_predictions / len(y_test)
predictions = np.argmax(test_outputs, axis=1) 
print(predictions)
print(y_test)
accuracy = accuracy_score(y_test, predictions)
print(f"Accuracy on the test set: {accuracy}") # 0.38