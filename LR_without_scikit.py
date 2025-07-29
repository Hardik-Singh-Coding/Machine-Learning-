import numpy as np
import matplotlib.pyplot as plt

X = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
y_old = np.array([2, 4, 6, 8, 10, 12, 14, 16, 18, 20])

x_mean = np.mean(X)
y_mean = np.mean(y_old)

B1_num = np.sum((X - x_mean) * (y_old - y_mean))
B1_den = np.sum((X - x_mean)** 2)
B1 = B1_num/B1_den
print(f"B1 = {int(B1)}")
Bo = y_mean - B1*x_mean
print(f"Bo = {int(Bo)}")

y_new = Bo + B1*X
print(f"y_old = {y_old.astype(int)}")
print(f"y_new = {y_new.astype(int)}")

plt.scatter(y_old, y_new, color='black', label='y_new vs y_old')
plt.plot(X, y_old, color='red', label='Original y_old vs X')
plt.xlabel("y_old")
plt.ylabel("y_new")
plt.title("y_old v/s y_new")
plt.legend()
plt.grid(True)
plt.show()