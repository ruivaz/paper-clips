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
  



def permutationList(list, i):
  if i==len(list)-1:
    print list         	
  else:
    for j in range(i, len(list)):
      list[i], list[j] = list[j], list[i]
      permutation(list, i+1)
      list[j], list[i] = list[i], list[j]
  


def permutationString(string, s):
  if len(s)==len(string):
    print s
  else:
    for i in string:
      if i in s: continue
      else:
        s=s+i
        permutationString(string,s)
        s=s[0:-1]


def xorswap(l, index1, index2):
  l[index1]= l[index1]^l[index2]
  l[index2]= l[index1]^l[index2]
  l[index1]= l[index1]^l[index2]
  

def main():

  permutationString('abc','')
  #permutationList([1,2,3],0)
  

if __name__ == "__main__":
  main()
