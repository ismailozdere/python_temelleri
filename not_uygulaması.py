def not_hesapla(satir):
    satir= satir[:-1]
    liste= satir.split(":")

    ogrenciadi= liste[0]
    notlar =liste[1].split(",")

    not1= int(notlar[0])
    not2= int(notlar[1])
    not3= int(notlar[2])

    ortalama = (not1+not2+not3)/3

    if ortalama >= 90 and ortalama<=100:
        harf ="AA"
    if ortalama >= 85 and ortalama<=89:
        harf ="BA"
    if ortalama >= 80 and ortalama<=84:
        harf ="BB"
    if ortalama >= 75 and ortalama<=79:
        harf ="CB"
    if ortalama >= 70 and ortalama<=74:
        harf ="CC"
    if ortalama >= 65 and ortalama<=69:
        harf ="DC"
    if ortalama >= 60 and ortalama<=64:
        harf ="DD"
    if ortalama >= 50 and ortalama<=59:
        harf ="FD"
    if ortalama <= 49 :
        harf ="FF"

    return ogrenciadi +": " + harf+ "\n"
    
def ortalamalari_oku():
    with open("sinav_notlari.txt","r",encoding="utf-8") as file:
        for satir in file:
            print(not_hesapla(satir))

def not_gir():
    ad= input("öğrenci adı :  ")
    soyad = input("öğrenci soyad: ")
    not1= input("not 1:  ")
    not2= input("not 2:  ")
    not3= input("not 3:  ")

    with open("sinav_notlari.txt","a", encoding="utf-8") as file:
        file.write(ad+ " "+soyad+":"+not1+","+not2+","+not3+"\n")

def notlari_kayit_et():
    with open("sinav_notlari.txt","r",encoding="utf-8") as file:
        liste = []

    for i in file:
        liste.append(not_hesapla(i))

    with open ("sonuclar.txt","w",encoding="utf-8") as file2:
        for i in liste:
            file2.write(i)


while True:
    islem = input("1- notları oku\n2- not girin\n3- notları kayıt et\n4- çıkış\n")

    if islem=="1":
        ortalamalari_oku()
    elif islem=="2":
        not_gir()
    elif islem=="3":
        notlari_kayit_et()
    else :
        break