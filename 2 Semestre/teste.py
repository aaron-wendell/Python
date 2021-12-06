def print_mode (thelist):
  counts = {}
  for item in thelist:
    counts [item] = counts.get (item, 0) + 1
  maxcount = 0
  maxitem = None
  for k, v in counts.items ():
    if v > maxcount:
      maxitem = k
      maxcount = v
  if maxcount == 1:
    print("All values only appear once")
  elif counts.values().count (maxcount) > 1:
    print ("List has multiple modes")
  else:
    print ("Mode of list:", maxitem)

vet = []
for i in range(4):
    x = int(input('Digita o valor'))
    vet.append(x)
print_mode(x)