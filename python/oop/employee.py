#!/usr/bin/python

class Hello:
  def __init__(self):
    print "Hello"

class Employee(Hello):
  '''Common base class for all employees'''
  empCount = 0  
 
  def __init__(self, name, salary, address):
    self.name = name
    self.salary = salary
    self.id = Employee.empCount
    self.__address = address
    Employee.empCount += 1

  def displayCount(self):
    print 'Number of Employees %d ' % Employee.empCount

  def displayInfo(self):
    print 'Name: ' + self.name
    print 'Address: ' + self.__address


  def displaySalary(self):
    print 'Salary %d' % self.salary
  
  def __del__(self):
    Employee.empCount -= 1 
    print self.name + " is being delete"   


emp1=Employee('Sara', 14000, "Rua de Camoes")
emp2=Employee('Jenelle', 19000, "Rua da Boavista")


a = emp1.displayInfo()

print a
print '-------------------------'

