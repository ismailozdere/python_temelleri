names = ["ali","yağmur","hakan","deniz"]
years=[1998,2000,1998,1987]

#1- "cenk" ismini listenin somuna ekleyin
names.append("cenk")
print(names)

#2- "sena" değerini listenin sonuna ekleyin 
names.insert(0,"sena")
print(names)

#3- deniz ismisi listeden silin 
#names.remove("deniz")
print(names)

#4- deniz isminin indeksi nedir 
result=names.index("deniz")
print(result)

#5 - ali listenin bir lemanı mıdır
result="ali" in names
print(result)

#6- liste elemanlarını  ters çeviriniz 
print(names[::-1])
names.reverse()
print(names)

#7- liste elemanlarıı alfabetik larak sıralayın 
names.sort()
print(names)

#8- years listesini rakamsal büyüklüğe göre sıralayınız
years.sort()
print(years)

#9- str="cherolet,dacia" karakterlerini listeye dönüştürün 
str ="chevrolet,dacia"
result=str.split(",")
print(result)

#10- years dizisinin en büyük ve en küçük elemanı nedir
result=max(years)
print(result)
result=min(years)
print(result)

#11- years dizisinin tüm elemanlarını silin 
years.clear()
print(years)
#12- kullanıcıdan alacağınız 3 tan marka bilgisini bir listede saklayın

markalar=[]

marka=input("marka: ")
markalar.append(marka)

marka=input("marka: ")
markalar.append(marka)

marka=input("marka: ")
markalar.append(marka)

print(markalar)