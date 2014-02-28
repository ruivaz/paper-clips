def isPalindrome(a_word):
  if len(a_word)<2:
    return True
  elif a_word[0]==a_word[-1]:
    return isPalindrome(a_word[1:-1])
  else:
    return False


print isPalindrome("assa")
