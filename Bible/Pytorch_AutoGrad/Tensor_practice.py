import torch

# Creating Tensors
tensor_a = torch.tensor([1, 2, 3])
tensor_b = torch.ones((3, 3), dtype=torch.float32)
tensor_c = torch.randn((2, 2))  # Randomly initialized tensor

# Printing Tensors
print("Tensor A:")
print(tensor_a)

print("\nTensor B:")
print(tensor_b)

print("\nTensor C:")
print(tensor_c)

# Tensor Operations
result_sum = tensor_a + tensor_b
result_product = torch.mm(tensor_b, tensor_c)

# Printing Results
print("\nResult of Sum (A + B):")
print(result_sum)

print("\nResult of Matrix Product (B * C):")
print(result_product)

"""
Creation of Tensors:

tensor_a is created from a Python list.
tensor_b is initialized as a 3x3 matrix of ones.
tensor_c is initialized as a 2x2 matrix with random values.
Printing Tensors:

Displaying the content of each tensor to observe their values.
Tensor Operations:

Performing element-wise addition of tensor_a and tensor_b.
Calculating the matrix product of tensor_b and tensor_c.
Printing Results:

Displaying the results of the tensor operations.
This program is a basic illustration of working with PyTorch tensors. You can experiment with different tensor operations, 
change the shapes of tensors, and explore more advanced features as you become more familiar with PyTorch.
"""