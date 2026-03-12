class person(object):
       population=500
       def __init__(self,name,age):
              self.name=name
              self .age=age

       @classmethod
       def getpopulation(cls):
              return cls.population
       
       @staticmethod
       def isadult(age):
              return age>=18
       
       def display(self):
              print(self.name)
              print(self.age)
              
newperson=person("Eamon",16)
print(person.isadult(16))