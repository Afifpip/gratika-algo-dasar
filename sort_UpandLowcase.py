def sort_uplowcase(txt):
  freq = {}
  for abj in txt:
    if abj.isalpha():
      if abj in freq:
        freq[abj] += 1
      else:
        freq[abj] = 1
  
  sorted_list = dict(sorted(freq.items()))
  return sorted_list

print(sort_uplowcase("Hello World"))
print(sort_uplowcase("Bismillah"))
print(sort_uplowcase("MasyaAllah"))