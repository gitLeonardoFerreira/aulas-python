#Dicionarios são coleções do ipo formulario
#sao do tipo chave:valor
#ex
#nome : leo
#idade : 18
#sexo : masculino
# NAO SAO POSICIONAIS - nao tem indice
#eles permitem tipos de dados diferentes
#permitem valores repetidos, porem chaves SAO UNICAS
#permitem inclusao, alteracao e exclusao -> SAO MUTAVEIS
#simbolo = {}

aluno = {'nome':'leo', 'idade':18, 'sexo':'masculino'}
print(aluno)
print(type(aluno))

#se eu quiser pegar qualque valor
print(f'\n{aluno['nome']}') #-> usar []
print(f'\n{aluno['idade']}') #-> usar []
print(f'\n{aluno['sexo']}') #-> usar []

vazio = {}

#inserindo dados no vazio
vazio['categoria'] = 'Brinquedos'
print(f'\n{vazio}')

#inserindo dados no aluno
aluno['profissao'] = 'Eng. de Software'
print(f'\n{aluno}')

#alterando valores
aluno['nome'] = 'Daniel'
print(f'\n{aluno}')
print(f'\n{aluno.get('nome')}')
aluno.update({'idade':19})
print(f'\n{aluno}')

#removendo valores
aluno.pop('idade')
print(f'\n{aluno}')
aluno.popitem() #-> elimina sempre o ultimo elemento
print(f'\n{aluno}')
del aluno['sexo']
print(f'\n{aluno}')

#limpa o dicionario todo
aluno.clear()
print(f'\n{aluno}')

#percorrendo ou varrendo o dicionario
aluno = {'nome':'leo', 'idade':18, 'sexo':'masculino', 'profissao':'eng. de software'}

for caracteristica in aluno: #-> voce acaba pegando todas as chaves
    print(caracteristica)

print('\n 2 ')
for chaves in aluno.keys(): # somente as chaves
    print(chaves) 

print('\n 3 ')
for value in aluno.values(): # somente valores
    print(value)

print('\n 4 ')
for chave in aluno: #somente os valores pela chave
    print(aluno[chave])

print('\n 5 ')
for item in aluno.items():
    print(item)

print('\n 6 ')
for chave, valor in aluno.items():
    print(f'{chave}={valor}')

#atribuição multipla
#x, y, z = 0, 1, 2
#|__|__|_____| | |
#   |__|_______| |
#      |_________|
#print(f'{x}')
#print(f'{y}')
#print#(f'{z}')

#na maior parte das colecoes a copia se da pela igualdade
#vamos examinar a lista
print('\n')
original = ['cafe', 'pao', 'leite']
copiafalsa = original
print(original)
print(copiafalsa)
copiafalsa.append('cachorro')
print('original', original)
print('copiafalsa', copiafalsa)

print('\n')
original = ['cafe', 'pao', 'leite']
copiaverdadeira = original.copy()
print(original)
print(copiaverdadeira)
copiaverdadeira.append('gato')
print('original', original)
print('copiaverdadeira', copiaverdadeira)

#copiando dicionario
print('\n')
alunocopia = aluno.copy()
alunocopia['nome'] = 'Andreia Matos'
print(aluno)
print(alunocopia)