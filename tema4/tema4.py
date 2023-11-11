# pip install pandas scikit-learn
# pip install tensorflow

import pandas as pd
from sklearn.model_selection import train_test_split
from tensorflow import keras
from keras.models import Sequential
from keras.layers import Dense
from keras.initializers import glorot_uniform

# citirea datelor din set
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/00236/seeds_dataset.txt"
column_names = ["area", "perimeter", "compactness", "length_of_kernel", "width_of_kernel", "asymmetry_coefficient", "length_of_kernel_groove", "class"]
data = pd.read_csv(url, sep="\s+", header=None, names=column_names)

# separarea datelor in caracterisitici si etichete
prop = data.drop("class", axis=1)
label = data["class"]

# impartirea setului in 25% date de testare & 75% date de antrenament
prop_train, prop_test, label_train, label_test = train_test_split(prop, label, test_size=0.25, random_state=42)

# initializare parametrii
input_dim = prop_train.shape[1] # dim stratului de intrare este 1
hidden_units = 64 # dim stratului ascuns
initializer = glorot_uniform(seed=42) # initializare de ponderi cu Glorot uniform
output_units = 3 # dim stratului de iesire (nr de clase din seeds_dataset)
learning_rate = 0.001 # rata de invatare
nr_epoci = 50 # nr maxim de epoci


# initializarea modelului
# model = Sequential()
# model.add(Dense(hidden_units, input_dim=input_dim, activation='relu', kernel_initializer=initializer)) # adaugarea stratului ascuns
# model.add(Dense(output_units, activation='softmax', kernel_initializer=initializer))

# compilare model
# model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy']) 
# model.summary()
