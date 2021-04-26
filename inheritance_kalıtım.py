""""
inheritance (kalıtım ): miras alma
"""
class Person():
    def __init__(self , fname, lname):
        self.firstname=fname
        self.lastname=lname
        print("person created")
    
    def Who_am_i(self):
        print("ı am a person ")
    
    def eat(self):
        print("ı am eating")


class Student(Person):
    def __init__(self ,fname, lname, number):
        Person.__init__(self,fname, lname)
        self.studentnumber= number
        print("student created ")

    #override
    def Who_am_i(self):
        print("ı am a student")
    
    def sayhello(self):
        print("ı am a student")

class Teacher(Person):
    def __init__(self, fname, lname, branch):
        super().__init__( fname, lname)
        self.branch=branch

    def Who_am_i(self):
        print(f"ı a  {self.branch} teacher")



p1=Person("ali", "yılmaz")
s1=Student("iso","özdere" , 1234)
t1=Teacher("namık","özdere","math")

print(p1.firstname + "" + p1.lastname)
print(s1.firstname + "" + s1.lastname+" " +str(s1.studentnumber))

p1.Who_am_i()
s1.Who_am_i()
p1.eat()
s1.eat()
s1.sayhello()
t1.Who_am_i()