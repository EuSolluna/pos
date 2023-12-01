import zeep

# define a URL do WSDL
wsdl_url = "https://www.dataaccess.com/webservicesserver/NumberConversion.wso?WSDL"

client = zeep.Client(wsdl=wsdl_url)

numero = int(input("digite um número: "))

result = client.service.NumberToWords(
	ubiNum=numero
)
print(result)