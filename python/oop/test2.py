class Vehicle(object):
  def __init__(self, speed, mpg):
    self.cost=0
    self.speed = speed
    self.mpg = mpg
  

class Bycicle(Vehicle):
  def __init__(self, speed, mpg, suspension):
    self.suspension = suspension
    super(Bycicle, self).__init__(speed,mpg)
   
  def start(self):
    print "Trim Trim"    

  def __enter__(self):
    print "Doing something before creatint the class"

  def __exit__(self, type, value, traceback):
    print "Tear Things Down"

  def __del__(self):
    print "This class is being removed"

bycicle = Bycicle(50, 0, 'no')

with bycicle:
  bycicle.start()
