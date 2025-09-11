import numpy as np

T = np.array([[90, -30, 0], [-30, 120, -30], [0, -30, 90]])

# Calculating the invariants
I = np.trace(T)
II = 0.5 * (I**2 - np.trace(np.dot(T, T)))
III = np.linalg.det(T)

print("I={}".format(I))
print("II={}".format(II))
print("III={}".format(III))
