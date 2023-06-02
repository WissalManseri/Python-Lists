thislist = ["apple", "banana", "cherry"]
print(thislist)

print(thislist[1])

thislist[1] = "blackcurrant"
print(thislist)

for x in thislist:
  print(x)

if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")
  print(len(thislist))

thislist.append("orange")
print(thislist)

thislist.insert(1, "orange")
print(thislist)

thislist.remove("banana")
print(thislist)

thislist.pop()
print(thislist)

del thislist[0]
print(thislist)

thislist.clear()
print(thislist)


