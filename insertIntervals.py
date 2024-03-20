def insertInterval(interval, newInterval):
    result = []
    for i in range(len(interval)):
        if newInterval[1] < interval[i][0]:
            result.append(newInterval)
            return result + interval[i:]
        elif interval[i][1] < newInterval[0]:
            result.append(interval[i])
        else:
            newInterval = [min(newInterval[0], interval[i][0]), max(newInterval[1], interval[i][1])]

    result.append(newInterval) 
    return result
    
print(insertInterval([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]))