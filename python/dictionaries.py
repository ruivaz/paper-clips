mydict = {1: 10, 3:22, 4:18, 2:32}


for element in sorted(mydict.iteritems(), key = lambda item: item[0]):
  print element
