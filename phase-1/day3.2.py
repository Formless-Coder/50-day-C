import numpy as np

#dataset: 5 samples, 2 features
X = np.array([
    [2,4],
    [3,6],
    [4,8],
    [5,10],
    [6,12]
], dtype=float)

#1> centre the data
X_centered = X - X.mean(axis=0)

#2> covariance matrix
cov = np.cov(X_centered, rowvar = False)

#3> eigen decomposition
values, vectors = np.linalg.eigh(cov)

#4> sort by descending eigenvalue
idx = np.argsort(values)[::1]
values = values[idx]
vectors = vectors[:,idx]

#5> select first principal component
W = vectors[:,idx]

#6> project data into one dimension
X_reduced = X_centered @ W

print("eigenvalues:", values)
print("pricipal components:\n", W)
print("reduced data:\n", X_reduced)

#explained variance ratio
print("explained variance ratio:",
     values[0]/ values.sum())
