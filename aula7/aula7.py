nome = 'Lucas'
idade = 23
anoAtual = 2021
peso = 90
altura = 1.85
anoNasc = anoAtual - idade
imc = peso / altura**2
print('{} tem {} anos, {} de altura e pesa {}Kg'.format(nome, idade, altura, peso))
print('O IMC de {} é {:.2f}'.format(nome, imc))
print('{} nasceu em {}'.format(nome, anoNasc))


carac = nome.__len__()

print(carac)