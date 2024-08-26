s = "w2oooooo2w"

def isPalindrome(s):
    for c in range(len(s)//2):
        if s[c] != s[-c-1]:
            return False
    return True

print(isPalindrome(s))
    

str = ["Hi", "Jay"]
print("|".join(str))

phonenum = "4167223428"

line = phonenum[-4:]
print(line)

str = "Hello"
for x in str:
    print(x)
    
for number in range(1, 6+1, 2):
    print(number * 3)
    
