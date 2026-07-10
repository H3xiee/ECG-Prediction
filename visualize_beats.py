import wfdb
import matplotlib.pyplot as plt

# Load ECG
record = wfdb.rdrecord("dataset/100")
signal = record.p_signal[:, 0]

# Load annotations
annotation = wfdb.rdann("dataset/100", "atr")

# First 10 seconds
fs = record.fs
samples = 10 * fs

plt.figure(figsize=(15,5))
plt.plot(signal[:samples], label="ECG")

# Plot R-peaks
for sample, symbol in zip(annotation.sample, annotation.symbol):

    if sample < samples:

        plt.plot(sample, signal[sample], "ro")

        plt.text(sample,
                 signal[sample] + 0.12,
                 symbol,
                 fontsize=8,
                 color="red")

plt.title("ECG with Beat Labels")
plt.xlabel("Samples")
plt.ylabel("Amplitude (mV)")
plt.grid()

plt.show()