def reverse(sequence):
  if len(sequence)==1:
    return sequence
  else:
    return reverse(sequence[1:]) + sequence[0]

print reverse("Hello")
