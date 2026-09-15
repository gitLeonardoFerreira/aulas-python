#ex1
# while True:
#     try:
#         numero = int(input('Digite um número: '))
#         numero_quadrado = numero ** 2
#         print(f'O quadrado do seu número é: {numero_quadrado}')
#         break
#     except ValueError:
#         print('Digite um número inteiro')


#ex 2
# try:
#     n1 = int(input('Digite o primeiro número: '))
#     n2 = int(input('Digite o segundo número: '))

#     if n1 == n2:
#         raise ValueError('Números iguais!')

#     if n1 > n2:
#         print(f'O número maior é: {n1} e o número menor é: {n2}')
#     else:
#         print(f'O número maior é: {n2} e o número menor é: {n1}')

# except ValueError as v:
#     print(f'Digite um número válido: {v}')

#Ex 3
# frutas = ["Amora", "Banana", "Carambola", "Damasco"]
# try:
#     letra = input('Digite uma letra entre A, B, C ou D: ').upper()
#     if letra not in ('A', 'B', 'C', 'D'):
#         raise ValueError('Digite uma leta válida!')
#     elif (letra == 'A'):
#         print(frutas[0])
#     elif (letra == 'B'):
#         print(frutas[1])
#     elif (letra == 'C'):
#         print(frutas[2])
#     elif (letra == 'D'):
#         print(frutas[3])
# except ValueError as a:
#     print(f'Erro: {a}')
# except Exception as e:
#     print(e)

#ex 4
# salario_minimo = 1621
# try:
#     salario = float(input('Digite o seu salário: '))
#     if salario < 0 or salario_minimo < 0:
#         raise ValueError('Negativo')
#     else:
#         print(f'Você ganha {salario/salario_minimo:.2f} salarios minimos')
# except ValueError as v:
#     print(f'Valor inválido: {v}')
# except ZeroDivisionError:
#     print('Divisão por zero')
# except Exception as e:
#     print(f'Ocoreu um erro: {e}')

#ex 5
# while True:
#     def buscar_item_por_indice(lista: list[str], indice: int) -> str:
#         return lista[indice]
#     promo = ['regata', 'tenis-nike', 'boné']
#     try:
#         ind = int(input('insira um valor: '))
#         print(f'Item em promocao: {buscar_item_por_indice(promo, ind)}')
#         break
#     except IndexError:
#         print('Indice inválido')
#     except ValueError:
#         print('Valor inválido')

#ex 6
produtos = {'Calça' : 65.00, 'Camisa' : 50.00, 
'Tenis' : 89.99, 'Boné' : 35.99}
print(produtos.keys())
try:
    escolha = input('Escolha um produto da lista: ')
    if escolha in produtos:
        print(f'o preço de {escolha} é {produtos[escolha]}')
    else:
        print('Produto não existente no catálogo.')
except KeyError:
    print('Indice não existente')
except Exception as a:
    print(f'Erro de sistema: {a}')
