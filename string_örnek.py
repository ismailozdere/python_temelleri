website="htttp://www.sadikturan.com"
course="python kursu:baştan sona python programlama rehberiniz(40 saat)"
#"course" karakter diziis kaç karakterden oluşmaktadır 
print(len(course))
#"website "wwww karakterlerini alın 
print(website[8:11])
#website içinden  com karakterlerini alın
print(website[23:26])
# course içinden ilk 15 ve son 15 karakteri alın 
print(course[0:15])
print(course[-15:-1])
# course ifadesindeki karakterleri tersten yazdırın  
print(course[::-1])
name,surname,age,job="bora","yılmaz",32,"mühendis"
#yukarıda verilen değişkenler ile ekrana 
#"benim adım boora yılmaz , yaşım 32v mesleğim mühendis "
print(f"benim adım {name},{surname},yasım {age}mesleğim {job}")
#"lhello word" ifadesindeki w yi W ile değiştirin 
s="hello world"
s=s[0:6] +"W"+s[-4:]
print(s)
#"abc" iifadesini yan ayana 3 kez yazdırın 
result="abc"*3
print(result)