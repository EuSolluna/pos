import requests
from xml.dom.minidom import parseString

# URL do serviço SOAP
url = "http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso"

# Solicita ao usuário que digite o código do país
codigo = input("Digite o código do país (por exemplo, BR para Brasil): ").upper()

# XML estruturado para obter informações do país

payloadUm = """<?xml version="1.0" encoding="utf-8"?>
			<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
				<soap:Body>
					<CountryName xmlns="http://www.oorsprong.org/websamples.countryinfo">
						<sCountryISOCode>"""+codigo+"""</sCountryISOCode>
					</CountryName>
				</soap:Body>
			</soap:Envelope>"""

payloadDois = """<?xml version="1.0" encoding="utf-8"?>
			<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
				<soap:Body>
					<CountryCurrency xmlns="http://www.oorsprong.org/websamples.countryinfo">
						<sCountryISOCode>"""+codigo+"""</sCountryISOCode>
					</CountryCurrency>
				</soap:Body>
			</soap:Envelope>"""

payloadTres = """<?xml version=\"1.0\" encoding=\"utf-8\"?>
			<soap:Envelope xmlns:soap=\"http://schemas.xmlsoap.org/soap/envelope/\">
				<soap:Body>
					<CapitalCity xmlns=\"http://www.oorsprong.org/websamples.countryinfo\">
						<sCountryISOCode>"""+codigo+"""</sCountryISOCode>
					</CapitalCity>
				</soap:Body>
			</soap:Envelope>"""

# Headers para a chamada de informações do país
headers = {
    'Content-Type': 'text/xml; charset=utf-8'
}

# Request POST para obter informações do país
responseUm = requests.post(url, headers=headers, data=payloadUm)
responseDois = requests.post(url, headers=headers, data=payloadDois)
responseTres = requests.post(url, headers=headers, data=payloadTres)

print(responseUm)
print(responseDois)
print(responseTres)
# Extrai as informações do XML de resposta
nome = (parseString(responseUm.text).documentElement.getElementsByTagName("m:CountryNameResult")[0].firstChild.nodeValue)
moeda = (parseString(responseDois.text).documentElement.getElementsByTagName("m:sISOCode")[0].firstChild.nodeValue)
capital = (parseString(responseTres.text).documentElement.getElementsByTagName("m:CapitalCityResult")[0].firstChild.nodeValue)

# Imprime as informações do país
print(f"{codigo} é o código do país: {nome}")
print(f"Moeda de {nome}: {moeda}")
print(f"Capital de {nome}: {capital}")

