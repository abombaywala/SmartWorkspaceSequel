class myClass():
    def some_method(self):
        print(f"Say hi to {self}")

myObject = myClass()
print(myObject.some_method())
print(myClass.__init__)
print(myObject.__init__)

class myOtherClass():
    def __init__(self, name):
        self.name = name

myOtherObject = myOtherClass('Tommy')
print(myOtherObject.name)
