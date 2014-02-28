from collections import defaultdict


class ExtFile:
  def __init__(self, filename, mode):
    self.file = open(filename, mode)
    self.wordcount = defaultdict(int)

  def topwords(self, n):
    for line in self.file:
      for word in line.split():
        self.wordcount[word]+=1
    
    return sorted(self.wordcount, key=self.wordcount.get, reverse = True)[0:n]

  def __enter__(self):
    return self  

  def __exit__(self, exc_type, exc_value, traceback):
    self.file.close()

