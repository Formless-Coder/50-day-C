import numpy as np

#create matrices
a = np.array([[1,2], 
              [3,4]])

b = np.array([[5,6],
              [7,8]])

#matrix multiplication
print("addition:", a+b)
print("scalar multiplication:", 3*a)
print("transpose:", a.T)

#identity matrix
i = np.eye(2)
print("identity:\n", a@i)

#inverse
print("inverse:\n", np.linalg.inv(a))

#linear transformations
x = np.array([1,2])
s = np.array([[2,0], [0,3]])

print("transformed vector:", s@x)

#composition of transformations
r = np.array([[0,-1], [1,0]])

shear = np.array([[1,1], [0,1]])

print("rotation then shear:\n", shear@r)
print("shear then rotation:\n", r@shear)

#verifyno commutativity
print("are they equal?",
              np.array_equal(shear@r, r@shear))

#matrix dimensions
print("shape of a:", a.shape)
print("shape of b:", b.shape)