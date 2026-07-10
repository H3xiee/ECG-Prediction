import wfdb
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt

# -----------------------------
# Load ECG Record
# -----------------------------
record = wfdb.rdrecord("dataset/100")
signal = record.p_signal[:,0]

fs = record.fs

# -----------------------------
# Bandpass Filter
# -----------------------------
def butter_bandpass(lowcut, highcut, fs, order=4):
    nyquist = 0.5 * fs
    low = lowcut / nyquist
    high = highcut / nyquist

    b, a = butter(order, [low, high], btype='band')
    return b, a

b, a = butter_bandpass(0.5, 40, fs)

filtered = filtfilt(b, a, signal)

# -----------------------------
# Plot Comparison
# -----------------------------
samples = 10 * fs

plt.figure(figsize=(15,5))

plt.plot(signal[:samples], label="Original")

plt.plot(filtered[:samples], label="Filtered")

plt.legend()

plt.title("Original vs Filtered ECG")

plt.xlabel("Samples")

plt.ylabel("Amplitude (mV)")

plt.grid()

plt.show()