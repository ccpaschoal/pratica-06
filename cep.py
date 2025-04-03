import requests

def consultar_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    resposta = requests.get(url)
    
    if resposta.status_code == 200:
        endereco = resposta.json()
        if 'erro' not in endereco:
            print(f"Logradouro: {endereco['logradouro']}")
            print(f"Bairro: {endereco['bairro']}")
            print(f"Cidade: {endereco['localidade']}")
            print(f"Estado: {endereco['uf']}")
        else:
            print("CEP não encontrado.")
    else:
        print("Erro ao consultar CEP.")

cep_usuario = input("Digite o CEP desejado (apenas números): ")
consultar_cep(cep_usuario)
