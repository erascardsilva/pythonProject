"""

    Exercicio  python verificando par ou impar

"""

numero_inteiro = input('Digite um numero inteiro : ')

if numero_inteiro.isdigit():
    numero_inteiro = int(numero_inteiro)
    par_ou_impar = numero_inteiro % 2

else:
    print('Voce não digitou um numero inteiro tente 0 - 9 por exemplo')
    print('saindo')
    exit()

if par_ou_impar == 0:
    print(f'O número {numero_inteiro}')
    print("O numero digitado é par")
else:
    print(f'O número {numero_inteiro}')
    print("O numero digitado é impar")
