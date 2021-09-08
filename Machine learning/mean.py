import numpy
data=[20,10,33,44,56,78,98,88,67,67]
mean=numpy.mean(data)
print("Mean = ",mean)
median=numpy.median(data)
print("Median = ",median)

from scipy import stats
mode=stats.mode(data)
print("Mode = ",mode)

sd=numpy.std(data)
print("Standard deviation =",sd)
variance=numpy.var(data)
print(variance)

import math
sd1=math.sqrt(variance)    #std is the sqrt of variance
print("Std deviation =",sd1)

sum=0
for i in range(len(data)):
    sum=sum+data[i]
    i=i+1
mean1=sum/len(data)
print("Mean1 =",mean1)
