#Exessoes
#sao erros que acontecem no tempo de exessao de um programa

##programa base##
# print('\nTicket medio supermercado')
# valor = float(input('Digite um valor gasto na compra: '))
# qtde = int(input('Digite a quantidade de itens da compra: '))
# ticket_medio = valor / qtde
# print(f'O seu ticket medio é R${ticket_medio:.2f}')
##

# print('\nTicket medio supermercado - com tratamento de erro basic')
# try:
#     valor = float(input('Digite um valor gasto na compra: '))
#     qtde = int(input('Digite a quantidade de itens da compra: '))
#     ticket_medio = valor / qtde
#     print(f'O seu ticket medio é R${ticket_medio:.2f}')
# except:
#     print('Valor invalido')


print('\nTicket medio supermercado - com tratamento de erro especifico')
try:
    valor = float(input('Digite um valor gasto na compra: '))
    qtde = int(input('Digite a quantidade de itens da compra: '))
    ticket_medio = valor / qtde
    print(f'O seu ticket medio é R${ticket_medio:.2f}')
except ZeroDivisionError:
    print('Quantidade zerada')
except ValueError:
    print('Valor invalido')
