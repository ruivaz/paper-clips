def palindrome(a_word):
  if len(a_word)<=1:
    return True
  elif a_word[0]==a_word[-1]:
    return palindrome(a_word[1:-1])
  else:
    return False


print palindrome("HaaH")
print palindrome("baaaaaab")
print palindrome("aghhhgb")
