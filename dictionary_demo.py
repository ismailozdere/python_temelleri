'''
     ogrenciler={
         "120":{
             "ad" : "ali",
             "soyadı": "yılmaz",
             "telefon": "532 000 00 01"
          } ,
             "125":{
             "ad" : "can",
             "soyadı": "korkmaz",
             "telefon": "532 000 00 02"
          } ,
             "128":{
             "ad" : "volkan",
             "soyadı": "tükselen",
             "telefon": "532 000 00 03"
          } ,
     }'''


ogrenciler={}

number=input("öğrenci no:")
name= input("öğrenci adı:")
surname=input("öğrenci soyad:")
phone=input("öğrenci telefon")


#ogrenciler[number]={
    "ad": name,
    "soyad":surname,
    "telefon":phone
}



print(ogrenciler)