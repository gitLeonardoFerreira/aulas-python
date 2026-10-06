texto ="""<body>
    <h1>Titulo Principlas da Pagina</h1>
    <p>Este é um paragrafo comum de texto.Vode pode usar <b>negrito</> e <i>italico</i> para escrever </p>
    <h2>Subtitulo da Seção</h2>
    <p>Este é o segundo parágrafo, separando do anterior</p>
</boddy>"""



print(texto)
import re
textopuro = re.sub(r'<[^>]+>','', texto)
print(textopuro)

#Ex1 

import requests 
def get_info_teste (url:str):
    try:
        if url:
            resposta = requests.get(url, verify=False)
        if resposta.status_code == 200:
            dados = resposta.json()