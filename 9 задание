def seidel_method(A, b, initial_guess, tolerance=1e-10, max_iterations=1000):
    n = len(A)
    x = initial_guess[:]
    for _ in range(max_iterations):
        x_new = []
        for i in range(n):
            sum_ax = sum(A[i][j] * x[j] for j in range(n) if j != i)
            new_xi = (b[i] - sum_ax) / A[i][i]
            x_new.append(new_xi)
        if all(abs(x_new[i] - x[i]) < tolerance for i in range(n)):
            return x_new
        x = x_new
    raise ValueError("Seidel method did not converge")

A = [[1, 5, 1], [4, -1, 1], [12, 12, 72]]
b = [22, 46, 168]
initial_guess = [0, 0, 0]

solution = seidel_method(A, b, initial_guess)
print("Solution:", solution)
