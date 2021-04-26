# error handling=> hata yönetimi 

"""
try:
    x= int(input("x: "))
    y=int(input("y: "))
    print(x/y)
except (ZeroDivisionError, ValueError) as e:
    print(" yanlış ifade girdiniz ")
    print(e)"""

""" 
try:
    x= int(input("x: "))
    y=int(input("y: "))
    print(x/y)
except :
    print(" yanlış ifade girdiniz ")"""
    

while True:
    try:
        x= int(input("x: "))
        y=int(input("y: "))
        print(x/y)
    except :
        print(" yanlış ifade girdiniz ")
    else:
        break
    finally:
        print("try except sonlandı. ")  