import requests

def main():
    cep_input = input("Digite seu CEP para consulta: ")
    if len(cep_input) !=8:
        print("Quantidade de Digitos Inválida! ")
        exit()
    request = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep_input))
    address_data = request.json()
    return address_data


