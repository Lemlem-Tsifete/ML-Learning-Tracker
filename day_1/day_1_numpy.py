import numpy as np

A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

A_transposed = np.transpose(A)

print("This is the transposed for ", A_transposed)

A_determinat = np.linalg.det(A)

print("This is determinat of ", A_determinat)

# Inverse (will error if determinant = 0)
try:
    A_inv = np.linalg.inv(A)
    print("\nInverse of A:")
    print(A_inv)
except np.linalg.LinAlgError:
    print("\nMatrix A is singular (no inverse).")

arr = np.array([10, 20, 30, 40, 50])

# Mean
mean_val = np.mean(arr)
print("\nMean:", mean_val)

# Median
median_val = np.median(arr)
print("Median:", median_val)

# Standard Deviation
std_val = np.std(arr)
print("Standard Deviation:", std_val)

#check using numpay dot product for the manualy dot product
import numpy as np

v1 = [1, 2, 3]
v2 = [4, 5, 6]

np_result = np.dot(v1, v2)
print("Numpy Dot Product", np_result)