def getSum(a, b):
    print("Sum is: " + str(a+b))
    print("type of a: " + str(type(a)))
    print("type of b: " + str(type(b)))
    
    
getSum(3, 4)

print(type("This is a string"))

random_numbers = [11, 2244, 323, 4, 57]
print(random_numbers)

sorted_numbers = sorted(random_numbers)
print(sorted_numbers, random_numbers)

print(max(random_numbers))
print(min(random_numbers))


def convert_seconds(seconds):
    hours = seconds // 3600
    minutes = (seconds - hours * 3600) // 60
    remaining_seconds = seconds - hours * 3600 - minutes * 60
    return hours, minutes, remaining_seconds
 
hours, minutes, seconds = convert_seconds(5000)
print(hours, minutes, seconds)


def getSum2(a, b):
    print("2type of a: " + str(type(a)))
    print("2type of b: " + str(type(b)))
    atype = type(a)
    return a + b, atype

sum, type = getSum2(3, 4)
print("Sum2 is: " + str(sum) 
      + " and type is: " + str(type))

print(getSum(3, 4))

print("ans: " + str((2**2) == 4))

number=10

if number > 11: 
  print(0)
elif number != 10:
  print(1)
elif number >= 20 or number < 12:
  print(2)
else:
  print(3)
  
print(10%3)
print(4095%4096)


number = 4
if number * 4 < 15:
 print(number / 4)
elif number < 5:
 print(number + 3)
else:
 print(number * 2 % 5)
 
def greater_value(x, y):
    if x > y:
        return x
    else:
       return y


print(greater_value(10,3*5))

x = 5*2

print((10 != x) or (10 > x))