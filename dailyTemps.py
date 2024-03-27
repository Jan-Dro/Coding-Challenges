def dailyTemps(temps):
    tempArr = [] 
    
    for i in range(len(temps)):
        count = 0  
        foundWarmer = False 
        for j in range(i + 1, len(temps)):
            count += 1 
            if temps[i] < temps[j]:
                tempArr.append(count)  
                foundWarmer = True 
                break 
        
        if not foundWarmer:
            tempArr.append(0) 

    return tempArr



print(dailyTemps([73,74,75,71,69,72,76,73]))
