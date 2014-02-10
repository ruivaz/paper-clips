import sys
def reverse(s):
  if s=="":
    return s
  else:
    return reverse(s[1:0])+s[0]


def sum(list):
  res=0;
  for number in list:
    res+=number
  return res   


def sum_equals(list):
  for i in range(len(list)):
    if sum(list[0:i]) == sum(list[i+1:len(list)]):
      print i


def fibonaci(number):
  if number == 0:
    return 0
  if number == 1:
    return 1
  else:
    return fibonaci(number-1) + fibonaci(number-2)
  


def main():
  print sys.argv[1]
  print fibonaci(int(sys.argv[1]))


if __name__ == "__main__":
  main()
