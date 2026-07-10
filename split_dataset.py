import wfdb
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

record = wfdb.rdrecord("dataset/100")
signal = record.p_signal[:,0]

annotation = wfdb.rdann("dataset/100","atr")

window = 90

beats=[]
labels=[]

valid_labels=['N','A','V']

for sample,symbol in zip(annotation.sample,annotation.symbol):

    if symbol not in valid_labels:
        continue

    if sample-window>=0 and sample+window<len(signal):

        beat=signal[sample-window:sample+window]

        beats.append(beat)

        labels.append(symbol)

X=np.array(beats)

encoder=LabelEncoder()

y=encoder.fit_transform(labels)

X_train,X_test,y_train,y_test=train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# CNN expects 3 dimensions
X_train=X_train.reshape(X_train.shape[0],180,1)
X_test=X_test.reshape(X_test.shape[0],180,1)

print("Training:",X_train.shape)
print("Testing :",X_test.shape)

# Save dataset
np.save("dataset/X_train.npy",X_train)
np.save("dataset/X_test.npy",X_test)
np.save("dataset/y_train.npy",y_train)
np.save("dataset/y_test.npy",y_test)

print("Dataset Saved Successfully!")