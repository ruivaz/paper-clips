class pet:
  number_of_legs = 0
  def sleep(self):
    print "zzz"

  def count_legs(self):
    print "Doug has %s legs." % doug.number_of_legs


class dog(pet):
  def bark(self):
    print "Woof"

doug = dog()
doug.number_of_legs = 4
doug.count_legs()
doug.bark()
