class member:
    year=2020
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def add_age(self):
        self.age= self.age+1

    def re_locate(self,place):
        self.place= place
    def display(self):
        print("year: "+str(member.year))
        print("name: "+self.name)
        print("age: " +str(self.age))
        print("place: " +self.place)
    @classmethod
    def add_year(cls):
        cls.year=cls.year+1




x=member("faisal",21,"calicut")
y=member("hyra",3,"wayanad")
x.display()
y.display()
print("********************************************")

member.year=member.year+1
x.add_age()
y.add_age()
x.display()
y.display()

print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
member.add_year()
x.add_age()
y.add_age()
x.re_locate("delhi")
y.re_locate("kannur")
x.display()
y.display()



