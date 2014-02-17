#!/usr/bin/python

class Employee:
  'Common base class for all employees'
  empCount = 0
  
  def __init__(self, name, salary):
    self.name = name
    self.salary = salary
    Employee.empCount += 1

  def displayCount(self):
    print 'Number of Employees %d ' % Employee.empCount

  def displayName(self):
    print 'Name: ' + self.name
 
  def displaySalary(self):
    print 'Salary %d' % self.salary
    


emp1=Employee('Sara', 14000)
emp1.displayCount()

emp2=Employee('Jenelle', 19000)

emp1.displayCount()
emp1.displayName()
emp1.displaySalary()

emp2.displayName()
emp2.displaySalary()
