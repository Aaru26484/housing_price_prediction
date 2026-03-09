# 🏠 House Price Prediction using Machine Learning

## 📌 Project Overview

This project predicts house prices using a **Machine Learning Linear Regression model**.
The model learns relationships between house features such as **bedrooms, bathrooms, living area, and year built** to estimate the price of a house.

---

## 📊 Machine Learning Model

We use the **Linear Regression model**, which predicts a value using the equation:

[
y = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + \beta_3 x_3 + \dots + \beta_n x_n
]

Where:

* (y) = Predicted house price
* (\beta_0) = Intercept
* (\beta_1, \beta_2, ..., \beta_n) = Model coefficients
* (x_1, x_2, ..., x_n) = Input features

In this project:

[
Price = \beta_0 + \beta_1(Bedrooms) + \beta_2(Bathrooms) + \beta_3(Sqft_Living) + \beta_4(YearBuilt)
]

---

## 📂 Project Structure

```
house-price-prediction
│
├── data
│   └── data.csv
│
├── models
│   └── house_price_model.pkl
│
├── src
│   ├── train_model.py
│   ├── predict_price.py
│   └── app.py
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Joblib
* Streamlit (GUI)

---

## 📈 Model Training

The dataset is split into **training and testing sets**:

[
Train = 80%
]

[
Test = 20%
]

The model is trained using:

```
python src/train_model.py
```

---

## 🔮 Prediction

To predict a house price using the trained model:

```
python src/predict_price.py
```

Example input:

* Bedrooms = 3
* Bathrooms = 2
* Living Area = 2000 sqft
* Year Built = 2005

Output:

[
Predicted\ Price \approx $540000
]

---

## 🖥 GUI Application

The project includes a **Streamlit-based GUI**.

Run the interface:

```
streamlit run src/app.py
```

The GUI allows users to:

* Enter house features
* Click **Predict Price**
* View the predicted house price

---

## 🚀 Future Improvements

* Use **Random Forest / XGBoost** for better accuracy
* Add **data visualization dashboards**
* Deploy the model using **Docker or Cloud services**

---

## 📚 Conclusion

This project demonstrates how **Machine Learning can be applied to real estate price prediction** by learning patterns from housing datasets and estimating future prices.
