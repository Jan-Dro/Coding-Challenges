
def accountsMerge(accounts):
    listDict = {}

    for account in accounts:
        name = account[0]
        email = account[1:]

        if name in listDict:
            listDict[name].extend(email)
        else:
            listDict[name] = email

    print(listDict)
    for name in listDict:
        listDict[name] = list(set(listDict[name]))


    print(listDict)
    


print(accountsMerge([["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]))