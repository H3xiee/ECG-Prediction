import wfdb
import numpy as np
import matplotlib.pyplot as plt

# Load ECG
record = wfdb.rdrecord("dataset/100")
signal = record.p_signal[:,0]

# Load annotations
annotation = wfdb.rdann("dataset/100","atr")

window = 90

beats = []
labels = []

for sample, symbol in zip(annotation.sample, annotation.symbol):

    if sample-window >= 0 and sample+window < len(signal):

        beat = signal[sample-window:sample+window]

        beats.append(beat)

        labels.append(symbol)

beats = np.array(beats)

print("Total Beats:", len(beats))
print("Shape:", beats.shape)

# Plot first heartbeat
plt.figure(figsize=(10,4))
plt.plot(beats[1])

plt.title(f"Heartbeat Label: {labels[1]}")

plt.xlabel("Samples")

plt.ylabel("Amplitude")

plt.grid()

plt.show()
