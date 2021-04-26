""" 
1-100 arasında rasgele sayı üretilecek bir sayıya aşağı yukarı ifadeleri ile buldurmaya çalışın . 
** "random modülü "
** 100 üzerinden puanlama yapın 
** hak bilgisini kuklanıcıdan alın 
"""
a=0
import random
random.randint(0,100)
randomsayı=int(random.random())
deneme=int(input("kaç kez denemek istersiniz"))
sayac=0


while deneme>0:
    sayac+=1
    deneme-=1
    tahmin=int(input("tahmin giriniz : "))
    if tahmin==randomsayı:
        print(f" tahmininiz doğru {sayac} defa da buldunuz puanınız {100-(100/deneme)*(sayac-1)}  " )
        break
    elif tahmin>randomsayı:
        print(f"{tahmin} girdiğiniz sayı küçültün  ")
    else :
        print(f"{tahmin} girdiğiniz sayı büyültün   ")
   


