import numpy
import math
import matplotlib.pyplot as plt

print('K : ', end='')
k = float(input())
print('M : ', end='')
m = float(input())
print('deltaT : ', end='')
dt = float(input())
print('tmax : ', end='')
tmax = float(input())

v0 = 0
t0 = 0
x0 = 0
i = 0
a,x,v,t = [],[],[],[]

x.append(1)
x.append(1)
v.append(v0)
v.append(v0)
t.append(t0)
t.append(t0)
a.append(0)
a.append(0)

j = 1
while i < tmax :
    a.append((-1*k/m) *x[j])
    v.append(v[j] + a[j+1] * dt)
    x.append(x[j] + v[j+1] * dt)
    t.append(i)
    i+=dt
    j+=1
    
plt.plot(t,x)
plt.show()