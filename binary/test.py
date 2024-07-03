"""
Agora é a sua vez! Escreva uma função que converta binários (string) para um número inteiro, e números inteiros para binários (string). 
Para saber mais acesse a documentação https://docs.python.org/3/

Outras fontes: https://www.w3schools.com/python/python_ref_string.asp  https://www.w3schools.com/python/ref_func_bin.asp
"""

def binary_to_decimal(bin): 
    """
    Converte um número binário (representado como string) em um número inteiro.

    Parâmetros:
    bin (str): O número binário como string.

    Retorna:
    int: O número binário convertido para decimal.
    """
    ...

def decimal_to_binary(dec):
    """
    Converte um número decimal (inteiro) em uma string que representa seu equivalente binário.

    Parâmetros:
    dec (int): O número decimal.

    Retorna:
    str: A representação binária do número decimal.
    """
    ...

def main():
    """
    Função principal para testar as funções de conversão.
    """
    assert binary_to_decimal("1010") == 10
    assert binary_to_decimal("1111") == 15
    assert decimal_to_binary(10) == "1010"
    assert decimal_to_binary(15) == "1111"
    print("All tests passed!")

main()