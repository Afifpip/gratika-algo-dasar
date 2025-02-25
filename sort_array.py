def sort_array(arr):
  abj = sorted([x for x in arr if isinstance(x, str)])
  num = sorted([x for x in arr if isinstance(x, (int, float))])
  return abj + num

array = [12, 9, 30, "A", "M", 99, 88, "J", "N", "B"]
sorted_list = sort_array(array)
print(sorted_list)