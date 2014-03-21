from collections import defaultdict
import re


with open('text.txt', 'r') as f:
  i = 0   
  for match in re.findall("\.test", f.read()):
    i+=1
  print i    
      
