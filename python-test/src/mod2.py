import typing
import numpy as np

number = -4

if number > 0:
    print("Number is positive.")
elif number == 0:
    print("Number is zero.")
else:
    print("Number is negative.")
    
number = "i'm a string"

print(number + " and I know it!")

base = 6
height = 3
area = (base*height)/2
print("The area of the triangle is: " + str(area)) 

quo = 11/3
print("quo is: " + str(quo))

num_list: typing.List[int] = [1, 2, 3, 4, 5]
num_tuple: typing.Tuple[int, int, int] = (1, 2, 3)
dctnry: typing.Dict[str, int] = {"key1": 1, "key2": 2, "key3": 3}

result = np.nan_to_num(np.divide(7,0), nan=0)
print("result is: " + result)

word1 = "How"
word2 = "do"
word3 = "you"
word4 = "like"
word5 = "Python"
word6 = "so"
word7 = "far?"

print(word1 + " " + word2 + " " + word3 + " " + word4 + " " + word5 + " " + word6 + " " + word7)