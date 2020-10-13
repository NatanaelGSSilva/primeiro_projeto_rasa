import requests 
import json

print("##############################")
print("###### Consulta CEP ##########")
print("##############################")

def main():
    cep_input = input("Digite seu CEP para consulta: ")

    if len(cep_input) !=8:
        print("Quantidade de Digitos Inválida! ")
        exit()

    request = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep_input))

    address_data = request.json()

    if 'erro' not in address_data:
        print('==> CEP ENCONTRADO <==')
        print('CEP:{} '.format(address_data['cep']))
        print('Logradouro: {} '.format(address_data['logradouro']))
        print('Complemento: {} '.format(address_data['complemento']))
        print('Bairro: {} '.format(address_data['bairro']))
        print('Cidade: {} '.format(address_data['localidade']))
        print('Estado: {} '.format(address_data['uf']))
        # print(request.json())
    else:
        print(f'CEP INVALIDO. {cep_input}')
    print('------------------------------------------------------------------')
    option = int(input("Deseja Realizar uma nova consulta ?\n1.Sim\n2.Sair\n"))
    if option == 1:
        main()
    else:
        print("Saindo")    
if __name__ == '__main__':
    main()