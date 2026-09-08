# dicionario = {}

# for _ in range(1, 6):
#     cpf = (input('Digite seu cpf: '))
#     nome = input('Digite seu nome: ')

#     dicionario[cpf] = nome

# print(dicionario)

#2

# produtos = {}
# #cadastro
# for _ in range(2):
#     nome = input('produto: ')
#     preco = float(input(f'valor de {nome}: '))
#     produtos[nome]=preco
# print('\n\n')
# #exibicao
# for nome, preco in produtos.items():
#     if preco > 50:
#         print(f'{nome} : R${preco}')


#3
# alunos_notas = {}

# for _ in range(3):
#     rm = int(input('Entre com seu rm: '))
#     n1 = int(input('Entre com sua primeira nota: '))
#     n2 = int(input('Entre com sua segunda nota: '))
#     n3 = int(input('Entre com sua terceira nota: '))
#     notas = [n1, n2, n3]
#     alunos_notas[rm] = notas

# print(alunos_notas)
# for rm, notas in alunos_notas.items():
#     print(f'{rm} -> {sum(notas)/len(notas):.1f}')

#4 vogais
frase = input('Entre com uma frase: ')
a, e, i, o, u = 0, 0, 0, 0, 0
for letra in frase:
    match letra.lower():
        case 'a':
            a += 1
        case 'e':
            e += 1
        case 'i':
            i += 1
        case 'o':
            o += 1
        case 'u':
            u += 1
qtd_vogais = {'a':a, 'e':e, 'i':i, 'o':o, 'u':u}
print(qtd_vogais)