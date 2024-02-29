"""
Class => Entity or Blue Print of object
Example: 

"""
class Animal:
    def __init__(self,*args):
        if len(args) == 1:
         self.name = args[0]
        elif len(args) ==2:
         self.species = args[0]
        elif len(args) == 3:
         self.name = args[0]
         self.species = args[1]
         self.age = args[2]

    def with_age(self):
      print(f"{self.name} is walking")
       

lion = Animal("Leo","Lion")
print(lion.with_age)
cat = Animal("Whiskers","Cat", 5)   
print(cat.with_age())


# Another Example
class Car:
 def __init__(self, Model, Speed):
   self.Speed = Speed
   self.Model = Model

  
 def model(self):
    print(f"Model is {self.Model}")

 def speed(self):
   print(f"Speed is {self.Speed} Km/hr.")

class Maruti(Car):
  def __init__(self, Model, Speed):
    super().__init__(Model, Speed)

  def name(self):
    super().speed()
    super().model()
    print("Name is Suzuki")

car = Maruti("Maruti",50 )
car.name()     

    
