# import numpy as np
from mlp.data import X, y
from mlp.model import MLP
from mlp.utils import derivative_sigmoid, sigmoid

# Initialize a MLP model
mlp = MLP(d_in=2, d_h=3, d_out=2)

# Train the MLP model
for epoch in range(10000):
    loss, y_pred, h = mlp.forward(X, y)
    mlp.backward(X, y, y_pred, h, learning_rate=0.1)

    if epoch % 100 == 0:
        print("epoch: {0}, loss: {1}".format(epoch, loss))
