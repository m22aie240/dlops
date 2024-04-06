import numpy as np
import matplotlib.pyplot as plt


# Data points
random_values = [-3.5, -1.2, 0, 2.8, -4.1, 1.5, -0.7, 3.2, -2.4, 4.6]

# Defining the activation functions
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

#def relu(x):
#    return np.maximum(0, x)

#def leaky_relu(x, alpha=0.01):
#    return np.where(x > 0, x, x * alpha)

#def tanh(x):
#    return np.tanh(x)

# Generating values for plotting
x = np.linspace(-10, 10, 100)

# Apply sigmoid function to each data point
sigmoid_results = list(map(sigmoid, random_values))

# Print the results
print("Sigmoid results:")
for value, result in zip(random_values, sigmoid_results):
    print(f"Sigmoid({value}) = {result}")

# Plotting
#plt.figure(figsize=(14, 8))

# Sigmoid
#plt.subplot(2, 2, 1)
#plt.plot(x, sigmoid(x), label="Sigmoid")
#plt.title("Sigmoid Activation Function")
#plt.grid(True)

# ReLU
#plt.subplot(2, 2, 2)
#plt.plot(x, relu(x), label="ReLU")
#plt.title("ReLU Activation Function")
#plt.grid(True)

# Leaky ReLU
#plt.subplot(2, 2, 3)
#plt.plot(x, leaky_relu(x), label="Leaky ReLU")
#plt.title("Leaky ReLU Activation Function")
#plt.grid(True)

# Tanh
#plt.subplot(2, 2, 4)
#plt.plot(x, tanh(x), label="Tanh")
#plt.title("Tanh Activation Function")
#plt.grid(True)

# Display all plots
#plt.tight_layout()
#plt.show()

