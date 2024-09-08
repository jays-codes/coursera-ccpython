s = "w2oooooo2w"

def isPalindrome(s):
    # Remove all whitespace from the string
    s = ''.join(s.split())
    for c in range(len(s)//2):
        if s[c] != s[-c-1]:
            return False
    return True

#print(isPalindrome(s))
print(isPalindrome("Never Odd or Even")) # Should be True
print(isPalindrome("abc")) # Should be False
print(isPalindrome("kayak")) # Should be True

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
    
                