#Q1.Create a BankAccount class with attributes account_number,owner_name,balance.Add methods to deposit,withdraw,and check balance.
#instance method
class BankAccount:
  def __init__(self,name,owner,balance):
    self.name = name
    self.owner = owner
    self.balance = balance
  def deposit(self,amount):
      self.balance += amount
      print(f"deposit:{amount}.new balance: {self.balance}")
  def withdraw(self,amount):
     self.balance -= amount
     print(f"withdraw:{amount}.update balance: {self.balance}")
  def check_balance(self):
     print(f"current amount:{self.balance}")
acc1 = BankAccount("UBL","Hafia khalid", 100_0000)
acc1.deposit(50000)
acc1.withdraw(10000)
acc1.check_balance()

#Q2.Create a class Book with the following attributes:
# •title
# •author
# •listofreviews
# And add methods to:
# •addanewreview
# •countreviews
# •displayallreviews
class Book:
   def __init__(self,title,author):
      self.title = title
      self.author = author
      self.listofreviews = []
   def addnew_review(self,review):
      self.listofreviews.append(review)
      print(f"addnew_review:{review}")
   def count_review(self):
      total = len(self.listofreviews)
      print(f"count_review:{total}")
   def display_all_review(self):
      print(f"display_all_review:{self.listofreviews}")

boo1 = Book("programming","Hafia")
boo1.addnew_review("Amazing book")
boo1.count_review()
boo1.display_all_review()

#Q3.Create a class student with private attributes_name,_roll_no,and_marks.Provide getter and setter  methods with validation (e.g.,marks cannot be negative,roll number has to be between 1&100& name cannot be empty).
#Encapsulation
class Student:
   def __init__(self,attribute_name,roll_no,marks):
      self.__name = attribute_name
      self.__no = roll_no
      self.__marks = marks #private - data mangling
   def get_name(self):
      return self.__name
   def set_name(self,newName):
      self.__name = newName
   def get_no(self):
      return self.__no
   def set_no(self,newNo):
      self.__no = newNo
   
   def get_marks(self): #getter
      return self.__marks
   def set_marks(self,newMarks): #setter
      self.__marks = newMarks
   
stu1 = Student("Hafia", 52 ,4500)
stu1.set_name("rehan")
stu1.set_no(60)
stu1.set_marks(4000)
print(stu1._Student__name,stu1._Student__no,stu1._Student__marks)
   
#Q4.Create a class Shape with a method area().Create subclasses Circle,Rectangle and Triangle that  the area() method.
#function overriding
class Shape:
   def __init__(self,area):
      self.area = area
class Circle(Shape):
   def __init__(self,radius):
      self.radius = radius
   def area(self): #overriding
      print(f"the area is:{3.14 * self.radius * self.radius}")
class Rectangle(Shape):
   def __init__(self,lenght,width):
      self.lenght = lenght
      self.width = width
   def area(self):
      print(f"the rectangle is:{self.lenght * self.width}")
class Triangle(Shape):
   def __init__(self,base,height):
      self.base = base
      self.height = height
   def area(self):
      print(f"the triangle is:{self.base * self.height * 0.5}")

c1 = Circle(1)
c1.area()
r1 = Rectangle(2,4)
r1.area()
t1 = Triangle(10,4)
t1.area()

#Q5.Create a base class vehicle with attributes like brand and model.Create two subclasses Car and Bike that add extra attributes-seats(inCar) & engine_cc(inBike).
#inheritance
class car:#classes tu subclasses
   def __init__(self,seats):
      self.seats = seats
class bike:
   def __init__(self,engine):
      self.engine = engine
class vehicle(car,bike):
   def __init__(self,seats,engine,brand,model):
      super().__init__(seats)
      bike.__init__(self,engine)
      self.brand = brand
      self.model = model
veh1 = vehicle(25,1,"toyato",3.5)
print(veh1.seats,veh1.engine,veh1.brand,veh1.model)
#subclaasses to classes
class vehicle:
   def __init__(self,brand,model):
      self.brand = brand
      self.model = model
