from collections import defaultdict

def solution(tickets):
    answer = []

    graph = defaultdict(list)
    for ticket in tickets:
        graph[ticket[0]].append(ticket[1])
    for key in graph:
        graph[key].sort()
    
    def dfs(destination, routes, depth):
        
        if depth == len(tickets):
            return True
        for i in range(len(graph[destination])):
            next_destination = graph[destination].pop(i)
            routes.append(next_destination)
            if dfs(next_destination, routes, depth + 1):
                return True
           
          
            graph[destination].insert(i,next_destination)
            routes.pop()
        return False
            
    routes = []
    routes.append("ICN")
    dfs("ICN", routes, 0)
    
    
    
    return routes