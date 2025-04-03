# Exercícios Básicos de Python - Uso de APIs e Geração de Dados Aleatórios

Este repositório contém soluções práticas para exercícios utilizando Python, abordando geração de senhas, consultas a APIs públicas e manipulação básica de JSON.

## Scripts Incluídos

1. **`senha.py`**: Gera uma senha aleatória utilizando letras, números e caracteres especiais. O usuário pode escolher o tamanho desejado da senha.

2. **`perfil.py`**: Consulta a API Random User Generator para criar um perfil aleatório contendo nome completo, email e país do usuário gerado.

3. **`cep.py`**: Realiza uma consulta de endereço através da API ViaCEP, exibindo o logradouro, bairro, cidade e estado correspondentes ao CEP informado pelo usuário.

4. **`cotacao.py`**: Consulta cotações atuais de moedas estrangeiras em relação ao Real Brasileiro (BRL), utilizando a API AwesomeAPI. Exibe a cotação atual, máxima, mínima, além da data e hora da última atualização.

## Dependências

Certifique-se de ter instalado a biblioteca `requests` antes de executar os scripts. Você pode instalá-la utilizando o comando:

```bash
pip install requests
```

## Como Executar

Para executar qualquer um dos scripts, abra um terminal no diretório dos arquivos e utilize os comandos abaixo:

```bash
python senha.py
python perfil.py
python cep.py
python cotacao.py
```

## Exemplos de APIs Utilizadas

- [Random User Generator](https://randomuser.me/)
- [ViaCEP](https://viacep.com.br/)
- [AwesomeAPI](https://docs.awesomeapi.com.br/)

