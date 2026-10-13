#ex2
# def potencia (n, e):
#     if e <= 0:
#         return 1
#     else:
#         return n * potencia(n, e-1)




# if __name__ == '__main__':
#     print(potencia(4, 5))

#ex3

# lista = [9, 70, 5, 17, 22]

# def buscar_numero (lista, n):
#     if len(lista) == 0:
#         return False
#     else:
#         if lista[0] == n:
#             return True
#         else:
#             buscar_numero(lista[1:], n)


# if __name__ == '__main__':
#     print(buscar_numero(lista, 70))

#4

def repeticao(lista, n):
    if len(lista) == 0:
        return 0
    else:
        if lista[0] == n:
            return 1 + repeticao(lista[1:], n)
        else:
            repeticao(lista[1:], n)

if __name__ == '__main__':
    print(repeticao([1,2,5,6,5], 5))