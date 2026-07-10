import numpy as np
from collections import Counter

# Load labels
y_train = np.load("dataset/y_train.npy")

print("Training Class Distribution:")
print(Counter(y_train))