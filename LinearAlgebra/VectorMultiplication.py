"""
Two vectors can me multiplied  with either using their dot or cartesian product but mainly we will be using dot product
multiply our vectors

Dot prodiuct of vectors totally depends on size and dimension of vectors but one thing that has to be remember os product
is only possible in the case of Vector 1 being of M x N  and vector 2 being N x p and result vector will be M x P
"""
import numpy as np

Vector_1 = np.array([1, 2])
Vector_2 = np.array([3, 4])

print("Dot Product of Vector_1 and Vector_2 is {}".format(Vector_1.dot(Vector_2)))
