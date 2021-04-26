sayı=int(input("bir sayı giriniz"))
a=0
bolen=0
while a<=sayı:
    if a%sayı==0:
        bolen+=1

if bolen==2:
    print(f"{sayı} girdiğiniz sayı asal sayıdır")
else :
    print(f"{sayı} girdiğiniz sayı asal sayı değildir")    
