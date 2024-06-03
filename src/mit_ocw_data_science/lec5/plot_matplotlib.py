import unittest
import matplotlib.pyplot as plt
import numpy as np
import unittest
import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    unittest.main()

x_vals = [1, 2, 3, 4]
y_vals_1 = [1, 2, 3, 4]
plt.plot(x_vals, y_vals_1, 'b-', label='first')
y_vals_2 = [1, 7, 3, 5]
plt.plot(x_vals, y_vals_2, 'r--', label='second')
plt.legend()
plt.show()
