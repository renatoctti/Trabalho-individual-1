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

class TestKaratsuba(unittest.TestCase):
    def test_small_numbers(self):
        """Caso com números pequenos: 3 * 4 = 12 e 7 * 8 = 56"""
        self.assertEqual(karatsuba(3, 4), 12)
        self.assertEqual(karatsuba(7, 8), 56)
    
    def test_large_numbers(self):
        """Caso com números grandes: 1234 * 5678 = 7006652 e 98765 * 43210 = 4267635650"""
        self.assertEqual(karatsuba(1234, 5678), 7006652)
        self.assertEqual(karatsuba(98765, 43210), 4267635650)
    
    def test_zero_cases(self):
        """Casos onde um dos números é zero: 0 * 1234 = 0 e 999 * 0 = 0"""
        self.assertEqual(karatsuba(0, 1234), 0)
        self.assertEqual(karatsuba(999, 0), 0)
    
    def test_negative_cases(self):
        """Casos com números negativos: -3 * 4 = -12 e -5 * -6 = 30"""
        self.assertEqual(karatsuba(-3, 4), -12)
        self.assertEqual(karatsuba(-5, -6), 30)

if __name__ == "__main__":
    print("Escolha uma opção:")
    print("1 - Rodar apenas os testes")
    print("2 - Inserir números manualmente e mostrar o resultado")
    print("3 - Fazer ambos")
    opcao = input("Digite a opção desejada: ")

    if opcao == "1":
        unittest.main(argv=[''], exit=False)
    elif opcao == "2":
        x = int(input("Digite o primeiro número: "))
        y = int(input("Digite o segundo número: "))
        resultado = karatsuba(x, y)
        print(f"Resultado: {x} * {y} = {resultado}")
    elif opcao == "3":
        unittest.main(argv=[''], exit=False)
        x = int(input("Digite o primeiro número: "))
        y = int(input("Digite o segundo número: "))
        resultado = karatsuba(x, y)
        print(f"Resultado: {x} * {y} = {resultado}")
    else:
        print("Opção inválida.")
