import joblib
import numpy as np
import os

# Get project root directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Model path
model_path = os.path.join(BASE_DIR, "models", "house_price_model.pkl")

# Load trained model
model = joblib.load(model_path)

print("Enter house details")

bedrooms = float(input("Bedrooms: "))
bathrooms = float(input("Bathrooms: "))
sqft_living = float(input("Living area sqft: "))
sqft_lot = float(input("Lot size sqft: "))
floors = float(input("Floors: "))
condition = float(input("Condition (1-5): "))
sqft_above = float(input("Sqft above: "))
sqft_basement = float(input("Sqft basement: "))
yr_built = float(input("Year built: "))

features = np.array([[bedrooms, bathrooms, sqft_living,
                      sqft_lot, floors, condition,
                      sqft_above, sqft_basement, yr_built]])

predicted_price = model.predict(features)

print("🏠 Predicted House Price:", predicted_price[0])