class Animal():
    name = "john"
    color = "black"
    age = 5
    action = "bark"

    def getColor(self,msg):
        return msg+" "+self.color

    def getName(self):
        return self.name


class Dog(Animal):
    name = "Tiger"
    color = "Brown"


norm_animal = Animal()
print("Animal class name: "+norm_animal.getName())
print("Animal class color: "+norm_animal.getColor("Dog color is"))
print("Animal class age: "+str(norm_animal.age))

dog = Dog();
print("Dog class name: "+dog.name)
print("Dog class inherit animal class name "+dog.getName())
print("Dog class color :"+dog.color)
print("Dog class inherit animal class color "+dog.getColor("Dog color is"))
