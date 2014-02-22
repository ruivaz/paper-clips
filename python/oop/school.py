class SchoolMember:
  def __init__(self, name, age):
    self.name = name
    self.age = age
    print 'Initialized school member: %s' % self.name
  def tell(self):
    '''Tell my Details'''
    print 'Name: "%s" Age: "%s"' % (self.name, self.age)

class Teacher(SchoolMember):

  def __init__(self, name, age, salary):
    SchoolMember.__init__(self, name, age)
    self.salary = salary
  
  def tell(self):
    SchoolMember.tell(self) 
    print 'Salary %s ' % self.salary 

class Student(SchoolMember):

  def __init__(self, name, age, grads):
    SchoolMember.__init__(self, name, age)
    self.grads = grads

  def tell(self):
    SchoolMember.tell(self)
    print 'Grads %s ' % self.grads

t = Teacher("Anthony", 52, 123000)
s = Student("Vaz", 27, 140000)

members = [s, t]

for member in members:
  member.tell()
