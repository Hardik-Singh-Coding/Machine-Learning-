import numpy as np 
from sklearn.linear_model import LinearRegression as LR
import matplotlib.pyplot as plt

# House size (sq ft)
X = np.array([[1000], [1500], [2000], [2500]]) # 2D array

# Prices (in Lakhs)
y = np.array([50, 70, 90, 110])

# Training model
model = LR()
model.fit(X,y) # fit tells the model to learn the relationship or pattern between X (input) and y (output)

# Predicting price
predicted_price = model.predict([[1800]])
print(f"The predicted price for 1800 sq ft: Rs {predicted_price[0]:.2f} Lakhs")

# Visualization
plt.scatter(X, y, color='black', label='Actual Prices')
plt.plot(X, model.predict(X), color='red', label='Regression Line')
plt.xlabel("House Size (sq ft)")
plt.ylabel("Price (Lakhs)")
plt.title("House price prediction")
plt.legend()
plt.grid(True)
plt.show()