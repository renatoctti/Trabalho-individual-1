def karatsuba(x, y):
    # Caso base: se um dos números for menor que 10, usa multiplicação normal
    if x < 10 or y < 10:
        return x * y

    # Determina o tamanho dos números
    n = max(len(str(abs(x))), len(str(abs(y))))
    m = n // 2

    # Divide os números
    high_x, low_x = divmod(x, 10**m)
    high_y, low_y = divmod(y, 10**m)

    # Recursivamente calcula os produtos
    z0 = karatsuba(low_x, low_y)
    z1 = karatsuba((low_x + high_x), (low_y + high_y))
    z2 = karatsuba(high_x, high_y)

    # Combina os resultados
    return (z2 * 10**(2*m)) + ((z1 - z2 - z0) * 10**m) + z0

if __name__ == "__main__":
    test_cases = [
        (3, 4, "Caso com números pequenos"),
        (7, 8, "Caso com números pequenos"),
        (1234, 5678, "Caso com números grandes"),
        (98765, 43210, "Caso com números muito grandes"),
        (0, 1234, "Caso onde um dos números é zero"),
        (999, 0, "Caso onde um dos números é zero"),
        (-3, 4, "Caso onde um número é negativo"),
        (-5, -6, "Caso onde ambos os números são negativos")
    ]

    for x, y, description in test_cases:
        result = karatsuba(x, y)
        print(f"{description}: karatsuba({x}, {y}) = {result}")
