# Import required libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
import tensorflow as tf
import torch
import requests
from bs4 import BeautifulSoup
from flask import Flask

# NumPy Example
def numpy_example():
    print("NumPy Example:")
    array = np.array([1, 2, 3, 4, 5])
    print("Array:", array)
    print("Mean:", array.mean())
    print()

# Pandas Example
def pandas_example():
    print("Pandas Example:")
    data = {'Name': ['John', 'Anna'], 'Age': [28, 24]}
    df = pd.DataFrame(data)
    print(df.head())
    print()

# Matplotlib Example
def matplotlib_example():
    print("Matplotlib Example:")
    plt.plot([1, 2, 3, 4], [10, 20, 25, 30])
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Simple Line Plot')
    plt.show()

# Seaborn Example
def seaborn_example():
    print("Seaborn Example:")
    tips = sns.load_dataset('tips')
    sns.scatterplot(x='total_bill', y='tip', data=tips)
    plt.show()

# Scikit-learn Example
def sklearn_example():
    print("Scikit-learn Example:")
    X = np.array([[1], [2], [3], [4]])
    y = np.array([2, 3, 5, 7])
    model = LinearRegression().fit(X, y)
    print("Prediction for 5:", model.predict([[5]]))
    print()

# TensorFlow Example
def tensorflow_example():
    print("TensorFlow Example:")
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(10, activation='relu'),
        tf.keras.layers.Dense(1)
    ])
    model.compile(optimizer='adam', loss='mean_squared_error')
    print("TensorFlow model summary:")
    model.summary()
    print()

# PyTorch Example
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

# Requests Example
def requests_example():
    print("Requests Example:")
    response = requests.get('https://api.github.com')
    print("Response from GitHub API:", response.json())
    print()

# BeautifulSoup Example
def beautifulsoup_example():
    print("BeautifulSoup Example:")
    response = requests.get('https://www.example.com')
    soup = BeautifulSoup(response.text, 'html.parser')
    print("Title of the page:", soup.title.text)
    print()

# Flask Example
def flask_example():
    print("Flask Example:")
    app = Flask(__name__)

    @app.route('/')
    def home():
        return 'Hello, Flask!'

    app.run(debug=True)

# Main Function to Execute All Examples
def main():
    numpy_example()
    pandas_example()
    matplotlib_example()
    seaborn_example()
    sklearn_example()
    tensorflow_example()
    pytorch_example()
    requests_example()
    beautifulsoup_example()
    # Uncomment the next line to run the Flask example. Note: Flask server will run and block further execution.
    # flask_example()

if __name__ == '__main__':
    main()
