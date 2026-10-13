#Recursividade é uma estratégia de quebrar o problema em partes menores até
#um problema conhecido
#ex: 5! => 5x4! => 4! => 4x3! ...... 1x0!, 0!=1
#0! é chamado de condicao base, que é a solucao de um projeto conhecido

def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n-1)

print(fatorial(5))

#problma: somar os elementos de uma lista
#fazer uma função recurssiva
lista = [3, 5, 678, 3, 78, 90]
def soma_lista_sem_recurssao(lista):
    total = 0
    for elemento in lista:
        total += elemento
    return total
print(soma_lista_sem_recurssao(lista))

def soma_lista(lista):
    if len(lista) == 0:
        return 0
    else:
        return lista[0] + soma_lista(lista[1:])
print(soma_lista(lista))
