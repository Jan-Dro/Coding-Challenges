def subDomain(s):
    for word in s:
        newString = word.split(' ')
    number = newString[0]
    newString.pop(0)
    domain = '.'.join(newString) 
    subdomains = domain.split('.')
    
    answer = []
    for i in range(len(subdomains)):
        subdomain = '.'.join(subdomains[i:])
        answer.append(number + ' ' + subdomain)

    return answer

            
print(subDomain(['9001 discuss.leetcode.com']))
