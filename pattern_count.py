def pattern_count(txt, ptrn):
  count = 0
  for i in range(len(txt) - len(ptrn) + 1):
    if txt[i:i+len(ptrn)] == ptrn:
      count += 1
  return count

print(pattern_count("plindrom", "ind"))
print(pattern_count("abakadabra", "ab"))
print(pattern_count("hello", " "))
print(pattern_count("ababab", "aba"))
print(pattern_count("aaaaaa", "aa"))
print(pattern_count("hell", "hello"))