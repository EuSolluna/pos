import requests
import json
from requests.auth import HTTPBasicAuth
from getpass import getpass

user = input("User: ")
password = getpass()
opcao = ""

while (opcao!="4"):
    opcao = input("1: Listar seus seguidores; 2: Seguir alguém; 3: Parar de seguir; 4: Sair; R:  ")
    if opcao == "1":
        response = requests.get('https://api.github.com/user/followers', 
                    auth = HTTPBasicAuth(user, password))
        for followers in response.json():
            print(followers["login"])

    elif opcao == "2":
        follow = input("Digite o ID do user que deseja seguir: ")
        response = requests.put('https://api.github.com/user/following/'+follow, 
            auth = HTTPBasicAuth(user, password))
        if(response.status_code == 204):
            print("Agora você segue "+ follow + " !")

    elif opcao == "3":
        follow = input("Digite o ID do usuer que deseja parar de seguir: ")
        response = requests.delete('https://api.github.com/user/following/'+follow, auth = HTTPBasicAuth(user, password))
    print(response)