#Consumo API

#Api serve para recuperarmos dados a partir da chamada de um programa
#Tipicamente esses "programas" estao disponiveis em alguma url

# nossa aplicacao --> requisicao para um servidor (API)
# nossa aplicacao <-- resposta

#Requisicoes sao feitas atraves do REQUEST
#Quando usamos http usamos a biblioteca requests
#pip install requests
#dinamica
#para fazer a requisicao usamos requests.get
#e recebemos a resposta com resposa.json

#tambem temos o status da resposta
#resposta.status_code --> 200 ok, 404 file not found, 500 internal error

import requests
try:
    resposta = requests.get('http://viacep.com.br/ws/01001000/json/')
    if resposta.status_code == 200:
        dados = resposta.json()
        print(dados)
    else:
        raise Exception (f"Erro de requisição {resposta.status_code}")

    

except requests.exception.ConnectionError as e:
    print("Erro de conexão")
except Exception as e:
    print(e)
