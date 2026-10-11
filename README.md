# ECG Prediction using Deep Learning

A deep learning-based Electrocardiogram (ECG) classification system developed using **Python**, **TensorFlow/Keras**, and the **MIT-BIH Arrhythmia Database**. This project preprocesses ECG signals, extracts heartbeat segments, trains a Convolutional Neural Network (CNN), and classifies ECG beats into different arrhythmia classes.

---

## Project Overview

Cardiovascular diseases are among the leading causes of mortality worldwide. Early detection of abnormal heart rhythms (arrhythmias) can significantly improve diagnosis and treatment.

This project automates ECG beat classification by applying signal preprocessing and a CNN-based deep learning model to identify different heartbeat classes.

---

## Features

- ECG signal preprocessing
- Beat extraction from raw ECG recordings
- Label encoding
- Dataset splitting into training and testing sets
- Class distribution analysis
- CNN-based heartbeat classification
- Model training and evaluation
- ECG beat visualization

---

## Dataset

This project uses ECG recordings from the **MIT-BIH Arrhythmia Database**.

Dataset includes:

- ECG signals (.dat)
- Header files (.hea)
- Annotation files (.atr)

After preprocessing, the dataset is stored as:

```
dataset/
│── X_train.npy
│── X_test.npy
│── y_train.npy
│── y_test.npy
```

---

## Project Structure

```
ECG-Prediction/
│
├── dataset/
│   ├── 100.dat
│   ├── 100.hea
│   ├── 100.atr
│   ├── X_train.npy
│   ├── X_test.npy
│   ├── y_train.npy
│   └── y_test.npy
│
├── annotations.py
├── class_distribution.py
├── encode_labels.py
├── extract_beats.py
├── preprocessing.py
├── read_ecg.py
├── split_dataset.py
├── train_cnn.py
├── test.py
├── visualize_beats.py
├── requirements.txt
└── README.md
```

---

## Workflow

```
Raw ECG Signal
        │
        ▼
Read ECG Record
        │
        ▼
Preprocessing
        │
        ▼
Heartbeat Extraction
        │
        ▼
Label Encoding
        │
        ▼
Dataset Split
        │
        ▼
CNN Training
        │
        ▼
Prediction
        │
        ▼
Classification Result
```

---

## Technologies Used

- Python
- TensorFlow
- Keras
- NumPy
- Matplotlib
- WFDB
- Scikit-learn

---

## Installation

Clone the repository

```bash
git clone   git clone https://github.com/H3xiee/ECG-Prediction.git
```

Move into the project directory

```bash
cd ECG-Prediction
```

Install the required dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Project

### Read ECG Signals

```bash
python read_ecg.py
```

### Extract Heartbeats

```bash
python extract_beats.py
```

### Encode Labels

```bash
python encode_labels.py
```

### Split Dataset

```bash
python split_dataset.py
```

### Check Class Distribution

```bash
python class_distribution.py
```

### Train CNN Model

```bash
python train_cnn.py
```

### Test the Model

```bash
python test.py
```

---

## Model

The project uses a Convolutional Neural Network (CNN) for ECG beat classification.

Typical architecture:

- Input Layer
- Convolution Layer
- ReLU Activation
- Max Pooling
- Convolution Layer
- Max Pooling
- Flatten
- Dense Layer
- Output Layer

---

## Applications

- Arrhythmia Detection
- Clinical Decision Support
- Healthcare AI
- Biomedical Signal Processing
- Remote Patient Monitoring

---

## Future Improvements

- Support all MIT-BIH records
- Handle imbalanced datasets using data augmentation
- Implement CNN-LSTM architecture
- Real-time ECG classification
- Web application deployment
- Explainable AI (Grad-CAM/LIME)
- Multi-class arrhythmia prediction

---

## Author

**Krishika Chellappandian**

Bachelor of Technology – Biomedical Engineering

GitHub: https://github.com/H3xiee

---

## License

This project is intended for educational and research purposes.
