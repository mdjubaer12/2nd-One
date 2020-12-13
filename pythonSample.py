#class inheritance simple program
#any class can be the parent class. So the syntax is same as a normal class
#here we will create a class named Person with firstname,  lastname properties and printname methods

class Person:
    def __init__(self_parameter,fname,lname):
        self_parameter.first_name=fname
        self_parameter.last_name=lname
    def printname(self):
       print(self.firstname,self.lastname)
       
#Here we will use the person class to create an object, and excute printname method

x=Person("Jubaer", "Rahman")
x.printname()

#Now we will create a child class to inherite the parent class's properties

class Student(Person):
    x=Student("Ahmed", "Khan")
    x.printname()


#Here we'll create another example

class Parent():
    def __init__(self, txt)
        self.text=txt
    def printtext(self)
        print(self.text)

class Child(Person):
    def __init__(self,txt)
        super.__init__(txt)

x=child("Hello Mr/Mrs, Welcome here")
x.printtext()
