# def usalma(number):

#     def inner(power):
#         return number** power

#     return inner



# two = usalma (2)
# three= usalma(3)
# print(two(3))
# print(three(4))


# def yetki_sorgula(page):
#     def inner (role):
#         if role == "admin":
#             return " {0} rolünün {1} sayfasına ulaşabilir. ".format(role,page)
#         else :
#                 return " {0} rolünün {1} sayfasına ulaşamaz. ".format(role,page)
#     return inner

# user1 = yetki_sorgula( "product edit")
# print(user1("admin"))
# print(user1("user"))


def islem(islem_adi):
    def toplam(*args):
        toplam =0
        for i in args:
            toplam+=i
        return toplam

    def carpma(*args):
        carpim=1
        for i in args:
            carpim*=i
        return carpim

    if islem_adi== "toplam":
        return toplam
    else:
        return carpma

toplama =islem("toplam")
print(toplama (1,2,3,3,4,5,6))

carpım = islem("carpma")
print(carpım(1,2,3,4,5,6,7))
