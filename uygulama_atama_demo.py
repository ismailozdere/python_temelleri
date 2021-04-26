x , y, z= 2 , 5, 10

numbers= 1,5,7,10,6


#1- kullanıcıdan aldığınız 2 sayının çarpımı ile x,y,z toplanının farkı nedir
a=int(input("bir sayı giriniz:"))
b=int(input("bir sayı giriniz:"))
result=  (a*b) - (x+y+z)
print(result)

#2- y'nin x're kalasız bölümünü hesaplayınız
bölüm=y//x
print(bölüm)

#3- (x,y,z) toplamının mod 3 ü nedir
mod=(x+y+z)%3
print(mod)

#4-  ynin x kuvvetini hesaplayınız 
result=y**x
print(result)

#5- x, *y,z = numbers işlemine göre z'nin küpü kaçtır?
x,*y,z=numbers

print(z**3)

#6- x,*y,z numbers işlemine göre y nin değerleri toplamı kaçtır?
result=y[0]  +  y[1]  +y[2]
print(result)