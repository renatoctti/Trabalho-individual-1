import unittest


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

# Testes automatizados


class TestKaratsuba(unittest.TestCase):
    def test_small_numbers(self):
        self.assertEqual(karatsuba(3, 4), 12)
        self.assertEqual(karatsuba(7, 8), 56)

    def test_large_numbers(self):
        self.assertEqual(karatsuba(1234, 5678), 1234 * 5678)
        self.assertEqual(karatsuba(98765, 43210), 98765 * 43210)

    def test_edge_cases(self):
        self.assertEqual(karatsuba(0, 1234), 0)
        self.assertEqual(karatsuba(999, 0), 0)
        self.assertEqual(karatsuba(-3, 4), -12)
        self.assertEqual(karatsuba(-5, -6), 30)


if __name__ == "__main__":
    try:
        x = int(input("Digite o valor de x: "))
        y = int(input("Digite o valor de y: "))
        print(
            f"Resultado da multiplicação de {x} e {y} usando Karatsuba: {karatsuba(x, y)}")
    except ValueError:
        print("Por favor, insira apenas números inteiros.")
