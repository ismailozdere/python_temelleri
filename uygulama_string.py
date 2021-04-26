website="htttp://www.sadikturan.com"
course="python kursu:baştan sona python programlama rehberiniz(40 saat)"
harc="hello world" 
#" hello world " karakter dizisinin baş ve sondai boşluklarını silin 
message=" hello world ".strip()
print(message)
#"website deki sadikturan hariç "bütün karakterleri silin 
website=website.split(".")
print(website[1])
#course karakter dizisinin tüm karakterlerini küçük harf yapın
course=course.lower()
print(course)
#wesite içinde kaç tane a karakteri vardır 
print(website.count("a"))
#website www ile başlayıp com ile bitiyor mu 
website=website.startswiht("www")
website=website.endswith("com")
#webssite içinde .com ifadesi var mı 
x=".com" in website
print(x)
#course içindeki karakterlerin hepsi alfabetik mi 
#contents ifadesindeki satırda 50 karkater içine yerlaeştirip sağ ve soluna *ekleyin 

#course karakter dizindeki tüm boşluk karaterlerini - ile değiştirin
course=course.replace(" ","-")
#hello world karakter dizisindeki world ifadesini there olarak değiştirin
harca=harc.replace("world","there")
print(harca)
#course karakter dizisini boşluk karaktelerinden ayırın 
course=course.split(" ")
print(course)