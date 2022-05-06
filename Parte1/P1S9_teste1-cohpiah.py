
as_a = [1, -2, 3, -4]
as_b = [-2, 5, 1, 3]

soma = 0
for i in as_a:
    soma = soma + (as_a[i] - as_b[i])

similar = abs(soma) / 6

print(similar)