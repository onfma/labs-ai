import torch
from torch.utils.data import TensorDataset, DataLoader
import pandas as pd
import numpy as np

file_path = "seeds_dataset.txt"
columns = ['Attr1', 'Attr2', 'Attr3', 'Attr4', 'Attr5', 'Attr6', 'Attr7', 'Class']
data = pd.read_csv(file_path, header=None, names=columns, sep='\t+', engine='python')

data = data.sample(frac=1, random_state=42).reset_index(drop=True)
x = data.drop('Class', axis=1).values
y = data['Class'].values


class_counts = {1: 70, 2: 70, 3: 70}
train_indices, test_indices = [], []

for class_label, count in class_counts.items():
    class_indices = data[data['Class'] == class_label].index.tolist()
    train_size = int(0.7 * count)
    train_indices.extend(class_indices[:train_size])
    test_indices.extend(class_indices[train_size:])

x_train, y_train = x[train_indices], y[train_indices]
x_test, y_test = x[test_indices], y[test_indices]
