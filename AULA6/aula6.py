nome = 'Lucas'
idade = 22
altura = 1.85
maior_idade = idade > 18
peso = 90
imc = peso / altura**2


print(f'{nome} tem {idade} anos, {peso}Kg e tem um imc de {imc:.2f}')
print('{} tem {} anos, {}Kg e tem um imc de {:.2f}'.format(nome, idade, peso, imc))