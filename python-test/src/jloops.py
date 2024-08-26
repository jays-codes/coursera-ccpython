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
  

print("sqr of each even num in an array using list comprehension")  
numbers = [1, 2, 3, 4, 5]
print(numbers)
sqr_nums = [x**2 for x in numbers if x%2==0]
print(sqr_nums)


print("run " * 8)

# demo of nested while loop
x = 0
while x < 5:
  print(x)
  x += 1
  
  input = "four score and seven years ago"
  
  print([c for c in input if c.lower() in ['a', 'e', 'i', 'o', 'u']])
  
  
# Should print: 11, 9, 7, 5, 3, 1 once the problem is fixed.
for n in range(11, -2):
  if n % 2 != 0:
    print(n, end=" ")

  for n in range(11, -2):
    if n % 2 != 0:
        print(n, end=" ")









