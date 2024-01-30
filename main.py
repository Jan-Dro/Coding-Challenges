
def isPalindrome(s):
    
    cleanString = [i for i in s if i.isalnum()]
    cleanString = ''.join(cleanString)
    cleanString = cleanString.lower()

    if cleanString == cleanString[::-1]:
        return True
    else:
        return False
        

    

print(isPalindrome("A man, a plan, a canal: Panama"))
