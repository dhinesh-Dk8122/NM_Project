
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
from sklearn.ensemble import RandomForestClassifier 
from sklearn.model_selection import train_test_split 
from sklearn.metrics import classification_report 

# Load dataset
sensor_data = pd.read_excel("sample_sensor_data.xlsx")

# Encode labels
sensor_data['label_encoded'] = sensor_data['label'].astype('category').cat.codes 

# Features and labels
X = sensor_data[['strain', 'vibration', 'temperature']] 
y = sensor_data['label_encoded'] 

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42) 

# Train model
model = RandomForestClassifier(n_estimators=100) 
model.fit(X_train, y_train) 

# Predictions and evaluation
y_pred = model.predict(X_test) 
print(classification_report(y_test, y_pred)) 

# Plot sample sensor readings
plt.figure(figsize=(10,5)) 
plt.plot(X_test['strain'].values[:50], label='Strain') 
plt.plot(X_test['vibration'].values[:50], label='Vibration') 
plt.plot(X_test['temperature'].values[:50], label='Temperature') 
plt.title("Sample Sensor Data - Structural Health Monitoring") 
plt.xlabel("Sample Index") 
plt.ylabel("Sensor Reading") 
plt.legend() 
plt.grid(True) 
plt.tight_layout() 
plt.show()
