import matplotlib.pyplot as plt

x_vals_1 = [1, 2, 3, 4, 5]
y_vals_1 = [1, 4, 9, 16, 25]
plt.plot(x_vals_1, y_vals_1, 'r--', label='x^2')
y_vals_2 = [1, 8, 27, 64, 125]
plt.plot(x_vals_1, y_vals_2, 'bs-', label='x^3')
plt.legend()
plt.show()
