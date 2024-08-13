class Human:
    count=0

    def __init__(self,_id=None,_name=None,_add=None):

        if( _add is not None and  'fayoum' in _add):
            self.id=_id
            self.name=_name
            self.add=_add
            Human.count+=1
        else:
            raise ('you must belong to fayoum')
        print('iam constructr',self)
    
    def introduce(self):
        print (f"Hi, my name is {self.name}")

    def speak(self, words):
        print (f"{self.name} says: '{words}'")
  
    def walk(self, steps):
        print (f"{self.name} walked {steps} steps.")
    
    def drink(self):
        print(self.name,'drinked')

    def eat(self):
        print(self.name,'eaten')

    def sleep(self):
        print(self.name,'sleep')

    @classmethod
    def getcount(cls):
        return cls.count 
    @classmethod
    def setcount(cls,newcount):
        if(newcount>0):
            cls.count=newcount
        else:
            raise (f'you have {cls.count }objects how  you want to set {newcount}')
        

person1 = Human(_id=1, _name="maria", _add="fayoum")

person1.introduce() 

person1.speak("Hello, world!")

person1.walk(10)

person1.drink()

person1.eat()

person1.sleep() 

print(Human.getcount())  

Human.setcount(5)  

print(Human.getcount())

class Employee:
    company_name = "ABC Inc."

    def __init__(self, name, age, gender, employee_id, position, salary):
       
        self.name = name
        self.age = age
        self.gender = gender
        self.employee_id = employee_id
        self.position = position
        self.salary = salary

    def describe_job(self):
        return f"{self.name} works as a {self.position} at {Employee.company_name}."

    def work(self, hours):
        return f"{self.name} worked for {hours} hours."

    def give_raise(self, amount):
        self.salary += amount
        return f"{self.name} received a raise. New salary: ${self.salary}"
    
  
employee1 = Employee(name="maria", age=23, gender="Female", employee_id="123", position="Software Engineer", salary=10000)

print(employee1.describe_job())  

print(employee1.work(8))  

print(employee1.give_raise(5000))  


