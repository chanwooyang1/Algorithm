def solution(n, costs):
    costs.sort(key=lambda x : x[2])
    parent = [i for i in range(n)]
    
    def union(a,b):
        p1 = find(a)
        p2 = find(b)
    
        if p1 < p2:
            parent[p2] = p1
        else:
            parent[p1] = p2
        
    
    
    def find(x):
        if parent[x] == x:
            return x
        parent[x] = find(parent[x])
        
        return parent[x]
    
    answer = 0
    
    
    for f,t,c in costs:
        if find(f) != find(t):
            union(f,t)
            answer += c
            
            
    
            
    
    
    
    return answer