class Person:

 def __init__(self, age):
     if age >= 0:
         self.age = int(age)
     else:
         self.age = 0
         print("Age is not valid, setting age to 0")

 def yearPassed(self, years):
     self.age+=years
     return self.age

 def amIOld(self):
     if 0<= self.age <13:
         print("You are young")
     elif 13<= self.age <=19:
         print("you are a teenager")

     else:
         print("you are old")



rohit = Person(25)
rohit.amIOld()




