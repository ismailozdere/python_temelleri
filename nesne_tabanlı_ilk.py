# class
"""
class Person:

    #class attributes
    address="no information"
    # constructor ( yapıcı metod)
    def __init__(self, name, year ):

        # object attributes
        self.name=name
        self.year=year
        print("init metodu çalıştı"),

        #methods
        def intro(self):
            print("hello world")

        def calculateage (self):
            return 2020-self.year




#object (instance)
p1= Person("ali",1990)
p2=Person("yağmur",2020)

#updating
p1.name="ismail"
p1.address="samsun"


#accesing object attributrs
print(f"name: {p1.name} year: {p1.year} address: {p1.address}")
print(f"name: {p2.name} year: {p2.year} address: {p2.address}")

print(p1)
print(p2)


print(type(p1))
print(type(p2))"""



class Circle:
    #class object attribute
    pi=3.14

    def __init__(self, yarıcap=1):
        self.yarıcap = yarıcap

    # methods
    def cevre_hesapla(self):
        return 2 * self.pi * self.yarıcap

    def alan_hesapla(self):
        return self.pi   * (self.yarıcap**2)


c1=Circle()
c2=Circle(5)

print(f'c1 : alan = {c1.alan_hesapla()} çevre = {c1.cevre_hesapla()}')
print(f'c2 : alan = {c2.alan_hesapla()} çevre = {c2.cevre_hesapla()}')
