import numpy
import math
import matplotlib.pyplot as plt
k = 5
m = 3
A = 1
tmax = 10
t = 0.1 
x,j = [],[]

i=t
w = math.sqrt(k/m)
while i < tmax :
    x.append(A*math.cos(w*i))
    j.append(i)
    i+=t

plt.plot(j,x)
plt.show()