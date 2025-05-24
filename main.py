import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler

def load_health_data(file_path):
    """Load health log data from a CSV file."""
    df = pd.read_csv(file_path, parse_dates=['timestamp'])
    df.sort_values('timestamp', inplace=True)
    return df

def detect_anomalies_ml(df, columns, contamination=0.05):
    """Detect anomalies using Isolation Forest."""
    model = IsolationForest(contamination=contamination, random_state=42)
    scaler = StandardScaler()
    X = scaler.fit_transform(df[columns])
    df['ml_anomaly'] = model.fit_predict(X) == -1
    return df

def plot_anomalies(df, column):
    """Plot a single vital sign and highlight ML-detected anomalies."""
    plt.figure(figsize=(12, 6))
    plt.plot(df['timestamp'], df[column], label=column, color='blue')
    plt.scatter(
        df[df['ml_anomaly']]['timestamp'],
        df[df['ml_anomaly']][column],
        color='red',
        label='Anomaly (ML)'
    )
    plt.xlabel('Time')
    plt.ylabel(column.replace('_', ' ').title())
    plt.title(f'{column.replace("_", " ").title()} Anomalies (Isolation Forest)')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    file_path = "health_logs.csv"  # Update path if needed

    # Load data
    df = load_health_data(file_path)

    # Define the vital signs to monitor
    vital_signs = ['HR', 'BP_sys','BP_dia','RR']
    # Clean missing data
    df = df.dropna(subset=vital_signs)

    # Detect anomalies using Isolation Forest
    df = detect_anomalies_ml(df, vital_signs)

    # Output detected anomalies
    print("Detected anomalies using Isolation Forest:")
    print(df[df['ml_anomaly']])

    # Plot anomalies for each vital sign
    for col in vital_signs:
        plot_anomalies(df, col)



