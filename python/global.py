stratus=5


def func1():
  global stratus
  stratus=11
  print stratus


def func2():
  print stratus

func1()
func2()
print stratus
