class Dog():
    name = 'Tiger'
    color = 'Brown'

    def getColor(self):
        return self.color

    def getName(self):
        return self.name;


obj = Dog()
print(obj.getName())
print(obj.getColor())