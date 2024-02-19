def imageTgas(images):

    tags_with_ids = [] 

    for image_id, tags in images:
        for tag in tags:
            tags_with_ids.append((tag, image_id))

    lastDict = {}
    for char in tags_with_ids:
        id = char[0]
        image = char[1]
        if id in lastDict:
            lastDict[id].append(image)
        else:
            lastDict[id] = []
            lastDict[id].append(image)
        
    return lastDict
            


    

        
print(imageTgas([("img001", ["travel", "beach", "summer"]),
    ("img002", ["food", "italian", "pasta"]),
    ("img003", ["travel", "mountains"]),
    ("img004", ["food", "dessert"])]))