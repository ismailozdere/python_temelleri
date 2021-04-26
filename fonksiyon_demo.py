"""def  yazım(sayı,kelime):
    print(kelime* sayı)  
    
    

yazım("merhaba\n",10)"""

#2- kendine gönderilen sınırsız sayıdaki parametreyi bir listeye çeviren fonksiyon 
"""
def listeleyici(*ekle):
    parametre=[]


    for param in ekle :
        parametre.append(param)  

    return parametre
    
result=listeleyici(10,20,30,"merhaba")

print(result)
"""
"""
def  asal(baslangic,bitiş):
    for deney in range(baslangic,bitiş+1):
        if  deney>1: 
            for i in range(2,deney):
                if (deney % i== 0):
                    break
                else:
                    print(f"girdiğiniz sayı {deney} asaldır")


baslangic =int(input("başlangıç değeri giriniz"))
bitiş =int(input("bitiş değeri giriniz"))       

asal(baslangic,bitiş)"""
a=0
while True:
    print(a)
    a+=1