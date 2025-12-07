rating = 0.0

print("")
rating = float(input("Star number? "))
print("")
print("===========================")
print("")
if rating > 4.5:
  print("Extraordinary!")
elif rating > 4:
  print("Excellent!")
elif rating > 3:
  print("Good!")
elif rating > 2:
  print("Fair")
else:
  print("Poor")
print("")