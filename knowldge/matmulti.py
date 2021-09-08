import numpy as np

a=np.array([[1,2,3],[3,4,5],[6,7,8],[3,1,5]])
print(a)
b=np.array([[1,2,3],[3,4,5],[6,7,8]])
print(b)
result=np.array([[0,0,0],[0,0,0],[0,0,0],[0,0,0]])
result=np.dot(a,b)
print(result)

