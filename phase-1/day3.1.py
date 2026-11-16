import numpy as np

#example matrix
a = np.array([
    [3,0],
    [0,2]
])

#calculate eigenvalues and eigenvectors 
eigenvalues, eigenvectors = np.linalg.eig(a)

print("eigenvalues:\n", eigenvalues)
print("eigenvectors:\n", eigenvectors)

#verify av = lambda * v
for i in range(len(eigenvalues)):
    v = eigenvectors[:,1]
    lam = eigenvalues[i]

    print("\nverification:")
    print("av =", a @ v)
    print("lambda * v =", lam * v)