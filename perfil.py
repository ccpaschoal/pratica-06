import requests

def gerar_usuario():
    response = requests.get('https://randomuser.me/api/')
    if response.status_code == 200:
        usuario = response.json()['results'][0]
        nome = f"{usuario['name']['first']} {usuario['name']['last']}"
        email = usuario['email']
        pais = usuario['location']['country']

        print(f"Nome: {nome}")
        print(f"Email: {email}")
        print(f"País: {pais}")
    else:
        print("Erro ao gerar usuário.")

gerar_usuario()
