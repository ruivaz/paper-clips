def MyDecorator(f):
  def new_f():
    print 'Hello What are you doing'
    f()
    print 'GoodBye'
  return new_f()



@MyDecorator
def rui():
  print 'My name is Rui' 
 
