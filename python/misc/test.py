def reverse(string):
  new_str=''
  for i in range(len(string)):
    new_str+=string[len(string)-1-i] 
  return new_str

def reverse1(string):
  if len(string)==1:
    return string
  return reverse1(string[1:]) + string[0:1] 

string = 'Hello World'
print reverse1(string)
