import torch

# Define the toy neural network class
class ToyNeuralNetwork:
    def __init__(self):
        # Initialize learnable parameters with random values
        self.w1 = torch.randn(1, requires_grad=True)
        self.w2 = torch.randn(1, requires_grad=True)
        self.w3 = torch.randn(1, requires_grad=True)
        self.w4 = torch.randn(1, requires_grad=True)

    def forward(self, a):
        # Forward pass
        b = self.w1 * a
        c = self.w2 * a
        d = self.w3 * b + self.w4 * c
        L = 10 - d
        return L

# Instantiate the toy neural network
toy_network = ToyNeuralNetwork()

# Input tensor 'a'
a = torch.tensor([2.0], requires_grad=True)

# Forward pass
L = toy_network.forward(a)

# Backward pass
L.backward()

# Display the gradients
print("Gradients:")
print("w1:", toy_network.w1.grad.item())
print("w2:", toy_network.w2.grad.item())
print("w3:", toy_network.w3.grad.item())
print("w4:", toy_network.w4.grad.item())

# Update the learnable parameters using a simple gradient descent update rule
learning_rate = 0.01
toy_network.w1.data -= learning_rate * toy_network.w1.grad
toy_network.w2.data -= learning_rate * toy_network.w2.grad
toy_network.w3.data -= learning_rate * toy_network.w3.grad
toy_network.w4.data -= learning_rate * toy_network.w4.grad

# Zero out the gradients for the next iteration
toy_network.w1.grad.zero_()
toy_network.w2.grad.zero_()
toy_network.w3.grad.zero_()
toy_network.w4.grad.zero_()

# Display the updated parameters
print("\nUpdated Parameters:")
print("w1:", toy_network.w1.item())
print("w2:", toy_network.w2.item())
print("w3:", toy_network.w3.item())
print("w4:", toy_network.w4.item())