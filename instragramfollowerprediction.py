from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression
import numpy as np

# Sample data: X represents features (e.g., post frequency), y represents followers
X = np.array([[1], [2], [3], [4], [5]])  # Example features
y = np.array([1000, 1500, 2000, 2500, 3000])  # Example followers

# Transform features using polynomial features
degree = 2  # Degree of polynomial
poly_features = PolynomialFeatures(degree=degree)
X_poly = poly_features.fit_transform(X)

# Train polynomial regression model
model = make_pipeline(PolynomialFeatures(degree), LinearRegression())
model.fit(X, y)

# Predict followers for future dates
future_dates = np.array([[6], [7], [8]])  # Example future dates
future_followers = model.predict(future_dates)
print("Predicted followers for future dates:", future_followers)