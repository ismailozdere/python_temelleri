#liste= [ "1", "2 ", "5a" ,"10b", "abc", "10", "50" ]

#1: liste elemanları içindeki sayısal değeri bulunuz.

#for x in liste:
#    try:
#        result=int(x)
#        print (result)
#    except ValueError:
#        continue


#2: kullanıcı "q" değerini girmedikçe aldığınız her inputun sayı olduğundan emin olun
#while True:
#   x=input()
#   if x=="q":
#        break
#   
#    try:
#        result=float(x)
#        print(result)
#    except ValueError:
#        continue 


# girilen parola içinde türkçe karakter hatası veriniz .

turkce_karakter= "çşüöıİ"

parola= input("parola giriniz")

for i in parola:
    if i in turkce_karakter:
        raise TypeError(" parola türkçe karakter içeremez")
    else:
        pass

print("geçerli parola")    
