from filepp import ExtFile

with ExtFile("text.txt", "r") as f:
  for word in f.topwords(10):
    print word, f.wordcount[word]
