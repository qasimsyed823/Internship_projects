"""Design a Library System with Book and Member classes.
   Books can be borrowed and returned; track availability status. 
   Use OOP principles throughout."""

class Book:
    def __init__(self,title,author):
        self.title =title
        self.author = author
        self.is_available = True

    def borrow_book(self):
        if self.is_available:
            self.is_available = False
            return True
        return False
    
    def return_book(self):
        self.is_available = True

    def __str__(self):
        status = "Available" if self.is_available else "Borrowed"
        return f"{self.title} by {self.author} ({status})"

    def __repr__(self):
        return self.__str__()


class Member:
    def __init__(self,member_id,name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def borrow(self,book):
        if book.borrow_book():
            self.borrowed_books.append(book)
            print(f"{self.name} borrowed '{book.title}' by '{book.author}'")
        else:
            print("Book is not available")

    def give_back(self,book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
            print(f"{self.name} returned '{book.title}' by '{book.author}'")
        else:
            print(f"This Book was not borrowed by the {self.name}")


class library:

    def __init__(self):
        self.books ={}
        self.member ={}

    
    def add_books(self,book):
        self.books[book.title] = book

    def add_member(self,member):
        self.member[member.member_id] = member

    def display(self):
        for book in self.books.values():
            print(book)


book1 = Book("Python","john")
book2 = Book("Django","Harry")
book3 = Book("OB","Stefen")

Library = library()

Library.add_books(book1)
Library.add_books(book2)

# Create Member
member1 = Member(101, "Ali")

Library.add_member(member1)

# Borrow Book
member1.borrow(book1)

# Display Books
Library.display()

# Return Book
member1.give_back(book1)

Library.display()

#---------------------------------------------------------------------------------------------

"""Build an Employee Payroll system: Employee base class with Manager and 
   Engineer subclasses. Each subclass calculates salary differently including bonuses."""

class Employee:
    def __init__(self,name,emp_id,base_salary):
        self.name = name
        self.emp_id = emp_id
        self._base_salary = base_salary
    
    def calcSalary(self):
        return self._base_salary
    
    def __str__(self):
        return f"ID: {self.emp_id}, Name: {self.name}, Salary: {self.calcSalary():,.2f}"

    def __repr__(self):
        return self.__str__()
    
class Manager(Employee):
    def __init__(self, name, emp_id, base_salary,bonus):
        super().__init__(name, emp_id, base_salary)
        self.bonus = bonus
    
    def calcSalary(self):
        print(f"Base Salary {self._base_salary}")
        print(f"Bonus {self.bonus}")
        Total_Salary=self._base_salary + self.bonus
        return Total_Salary
    
class Engineer(Employee):
    def __init__(self, name, emp_id, base_salary,performance_bonus):
        super().__init__(name, emp_id, base_salary)
        self.performance_bonus = performance_bonus

    def calcSalary(self):
        print(f"Base Salary {self._base_salary}")
        print(f"Bonus {self.performance_bonus}")
        Total_salary=self._base_salary +(self._base_salary * self.performance_bonus/100)
        return Total_salary

    
eng = Engineer("qasim",101,90000,100)
#eng.calcSalary()

mng = Manager("Ali",101,50000,10000)
#mng.calcSalary()

class PayrollSystem:
    def __init__(self):
        self.employees =[]

    def add_employees(self,employee):
        self.employees.append(employee)

    def generate_payroll(self):
        print("----------Payroll Report-----------")
        for emp in self.employees:
            print(emp)
            print("-----------------------------------")

payroll = PayrollSystem()
payroll.add_employees(eng)
payroll.add_employees(mng)
payroll.generate_payroll()

#-----------------------------------------------------------------------------------------


"""Create a contact book app that saves and loads contacts to a JSON file. 
Support add, search, delete, and list-all operations with a menu-driven interface."""


import json
import os

File = "todo.json"

if not os.path.exists(File):
    data = {"contacts":[]}

    with open(File,'w',encoding="utf-8") as f:
        json.dump(data,f,indent=2)
    print(f"{File} created successfully with empty contact list")
    
else:
    print("File already exixts")


def load_data():
    with open(File,'r') as f:
        return json.load(f)

def save(data):
    with open(File,'w',encoding="utf-8") as f:
        json.dump(data,f,indent=2)
    print("Data Saved successfully!")


def view_contact():
    data = load_data()
    for i,c in enumerate(data["contacts"],start=1):
        print(f"{i}.{c['contact']}-{c['contact_name']}")


def add_contact():
    data = load_data()
    contact = int(input("Enter contact number "))
    contact_name =input("Enter contact name ")
    new_contact = {"contact":contact,"contact_name":contact_name}
    data["contacts"].append(new_contact)
    save(data)
    print("Contact Added")


def search_contact():
    data = load_data()
    name = input("Enter name of contact to search ")
    found =  False
    for c in data['contacts']:
        if c['contact_name']==name:
            print(f"{c}")
            found= True
            break
    if not found:
        print("Not Found")

    
def del_contact():
    data = load_data()
    name = input("Enter name of contact to delete ")
    found = False
    for c in data['contacts']:
        if c['contact_name']==name:
            data["contacts"].remove(c)
            print("Deleted Successfully")
            save(data)
            found = True
            break
    if not found:
        print("Not Found")
    

while True:
    print("----------Contact Book----------")
    print("1.View All Contacts ")
    print("2.Add new Contact ")
    print("3.Search Contact")
    print("4.Delete Contact")
    print("5.Exit")
    print("--------------------------------")

    user = int(input("Enter your choice "))
    if user ==1:
        view_contact()
    elif user ==2:
        add_contact()
    elif user ==3:
        search_contact()
    elif user ==4:
        del_contact()
    elif user ==5:
        break
    else:
        print("Enter corrrect choice!")

    
      