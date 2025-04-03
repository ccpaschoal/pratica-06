import requests
from datetime import datetime

def consultar_cotacao(moeda):
    url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"
    resposta = requests.get(url)

    if resposta.status_code == 200:
        dados = resposta.json()
        chave = f"{moeda}BRL"
        
        if chave in dados:
            moeda_info = dados[chave]
            print(f"Moeda: {moeda}/BRL")
            print(f"Cotação atual: R$ {moeda_info['bid']}")
            print(f"Cotação máxima: R$ {moeda_info['high']}")
            print(f"Cotação mínima: R$ {moeda_info['low']}")
            timestamp = int(moeda_info['timestamp'])
            data_hora = datetime.fromtimestamp(timestamp).strftime("%d/%m/%Y %H:%M:%S")
            print(f"Última atualização: {data_hora}")
        else:
            print("Código de moeda inválido.")
    else:
        print("Erro ao consultar cotação.")

codigo_moeda = input("Digite o código da moeda desejada (ex: USD, EUR, GBP): ").upper()
consultar_cotacao(codigo_moeda)
