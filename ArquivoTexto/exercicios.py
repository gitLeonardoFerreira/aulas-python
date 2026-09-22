#1

# try:
#     arqNum = open('numeros.txt', 'w', encoding='utf-8')
#     for i in range(10):
#         n = int(input(f'Entre com o {i+1} numero inteiro: '))
#         arqNum.write(f'{n}\n')
#     arqNum.close()
# except ValueError:
#     print('Entre com número inteiro')
# except Exception as erro:
#     print(f'Ocorreu um erro na linha {erro}')

# #2

# arqNum = open('numeros.txt', 'r')
# print(f'A soma dos numeros é: {sum(int(linha) for linha in arqNum)}')
# arqNum.close()

#3
# try:
#     arqTxt = open('arquivos.txt', 'w', encoding='utf-8')
#     l = input('Digite caracteres: ')
#     for i in l:
#         print(i)
#         if i == '0':
#             raise ValueError('Digite um caractere válido!')
#         arqTxt.write(f'{i}')
#     arqTxt.close()
# except ValueError as v:
#     print(f'{v}')

#4
# try:
#     number = []
#     arqPar = open('pares.txt', 'w', encoding='utf-8')
#     arqImp = open('impares.txt', 'w', encoding='utf-8')
#     n = int(input('Entre com o número: '))
#     number.append(n)
#     for i in number:
#         if i % 2 == 0:
#             arqPar.write(f'{number}\n')
#         else:
#             arqImp.write(f'{number}\n')
#     arqPar.close()
#     arqImp.close()
# except ValueError:
#     print('Entre com um númer inteiro')


#6
# try:
#     with open('notas.txt', 'r') as aNotas:
#         linhas = aNotas.readlines()
#         print(linhas)
#         for linha in linhas:
#             aluno = linha.strip().split(',')
#             #print(aluno)
#             media = float(aluno[0]) + float(aluno[1])
#             print(f'{aluno[1]} media: {media:.1f}')
# except FileNotFoundError:
#     print('Arquivo de notas')

#7
# try:
#     ips = set()
#     with open('ips.txt', 'r') as aips:
#         for linha in aips.readline():
#             ips.add(linha.strip())
#     ips = list(ips)
#     ips.sort()
#     print(ips)
#     with open('ips_unicos.txt', 'w') as aips:
#         aips.writelines([ip + '\n' for ip in ips])



# except Exception as erro:
#     print(erro)

#8
try:
    contagem = 0
    