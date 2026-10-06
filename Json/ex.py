import json

# with open ('notas.txt', 'r') as aNote:
#         for linha in aNote:
#             linha = linha.strip()
#             print(linha)
#             notas = linha.split(',')
#             print(notas)
#             rm = notas[0]
#             nome = notas[1]
#             nota_str = notas[2:]
#             nota_float = [float(nota) for nota in nota_str]
#             notas[rm] = {'nome':nome, 'notas':nota_float}

# with open('notas.json', 'w', encoding='utf-8') as arqAluno:
#       json.dump(notas, aNote, indent=4, ensure_ascii=False)



with open('heroes.json', 'r') as aHero:
    herois = json.load(aHero)
    print(type(herois))
    members =  herois["members"]
    for member in members:
        if 'Flight' in member["powers"]:
            print(member["name"], member["powers"])


 