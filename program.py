# import seaborn as sns
# import matplotlib.pyplot as plt

# # Create a scatter plot
# sns.scatterplot(x='total_bill', y='tip', data=sns.load_dataset('tips'))
# plt.show()

# from sklearn.linear_model import LinearRegression
# import numpy as np

# # Create a simple linear regression model
# X = np.array([[1], [2], [3], [4]])
# y = np.array([2, 3, 5, 7])

# model = LinearRegression().fit(X, y)
# print(model.predict([[7]]))  # Predict for a new value

# import tensorflow as tf

# # Create a simple neural network model
# model = tf.keras.Sequential([
#     tf.keras.layers.Dense(10, activation='relu'),
#     tf.keras.layers.Dense(1)
# ])
# model.compile(optimizer='adam', loss='mean_squared_error')

import torch
def pytorch_example():
    print("PyTorch Example:")
    class SimpleNN(torch.nn.Module):
        def __init__(self):
            super(SimpleNN, self).__init__()
            self.fc = torch.nn.Linear(10, 1)

        def forward(self, x):
            return self.fc(x)

    model = SimpleNN()
    print("PyTorch model:", model)
    print()
