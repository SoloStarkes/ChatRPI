import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms
from torch.utils.data import DataLoader

# Step 1: Define the Neural Network Architecture
class SimpleNN(nn.Module):
    def __init__(self):
        super(SimpleNN, self).__init__()
        self.flatten = nn.Flatten()
        self.fc1 = nn.Linear(28 * 28, 128)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(128, 10)  # 10 output classes for digits 0-9

    def forward(self, x):
        x = self.flatten(x)
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)
        return x

# Step 2: Load and Preprocess the Data
transform = transforms.Compose([transforms.ToTensor(), transforms.Normalize((0.5,), (0.5,))])

train_dataset = datasets.MNIST(root='./data', train=True, download=True, transform=transform)
test_dataset = datasets.MNIST(root='./data', train=False, download=True, transform=transform)

train_dataloader = DataLoader(train_dataset, batch_size=64, shuffle=True)
test_dataloader = DataLoader(test_dataset, batch_size=64, shuffle=False)

# Step 3: Initialize the Model, Loss Function, and Optimizer
model = SimpleNN()
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

# Step 4: Training Loop
num_epochs = 5

for epoch in range(num_epochs):
    model.train()

    for inputs, labels in train_dataloader:
        optimizer.zero_grad()
        outputs = model(inputs)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()

    print(f'Epoch {epoch + 1}/{num_epochs}, Loss: {loss.item()}')

# Step 5: Evaluation on Test Set
model.eval()
correct = 0
total = 0

with torch.no_grad():
    for inputs, labels in test_dataloader:
        outputs = model(inputs)
        _, predicted = torch.max(outputs.data, 1)
        total += labels.size(0)
        correct += (predicted == labels).sum().item()

accuracy = correct / total
print(f'Test Accuracy: {accuracy * 100}%')

"""
- Neural Network Architecture (Step 1): SimpleNN is a basic neural network with one hidden layer.

- Data Loading and Preprocessing (Step 2): We use the MNIST dataset and DataLoader for efficient batching.

- Model Initialization and Optimization (Step 3): Initialize the model, define the loss function (CrossEntropyLoss), and 
choose an optimizer (Adam).

- Training Loop (Step 4): Iterate through epochs, perform forward and backward passes, and update model parameters.

- Evaluation on Test Set (Step 5): Switch the model to evaluation mode, compute accuracy on the test set.

This example showcases the key steps in training a neural network for image classification using PyTorch. Adjustments to the 
model architecture, hyperparameters, and additional techniques (e.g., dropout, learning rate scheduling) can be made to improve 
performance further.
"""