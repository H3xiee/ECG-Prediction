import wfdb

# Read ECG annotations
annotation = wfdb.rdann("dataset/100", "atr")

print("Number of beats:", len(annotation.sample))

print("\nFirst 20 Beat Positions:")
print(annotation.sample[:20])

print("\nFirst 20 Beat Labels:")
print(annotation.symbol[:20])