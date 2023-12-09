import torch
import torch.nn as nn
import torch.optim as optim
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split

# Create a synthetic dataset
X, y = make_classification(n_samples=1000, n_features=20, n_informative=10, n_clusters_per_class=2, random_state=42)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Convert the data to PyTorch tensors
X_train_tensor = torch.FloatTensor(X_train)
y_train_tensor = torch.FloatTensor(y_train)
X_test_tensor = torch.FloatTensor(X_test)
y_test_tensor = torch.FloatTensor(y_test)

# Define a simple neural network
class SimpleNN(nn.Module):
    def __init__(self):
        super(SimpleNN, self).__init__()
        self.fc1 = nn.Linear(20, 10)  # Input features: 20, Output features: 10
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(10, 1)   # Input features: 10, Output features: 1 (binary classification)

    def forward(self, x):
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)
        return torch.sigmoid(x)

# Instantiate the neural network, loss function, and optimizer
model = SimpleNN()
criterion = nn.BCELoss()  # Binary Cross Entropy Loss
optimizer = optim.SGD(model.parameters(), lr=0.01)

# Training loop
num_epochs = 100
train_losses = []

for epoch in range(num_epochs):
    # Forward pass
    outputs = model(X_train_tensor)
    loss = criterion(outputs.squeeze(), y_train_tensor)

    # Backward pass and optimization
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    train_losses.append(loss.item())

    if (epoch + 1) % 10 == 0:
        print(f'Epoch [{epoch+1}/{num_epochs}], Loss: {loss.item():.4f}')

# Plot the training loss curve
plt.plot(train_losses, label='Training Loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.legend()
plt.show()

# Evaluate the model on the test set
with torch.no_grad():
    model.eval()
    y_pred = model(X_test_tensor).squeeze().numpy()

# Convert predicted probabilities to binary predictions
y_pred_binary = (y_pred > 0.5).astype(int)

# Evaluate accuracy
accuracy = (y_pred_binary == y_test).mean()
print(f'Test Accuracy: {accuracy * 100:.2f}%')



"""
Dataset Preparation:

A synthetic dataset is created using make_classification from scikit-learn.
Neural Network Definition:

A simple neural network (SimpleNN) with one hidden layer is defined using PyTorch's nn.Module.
Training Loop:

The model is trained using a simple training loop.
Binary Cross Entropy Loss is used as the loss function.
Stochastic Gradient Descent (SGD) is used as the optimizer.
Plotting Training Loss Curve:

The training loss is plotted over epochs to visualize the learning progress.
Model Evaluation:

The trained model is evaluated on the test set.
Accuracy is computed for model performance evaluation.
This example demonstrates the fundamental steps of training a neural network using PyTorch, including defining the model, 
specifying the loss function and optimizer, conducting the training loop, and evaluating the model.
"""