class car(vehicle):
   def __init__(self,brand,model,seats):
      super().__init__(brand,model)
      self.seats = seats
class bike(vehicle):
   def __init__(self,brand,model,engine):
      super().__init__(brand,model)
      self.engine = engine
c1 = car("toyato","BMW",5)
print(c1.brand,c1.model,c1.seats)
b1 = bike("honda","Cd-70",1)
print(b1.brand,b1.model,b1.engine)

#Q6.Create an abstract class with an abstract method calculate_salary().
# Create subclasses Intern,Fulltimeemployee,and ContractEmployee  that implement the method differently. 
#Abstraction
from abc import ABC, abstractmethod
class salary(ABC):
   @abstractmethod
   def calculate_salary(self):
      pass
class Intern(salary):
   def calculate_salary(self):
      print("50_000")
class FullTimeEmployee(salary):
   def calculate_salary(self):
      print("80_000")
class ContractEmployee(salary):
   def calculate_salary(self):
      print("90_000")
Intern = Intern()
Intern.calculate_salary()
FullTimeEmployee = FullTimeEmployee()
FullTimeEmployee.calculate_salary()
ContractEmployee = ContractEmployee()
ContractEmployee.calculate_salary()
   
#Q7.Create a class person that allows the constructor to work with: 
#•nameonly
#•name+age
#•name+age+address
# As direct construct oroverloading(multiple constructors)are not allowed but we have to use default parameters to simulate constructor overloading.
class person:
   def __init__(self,name,age=0,address=0):
      self.name = name
      self.age = age
      self.address = address
p1 =person("hafia",25,"johar town")
print(p1.name,p1.age,p1.address)

#q8.Concept:instance and class Attributes
# .Create a class Player with:
# • a class variable player_count 
# •instance variables name and level Track how many  players  were created.
class player:
   player_count = 0
   def __init__(self,name,level):
      self.name = name
      self.level = level
      player.player_count += 1
      
p1 = player("hafia",2)
p2 = player("rehan",10)
print(p1.name,p1.level)
print(p2.name,p2.level)
print(f"player count:{player.player_count}")

#Q9.Create the following classes:Hebivore,carnivore,Omnivore with some attributes & methods.Then create a class Bear that inherits from all the  above classes   to show case how multiple inheritance works.
#multiple inheritance
class Hebivore:
   def eat_grass(self):
      print("i eat grass")
class carnivore:
   def eat_meat(self):
      print("i eat meat")
class Omnivore:
   def eat_both(self):
      print("i eat both grass and meat")

class Bear(Hebivore,carnivore,Omnivore):
   pass
B1 = Bear()
B1.eat_grass()
B1.eat_meat()
B1.eat_both()

# PROJECT OOPS
#Q10.Mini Project–OOP Chat System
#Letʼs create a Chat System using OOPs concepts.We have to create classes:
#•User
#•Message
#•ChatRoom
#And we have to implement functions:
#•sending messages
#•viewing chat history
#•user joining and leaving the chatroom
class student_room:
   def __init__(self,users):
      self.users = users
class messages:
   def __init__(self,sender,text):
      self.sender = sender
      self.text = text
class chat_room:
   def __init__(self):
      self.users = []
      self.messages = []
   def join_room(self,anyuser):
      self.users.append(anyuser)
      print(f"{anyuser}")
   def send_messages(self,anymessage):
      self.messages.append(anymessage)
      print(f"{anymessage}")
   def view_history(self):
      M1 = self.messages[0]
      print(f"{M1.sender}:{M1.text}")
      M2 = self.messages[1]
      print(f"{M2.sender}:{M2.text}")

u1 = student_room("hafia")
u2 = student_room("maryam")
M1 = messages(u1.users,"i am newer student")
M2 = messages(u2.users,"i am a hardworking student")
ch1 = chat_room()
ch1.join_room(u1.users)
ch1.join_room(u2.users)
ch1.send_messages(M1)
ch1.send_messages(M2)
ch1.view_history()


      
   