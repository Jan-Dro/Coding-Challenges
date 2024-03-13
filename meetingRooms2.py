def meetingRooms2(intervals):
    maxRooms = 0
    startTime = sorted([i[0] for i in intervals])
    endTime = sorted([j[1] for j in intervals])

    count = 0

    i, j = 0, 0

    while i < len(intervals):
        if startTime[i] < endTime[j]:
            count += 1
            i += 1
        else:
            count -= 1
            j += 1
        maxRooms = max(maxRooms, count)

    return maxRooms

print(meetingRooms2([[[5,8],[6,8]]]))