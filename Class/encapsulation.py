# """Private Access"""
# class Person:
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age    

#     def display(self):
#         print(f"The person name is {self.__name} is {self.__age} years old.") 

# if __name__ =="__main__":
#         person_test = Person(name = "Subinika", age = 22)
#         person_test.display()



# """Protected Access""" 
  
# class Person:
#     def __init__(self, name, age):
#         self._name = name
#         self._age = age 

# class Subinika(Person):
#     def __init__(self,name,age):
#          super().__init__(name,age)

#     def display(self):
#         print(f"The person name is {self._name} is {self._age} years old.") 

# if __name__ =="__main__":
#         person_test = Subinika(name = "Subinika", age = 22)
#         person_test.display()

   
"""Abstraction """
from abc import ABC , abstractmethod
class BankingApp(ABC):
    print(f"Connect to database Successfully")

    def security(self):
        pass  


class MobileApp(BankingApp):
    def login_app(self):
        print("Login Successfully")

    def security(self):
          print("security of mobile app")   
       

if __name__ == "__main__":
    mobile_app= MobileApp()
    mobile_app.security()
