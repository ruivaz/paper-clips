def append567(sequence):
  sequence+=(5,6,7)
  return sequence 

def main():
  list=[1,2,3,4] # lists are mutable
  tuple=(1,2,3,4) # tuples are immmutable
  
  l=append567(list)
  t=append567(tuple)
  
  print list
  print tuple
  print l
  print t

if __name__ == "__main__":
  main()
