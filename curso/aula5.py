"""

    Exercicio aula 5
    criar variaveis para nome,idade, altura, peso, e variavel para ano atua



"""

# VARIAVEIS

nome = 'Erasmo'
altura = 1.65
peso = 85.5
ano_atual = 2022
idade = input('Qual sua idade ? ' )
nascimento = ano_atual - int(idade)
imc = peso / altura ** 2


print(f'{nome} nasceu em {nascimento} tem {idade}')
print(f'{nome} pesa {peso} seu IMC é {imc:.2f}')