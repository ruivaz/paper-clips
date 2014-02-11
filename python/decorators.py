def MyDecorator(f):
  def new_f():
    print "My name is"
    f()
    print "And I am 22 years old"
  return new_f
  


@MyDecorator
def myFunction():
  print "Rui"

myFunction()
