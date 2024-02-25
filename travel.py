from collections import defaultdict, deque

def travel(n, flights, src, dst, k):
    graph = defaultdict(list)
    for flight in flights:
        source, destination, cost = flight
        graph[source].append((destination, cost))

    print(graph)

    queue = deque([(src, 0, 0)]) 
    print(queue)
    
    while queue:
        current_city, total_cost, stops = queue.popleft()
        
        if current_city == dst:
            return total_cost
        
        if stops > k:
            continue
        
        for neighbor, cost in graph[current_city]:
            queue.append((neighbor, total_cost + cost, stops + 1))
            print(queue)
    
    return -1
    

print(travel(4, [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], 0, 3, 1))