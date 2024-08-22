s = "w2oooooo2w"

def isPalindrome(s):
    for c in range(len(s)//2):
        if s[c] != s[-c-1]:
            return False
    return True

print(isPalindrome(s))
    
    
