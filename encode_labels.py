import wfdb
import numpy as np
from sklearn.preprocessing import LabelEncoder

# Read ECG
record = wfdb.rdrecord("dataset/100")
signal = record.p_signal[:,0]

# Read annotations
annotation = wfdb.rdann("dataset/100","atr")

window = 90

beats = []
labels = []

for sample, symbol in zip(annotation.sample, annotation.symbol):

    if sample-window >=0 and sample+window < len(signal):

        beat = signal[sample-window:sample+window]

        beats.append(beat)

        labels.append(symbol)

beats = np.array(beats)

# Encode labels
encoder = LabelEncoder()

encoded_labels = encoder.fit_transform(labels)

print("Classes:")
print(encoder.classes_)

print("\nFirst 20 Labels:")
print(labels[:20])

print("\nEncoded:")
print(encoded_labels[:20])