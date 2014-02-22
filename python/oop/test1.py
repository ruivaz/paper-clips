class Person(object):
  def __init__(self, name, age):
    self.name=name
    self.age=age
  
  def name(self):
    return self.name
  

  def setAddress(self, address):
    self.address=address

class Police(Person):
  def __init__(self, name , age, gun):
    self.gun = gun
    super(Police, self).__init__(name, age)

rui=Police('Rui', 16, 'Ak47')


print rui.__dict__

