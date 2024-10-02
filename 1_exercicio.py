def fibonacci_check(n: int) -> str:
    a, b = 0, 1
    fibonacci_numbers = {a, b}  # Usando um conjunto para armazenar os números de Fibonacci

    while b <= n:
        a, b = b, a + b
        fibonacci_numbers.add(b)

    if n in fibonacci_numbers:
        return f"O número {n} pertence a sequência de Fibonacci."
    else:
        return f"O número {n} não pertence a sequência de Fibonacci."

numero = 5
resultado = fibonacci_check(numero)
print(resultado)