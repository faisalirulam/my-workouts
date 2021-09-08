import numpy as np
a=np.mat("2 3; 5 7")
print("a:\n",a)
print("eigen values:",np.linalg.eigvals(a))

eigenvalue,eigenvector =np.linalg.eig(a)
print("first tuple of eig:",eigenvalue)
print("second tuple of eig:",eigenvector)
