#json
#Para tratar arquivos json o pyhton tem uma biblioteca propria
#json

#Arquivos JSON sao texts estruturados

pessoa = {'nome':'Patricia', 'idade':25, 'hobbies':['caminhada', 'tenis']}
print(type(pessoa))
print(pessoa)

#o nome do arquivo tem que comecar com letra Maiuscula
# a biblioteca json vai pegar esse dicionario e transformar num texto
#porque é interessante? porque na hora de gravar um arquivo, nós precisamos de texto
import json
#o metodo dumps, da biblioteca json, converte uma coleção em um texto
pessoa2 = json.dumps(pessoa) # -> dumps (s de string)
print(type(pessoa2))
print(pessoa2)

#o uso mais comum, no entanto é gravar essas informacoes em um arquivo
#o metodo agora muda de nome: dump

with open('alunos.json', 'w', encoding='utf-8') as arqAluno:
    json.dump(pessoa, arqAluno)
    arqAluno.write('\n\n')

with open('alunos.json', 'a', encoding='utf-8') as arqAluno:
    json.dump(pessoa, arqAluno, indent=4)
    
#acentuacao
pessoanova = {'nome':'João Álvarez', 'idade':43, 'hobbies':['caçada de formiga', 'tênis']}
pessoanova2 = json.dumps(pessoanova, indent=4, ensure_ascii=False)
print(type(pessoanova))
print(pessoanova2)

with open('alunos.json', 'a', encoding='utf-8') as arqAluno:
    json.dump(pessoanova, arqAluno, indent=4, ensure_ascii=False)

#Leitura JSON
#enquato o dumps(string)/dump(arquvio) escreve no formato json
#o loads(string) e o load(arquivo) le do formato JSON e coloca numa colecao

pessoatexto = '{"nome":"Antonio", "idade":25, "hobbies":["aeromodelismo", "board games"]}'
print(type(pessoatexto))
print(pessoatexto)
#o metodo LOADS transforma essa string em uma colecao
pessoadicionario = json.loads(pessoatexto)
print(type(pessoadicionario))
print(pessoadicionario)

#como ler de um arquivo? metodo LOAD

with open ('alunos1.json', 'r', encoding='utf-8') as arqAlunos:
    aluno = json.load(arqAlunos)
    print(type(aluno))
    print(aluno)