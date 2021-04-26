sayi1=int(input("sayi1 giriniz: "))
sayi2=int(input("sayi2 giriniz: "))
sayi3=int(input("sayi3 giriniz: "))

metin ="en büyük sayı {} ortanca sayı {} en küçük sayı {} "
if sayi1==sayi2 and sayi1==sayi3:
    print("sayılar eşittir")
elif  sayi1>sayi2 and sayi1>sayi2:
    if sayi2>sayi3:
        print(metin.format(sayi1 ,sayi2 ,sayi3))
    else:
        print(metin.format(sayi1, sayi3,sayi2))
        
elif sayi2>sayi1 and sayi2>sayi3:
    if sayi3>sayi1:
        print (metin.format(sayi2 ,sayi3 ,sayi1))
    else:
        print(metin.format(sayi2, sayi1,sayi3))
    
else  :
    if sayi1>sayi2:
        print(metin.format(sayi3,sayi1,sayi2))
    else:
        print(metin.format(sayi3,sayi2,sayi1))
        