class Animal:
    Cat = "animal"
    Dog = "animal"
    Mouse = "animal"

    def __init__(self,name,feature):
    	self.ten = name
    	self.text = feature

class Cat(Animal):
    text = "Meomeo"
dv= Cat("Cat","meo meo")
print(dv.Cat)
print(dv.__dict__)

class Dog(Animal):
	text ="gaugau"
dv1= Dog("Dog","Gau Gau")
print(dv1.__dict__)

class Mouse(Animal):
    text ="chip chip"
dv2= Mouse("Mouse","chip chip")
print(dv2.__dict__)