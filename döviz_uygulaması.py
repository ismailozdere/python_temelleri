import requests
import json

api_url="https://api.exchangeratesapi.io/latest?base="


bozulan_döviz=input("bozulan döviz türü: ")
alinan_döviz= input("alınan döviz türü")
miktar = int(input(f"ne kadar {bozulan_döviz} bozdurmak istiyorsunuz:  "))

result =requests.get(api_url+bozulan_döviz)
result = json.loads(result.text)

print("1{0} ={1} {2}".format(bozulan_döviz, result["rates"][alinan_döviz],alinan_döviz)  )

print("{0}{1}={2} {3}".format(miktar , bozulan_döviz,miktar*result["rates"][alinan_döviz],alinan_döviz )  )




