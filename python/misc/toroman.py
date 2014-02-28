import sys

def to_roman(numeral, roman):
  if numeral == 0:
    return roman 
  else: 
    for n in sorted(dic.iteritems(), key = lambda x: x[0], reverse = True):
      if numeral >= n[0]:
        numeral -= n[0]
        roman += n[1]
        break;
    return to_roman(numeral, roman)
  

dic={1000:'M', 900:'CM', 500:'D', 400: 'CD', 100:'C', 90:'XC', 50:'L', 40:'XL', 10:'X', 9:'IX', 5:'V', 4:'IV', 1:'I'}

print to_roman(int(sys.argv[1]), roman)
