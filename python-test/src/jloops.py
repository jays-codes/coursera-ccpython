for x in range(1, 5):
    print(x)
    
    
def to_celsius(x):
  return (x-32)*5/9

for x in range(0,101,10):
  print(x, to_celsius(x))