# Health Log Anomaly Detection


This project provides a Python script to detect anomalies in user health logs using machine learning (Isolation Forest). It focuses on key vital signs including:

- Heart rate

- Blood pressure (systolic and diastolic)

- Respiration rate

- Blood Oxygen Percentage 


## Requirements

- pandas

- numpy

- matplotlib

- scikit-learn

---

## Installation

**Clone the Repository**
   ```bash
   git clone https://github.com/Pradyumna-RN/Health-anomaly.git
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

When prompted enter the path of the csv file.

```bash
Enter the path to the health logs CSV file:
```

## Output

The result will display the rows which are marked as anamoly True and a visual representation in the form of line graph
```
Detected anomalies using Isolation Forest:
             timestamp     HR  BP_sys  BP_dia    RR  ml_anomaly
10  2025-05-01 08:50:00  180.0   118.0     82.0  16.0        True
```


