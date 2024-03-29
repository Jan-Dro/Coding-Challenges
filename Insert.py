def insert(intervals, newInterval):
    result = []
    i = 0
    
    while i < len(intervals) and intervals[i][1] < newInterval[0]:
        result.append(intervals[i])
        i += 1

    while i < len(intervals) and intervals[i][0] <= newInterval[1]:
        newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
        i += 1

    result.append(newInterval)

    while i < len(intervals):
        result.append(intervals[i])
        i += 1

    return result

print(insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]))