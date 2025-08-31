import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

# Load the dataset
data = pd.read_csv('diabetes.csv')  # make sure this file exists in the same folder

# Features and target
X = data.drop('Outcome', axis=1)
y = data['Outcome']

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save the model
with open('diabetes-prediction-rfc-model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("✅ Model saved as diabetes-prediction-rfc-model.pkl")
