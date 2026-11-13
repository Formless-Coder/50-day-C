import numpy as np

#create a scalar
a = np.array([2,3])
b = np.array([4,5])

#vector addition
print("addition:", a+b)

#scalar multiplication
print("scalar multiplication:", 3*a)

#dot product
print("dot product:", np.dot(a,b))

#create matrices
m1 = np.array([
    [1,2],
    [3,4]
])

m2 = np.array([
    [5,6],
    [7,8]
])

#matrix multiplication
print("matrix multiplication:\n", m1 @ m2)

#create a 3d tensor
tensor = np.array([
    [[1,2], [3,4]],
    [[5,6], [7,8]]
])

#check shapes
print("vector shape:", a.shape)
print("matrix shape:", m1.shape)
print("tensor shape:", tensor.shape)

#simple neural network layer
X = np.array([[5,80,70]])

W = np.array([
    [0.2,0.4],
    [0.3,0.1],
    [0.5,0.2]
])

bias = np.array([1,2])

Z = X @ W + bias

print("neural network output:", Z)