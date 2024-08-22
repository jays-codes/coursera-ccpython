for x in range(1, 5):
    print(x)
    
    
def to_celsius(x):
  return (x-32)*5/9

for x in range(0,101,10):
  print(x, to_celsius(x))
  
for left in range(7):
  for right in range(left, 7):
    print("inner loop:[" + str(left) +"|"+ str(right)+"]")
  print()
  
teams = ["Barcelona", "Real Madrid", "Bayern Munich", "Manchester United", "Juventus"]
for home in teams:
  for away in teams:
    if home != away:
      print(home + " vs " + away)
      
for c in "Hello":
  print(c)