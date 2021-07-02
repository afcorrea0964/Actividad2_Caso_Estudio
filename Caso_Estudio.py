import numpy as np
n=100
a=0.5*np.ones([100])
b=2*np.ones([100])
d=np.ones([100])
b[0]=b[99]=1.5
c=a
def tridiag(n,d,a,c,b):
    x = np.zeros(n)
    for i in range(1,n-1):
        mult = a[i-1]/d[i-1]
        d[i]-= mult*c[i-1]
        b[i] -= mult * b[i-1]
        print(d)
        x[n-1]=b[n-1]/d[n-1]
        for i in range (n-2,-1,-1):
            x[i]=(b[i]-c[i]*x[i+1]/d[i])
        return x
print('Valores de la diagonal, matriz 100x100')
print(d)
print('Valores de la subdiagonal, matriz 100x100')
print(a)
print('Valores de la superdiagonal, matriz 100x100')
print(c)

print('Valores de los terminos independientes, matriz 100x100')
print(b)
print('Matriz resultante')
tridiag(n,d,a,c,b)