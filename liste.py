arabalar=["bmw","mercedes","opel","mazda"]
#listre  kaç elemanlı

print(len(arabalar))
#listenin ilk ve son elemanı nedir"
result=arabalar[0]
print(result)
result=arabalar[3]
print(result)
#mazda değerini toyota ile değiştir
arabalar[-1]="toyota"
print(arabalar)
#mercedes listenin bir değeri midir
result="mercedes" in arabalar
print(result)
#listenin -2 indeksindeki değeri nedir
print(arabalar[-2])
#listenin ilk 3 elemaının alın
print(arabalar[0:3])

#listenin son 2 elemanı yerine toyota ve renault değerini ekleyin 
arabalar[-2:]=["toyota","renault"]
print(arabalar)
#listenin üzerine audi ve nissam değerlerini ekleyin
result=arabalar+["audi","nissan"]
print(result)
#listenin son elemanını silin 
del arabalar[-1]
result=arabalar
print(result)
#liste elemanlarını tersten yazdırın
result=arabalar[::-1]
print(result)
#aşağıdaki verileri bir şiste içinre saklayin 
    #studenta:yigit bilgili 2010,(70,60,70)
    #studentb:sena turan    1999,(80,80,70)
    #studentc:ahmet turan   1998,(80,70,90)

studenta=["yigit"," bilgili", 2010,[70,60,70]
studentb=["sena", "turan"  ,  1999,[80,80,70]
studentc=["ahmet", "turan",   1998,[80,70,90]



#liste elemanları ekrana yazdırın 
result=f"{studenta[0]} {studenta[1]} {2019-studenta[2]} yaşında ve not ortalaması {studenta[3][0] +studenta[3][1]+studenta[3][2]}"
print(result)