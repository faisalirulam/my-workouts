class baseclass:
    def display(self):
        print("hello")


class subclass(baseclass):
    def welcome(self):
        print("welcome")


x=baseclass()
x.display()

y=subclass()
y.display()
y.welcome()
