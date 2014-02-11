def main():
  l = [x*2 for x in range(10)]
  print l

  d = dict((x, i) for (x,i) in enumerate(range(10)))
  print d



if __name__ == "__main__":
  main()
