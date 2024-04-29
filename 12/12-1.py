# Метод половинного деления

def F(x):
    return -3.456 + 5.76*x - 3.6*x**2 + x**3

a = float(input("Введите a: "))
b = float(input("Введите b: "))
eps = 0.001

while abs(b - a) > eps:
    x = (a + b) / 2
    if (F(x) == 0): break
    if (F(a) * F(x) > 0):
        a = x
    else:
        b = x

print('X = ', x)
print('F(X) = ', F(x))
