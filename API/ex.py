# texto ="""<body>
#     <h1>Titulo Principlas da Pagina</h1>
#     <p>Este é um paragrafo comum de texto.Vode pode usar <b>negrito</> e <i>italico</i> para escrever </p>
#     <h2>Subtitulo da Seção</h2>
#     <p>Este é o segundo parágrafo, separando do anterior</p>
# </boddy>"""



# print(texto)
# import re
# textopuro = re.sub(r'<[^>]+>','', texto)
# print(textopuro)

# #Ex1 

# import requests 
# def get_info_teste (url:str):
#     try:
#         if url:
#             resposta = requests.get(url, verify=False)
#         if resposta.status_code == 200:
#             dados = resposta.json()


#ex 6
import requests

def get_clima():
    try:
        latitude = input('Digite a latitude - até 90: ')
        longitude = input('Digite a longitude - até 90: ')
        clima = requests.get(f'https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true')
        if clima.status_code == 200:
            dados = clima.json()
            clima_atual = dados['current_weather']
            print(f'Temperatura:{clima_atual['temperature']} Celsius')
            print(f'Velocidade Vento:{clima_atual['windspeed']} KM/H')
    except requests.exception.ConnectionError as e:
        print('Erro de conexao')
    except Exception as e:
        print(e)









#7
# import requests

# def get_image():
#     try:
#         response = requests.get('https://science.nasa.gov/wp-json/wp/v2/apod-basic', timeout=)
#         print(type(response))
#     except Exception as e:
#         print(f'Erro: {e}')






if __name__ =='__main__':
    #get_image()
    get_clima()