# Метод Ньютона

def F(x):
    return -3.456 + 5.76*x - 3.6*x**2 + x**3

def F1(x):
    return  5.76 - 6.2*x + 3*x**2

x1 = float(input("Введите X0: "))
eps = 0.001
x0 = x1 + 2*eps

while abs(x1 - x0) > eps:
    x0 = x1
    x1 = x0 - F(x0) / F1(x0)

print('X = ', x1)
print('F(X) = ', F(x1))
