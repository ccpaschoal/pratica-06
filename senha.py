import random
import string

def gerar_senha(comprimento: int) -> str:
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(comprimento))
    return senha

# Solicita a quantidade de caracteres ao usuário
tamanho = int(input("Digite o tamanho desejado da senha: "))
senha_gerada = gerar_senha(tamanho)

print(f"Sua senha gerada é: {senha_gerada}")
