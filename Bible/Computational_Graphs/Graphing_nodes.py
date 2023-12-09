import torch
import torch.nn as nn
import torch.optim as optim

# Define a simple neural network
class SimpleNet(nn.Module):
    def __init__(self):
        super(SimpleNet, self).__init__()
        self.fc1 = nn.Linear(2, 3)  # Fully connected layer with 2 input features and 3 output features
        self.fc2 = nn.Linear(3, 1)  # Fully connected layer with 3 input features and 1 output feature

    def forward(self, x):
        x = self.fc1(x)
        x = torch.relu(x)  # ReLU activation function
        x = self.fc2(x)
        return x

# Create an instance of the neural network
model = SimpleNet()

# Define input data (batch size: 2, input features: 2)
input_data = torch.tensor([[1.0, 2.0], [3.0, 4.0]], requires_grad=True)

# Forward pass through the network
output = model(input_data)

# Print the computational graph
print("Computational Graph:")
print(model)

# Backward pass to compute gradients
output.backward()

# Print gradients for each parameter in the model
print("\nGradients:")
for name, param in model.named_parameters():
    if param.grad is not None:
        print(f"{name}: {param.grad}")

"""
1. We define a simple neural network (SimpleNet) with two fully connected layers.

2. We create an instance of the network (model).

3. We define input data (input_data) with requires_grad set to True to track gradients during the backward pass.

4. We perform a forward pass through the network by passing the input data to the model.

5. We print the computational graph using print(model).

6. We perform a backward pass to compute gradients with respect to the input data.

7. We print the gradients for each parameter in the model.


This example demonstrates the creation of nodes in a computational graph as part of the forward and backward passes in a 
simple neural network.
"""