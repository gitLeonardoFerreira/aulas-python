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


# print('\nTicket medio supermercado - com tratamento de erro especifico')
# try:
#     valor = float(input('Digite um valor gasto na compra: '))
#     qtde = int(input('Digite a quantidade de itens da compra: '))
#     ticket_medio = valor / qtde
#     print(f'O seu ticket medio é R${ticket_medio:.2f}')
# except ZeroDivisionError:
#     print('Quantidade zerada')
# except ValueError:
#     print('Valor invalido')


#lançamento de exessão
#lançamos exeção quando do ponto de vista do negocio aquela operação esta errada 
#nesse caso do exemplo, qdo temos um valor negativo de compras ou de quantidades
print('\nTicket medio supermercado - com lançamento de exeção')
try:
    valor = float(input('Digite um valor gasto na compra: '))
    qtde = int(input('Digite a quantidade de itens da compra: '))
    if valor < 0 or qtde < 0:
        #raise Exception('O valor ou quantidade negativo') #lançando exeção
        raise ValueError('O valor ou quantidade negativo')
    ticket_medio = valor / qtde
    print(f'O seu ticket medio é R${ticket_medio:.2f}')
except ValueError as v:
    print(f'Valor invalido:{v}')
except Exception as e:
    print(f'Ocorreu um erro, contate o administrador: {e}')
else: #só executa qdo não ha err
    print(f'O seu icket médio é R${ticket_medio:.2f}')
finally:
    print('Obrigado por comprar no supermercado BEM BARATO')