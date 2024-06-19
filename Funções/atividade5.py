def soma (a, b):
    return a + b

try:
    numero1 = float(input('Digite um número: '))
    numero2 = float(input('Digite outro número: '))

    resultado = soma(numero1, numero2)
    print(f'O resultado da soma de {numero1} mais {numero2} é {resultado}.')
    
    if resultado == 0:
        print('A soma tem resultado nulo.')
    elif resultado > 0:
        print('A soma tem resultado positivo')
    else:
        print('A soma é negativa.')

except ValueError:
    print('Digite dois números válidos.')