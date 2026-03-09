import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import joblib

# Get project root directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Correct dataset path
data_path = os.path.join(BASE_DIR, "data", "data.csv")

# Load dataset
data = pd.read_csv(data_path)

# Select features
X = data[['bedrooms','bathrooms','sqft_living','sqft_lot',
          'floors','condition','sqft_above','sqft_basement','yr_built']]

# Target
y = data['price']

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Save model
model_path = os.path.join(BASE_DIR, "models", "house_price_model.pkl")
joblib.dump(model, model_path)

print("✅ Model trained successfully!")
print("✅ Model saved at:", model_path)