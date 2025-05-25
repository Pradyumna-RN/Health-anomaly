# Health Log Anomaly Detection


This project provides a Python script to detect anomalies in user health logs using machine learning (Isolation Forest). It focuses on key vital signs including:

- Heart rate

- Blood pressure (systolic and diastolic)

- Respiration rate


## Requirements

- pandas

- numpy

- matplotlib

- scikit-learn

---

## Installation

**Clone the Repository**
   ```bash
   git clone <your-repo-url>
   cd <your-project-directory>
   ```
---

## Install Dependencies
   ```bash
   pip install -r requirements.txt
   ```
---

**If requirements.txt is not present, manually install:**
   ```bash
   pip install pandas numpy matplotlib scikit-learn
   ```
---

## Usage
**Run the project using the main script:**
  ```bash
  python main.py
```

## Steps to run the project 


**Step 1: Run the main.py**

You'll see a list of images in the input folder.

Provide the number of images to be checked
```bash
Image files in the 'input' folder:
1. image1jpg
2. image2.jpg
3. image3.jpg
```

## Output

The result will be displayed as clear, moderate or blur according to the image
```
Result for 'image1.jpg': Clear
```


