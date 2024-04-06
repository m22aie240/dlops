import numpy as np
import matplotlib.pyplot as plt

# Defining the activation functions
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

<<<<<<< HEAD
#def relu(x):
#    return np.maximum(0, x)

#def leaky_relu(x, alpha=0.01):
#    return np.where(x > 0, x, x * alpha)

#def tanh(x):
#    return np.tanh(x)
=======
def relu(x):
    return np.maximum(0, x)

def leaky_relu(x, alpha=0.01):
    return np.where(x > 0, x, x * alpha)

def tanh(x):
    return np.tanh(x)
>>>>>>> feature-2

# Generating values for plotting
x = np.linspace(-10, 10, 100)

# Plotting
plt.figure(figsize=(14, 8))

# Sigmoid
plt.subplot(2, 2, 1)
plt.plot(x, sigmoid(x), label="Sigmoid")
plt.title("Sigmoid Activation Function")
plt.grid(True)

# ReLU
<<<<<<< HEAD
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
=======
plt.subplot(2, 2, 2)
plt.plot(x, relu(x), label="ReLU")
plt.title("ReLU Activation Function")
plt.grid(True)

# Leaky ReLU
plt.subplot(2, 2, 3)
plt.plot(x, leaky_relu(x), label="Leaky ReLU")
plt.title("Leaky ReLU Activation Function")
plt.grid(True)

# Tanh
plt.subplot(2, 2, 4)
plt.plot(x, tanh(x), label="Tanh")
plt.title("Tanh Activation Function")
plt.grid(True)
>>>>>>> feature-2

# Display all plots
plt.tight_layout()
plt.show()

