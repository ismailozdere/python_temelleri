 #1- kullanıcıdan isim, yaş, ve eğitim bilgilerini isteyip ehliyet alabilme durumunu kontrol ediniz. ehliyet alma koşulu en az 18 ve 
 # eğitim durumu lise ya da üniversite olmalıdır.

#isim= input("lütfen adınızı yazın :  ")
#yas=int(input("lütfen yaşınızı giriniz.: "))
#okul=input("lütfen eğitim bilgisi verin : ")
#if (( yas>=18) and (okul=="lise") or (okul=="üniversite")  ):
#        print("ehliyet alabilirisiniz .")
#else :
#        print("ehliyet alamazsın")

#2- bir öğrencinin 2 yazılı bir sözlü notunu alıp hesaplanan ortalamaya göre not aralığına karşılık gelen not bilgisini yazdırın 
#   0-24  =>0
#   25-44 =>1
#   45-54 =>2
#   55-69 =>3
#   70-84 =>4
#   85-100 =>5

"""a=int(input("1. not : "))
b=int(input("2. not : "))
ortalama=  ((a+b)/2)
if (ortalama<=24):
    print("not ortalamnız 0")

elif ((ortalama<44) and (ortalama>25)):
    print("not ortalamanız 1")

elif ((ortalama>45) and (ortalama<54)):
    print("not ortalamanız 2")

elif ((ortalama<69) and (ortalama>55)):
    print("not ortalamanız 3")     

elif ((ortalama>70) and (ortalama<84)):
    print("not ortalamanız 4")  

elif ((ortalama>85) and (ortalama<100)):
    print("not ortalamanız 2")  """           


#3- trafiğe çıkış tarihi alınan bir aracın servis zamanını aşağıdaki bilgilere göre hesaplayınız
# 1. bakım => 1. yılı 
# 2. bakım => 2. yılı 
# 3. bakım => 3. yılı 
#  ** süre hesabını alınan gün , ay, yıl bilgisine göre gün bazlı hesaplayınız 
#  *** datetime modülünü kullanmanız gerekiyor.
#  (şimdi ) - (2018/8/1) => gün 
import datetime
tarih=input("araç tarihini (2019/8/9) olarak giriniz")
tarih=tarih.split("/")

trafigecikis=datetime.datetime(int(tarih[0]),int(tarih[1]),int(tarih[2]))
simdi=datetime.datetime.now()
bakım=simdi-trafigecikis
days=bakım.days

if 365>=days:
    print("1 serviz zamanı ")

elif 365<=days and 365*2>=days:
    print("2. servis zamanı ")

elif 365*2<=days and 365*3>=days:
    print("3. servis zamanı ")    

else :
    print("yanlış zaman dilimi")    