sayılar= [1,3,5,7,9,12,19,21]
"""
#1- sayılar listesindeki hangi sayılar 3'ün katıdır?
#for  a in sayılar:
    if (a%3==0):
        print(f"{a} sayısı 3'ün tam katıdır : ")
"""

#2- sayılar listesinde sayıların toplamı kaçtır?
toplam=0
for  a in sayılar:
     toplam= toplam + a
    
print(toplam)

#3- sayılar listesindeki tek sayıların karesini alınız.

for  a in sayılar:
    if (a%2==1):
        print(f"{a} sayısı tek sayıdır : ")
