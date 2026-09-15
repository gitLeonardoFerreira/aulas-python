#Muitas vezes precisamos acessar o conteudo de um arquivo no file system
#alguns tipos de arquivo o python le naturalmente, outros ele precisa de biblioteca
#especializada
#O arquivo texto é natural do python

print('Arquivo de texo')
#para acessar um arquivo precisamos informar ao SO (sistema operacional) que vamos manipular o arquivo
#isso é feito através do OPEN / CLOSE
arqAlunos = open('alunos.txt', 'r')
print(arqAlunos.readline())
print(arqAlunos.readline(), end='')
print(arqAlunos.readline(), end='')

#ao cehgar no fim do arquivo, ele nao le e nao imprime mais nada
for linha in arqAlunos:
    print(linha, end='')


#se eu quiser voltar a ler o arquivo desde o inicio
#tenho que voltar o cursor para o inicio
print('\n')
arqAlunos.seek(0)
print(arqAlunos.readline(), end='')

print('\n')
listaLinhas = arqAlunos.readlines()
print(listaLinhas)

print('\n')
listaLimpa = [item.strip() for item in listaLinhas]
print(listaLimpa)

print('\nLendo o arquivo todo')
print(arqAlunos.read())

print('\nFechando arquivo')
arqAlunos.close