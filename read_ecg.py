import wfdb
import matplotlib.pyplot as plt

# Read ECG Record 100
record = wfdb.rdrecord("dataset/100")

# Extract first ECG lead (MLII)
signal = record.p_signal[:, 0]

print("ECG Record Loaded Successfully!")
print("Number of Samples:", len(signal))
print("Sampling Frequency:", record.fs)
print("Signal Names:", record.sig_name)

# Plot ECG Signal
import wfdb
import matplotlib.pyplot as plt

# Read ECG Record
record = wfdb.rdrecord("dataset/100")

signal = record.p_signal[:,0]

fs = record.fs   # Sampling frequency

# Display first 10 seconds
samples = 10 * fs

plt.figure(figsize=(15,4))
plt.plot(signal[:samples])

plt.title("First 10 Seconds of ECG")
plt.xlabel("Samples")
plt.ylabel("Amplitude (mV)")
plt.grid(True)

plt.show()

