import requests
from getpass import getpass

api_url = "https://suap.ifrn.edu.br/api/"

user = input("user: ")
password = getpass()
data = {"username":user,"password":password}
response = requests.post(api_url+"v2/autenticacao/token/", json=data)
token = response.json()["access"]

# ano_letivo = input("Ano letivo: ")
# periodo_letivo = input("Período letivo: ")
print(response.json())


# print(response.json())
#token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjk5NjEzNjgzLCJpYXQiOjE2OTk2MTMzODMsImp0aSI6ImE1OWIyZmFkMmVmMDQ1ODg4NjE4YTQzNWExZjdkOTQyIiwidXNlcl9pZCI6MjkxMjU4fQ.8ptNIhF0eQPMWm234HeNaX5wtXEnVdC4kjfuae3Si2w"
# print(token)





headers = {
    "Authorization": f'Bearer {token}'
}
#print(headers)

response = requests.get(api_url+"v2/minhas-informacoes/boletim/2023/1/", headers=headers)

#print(response.text)

disciplinas = response.json()
for disciplina in disciplinas:
    nomeDisciplina = disciplina["disciplina"]
    notaUm = disciplina["nota_etapa_1"]["nota"]
    notaDois = disciplina["nota_etapa_2"]["nota"]
    notaTres = disciplina["nota_etapa_3"]["nota"]
    notaQuatro = disciplina["nota_etapa_4"]["nota"]
    print(f"{nomeDisciplina}: {notaUm} - {notaDois} - {notaTres} - {notaQuatro}")