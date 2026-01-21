def solution(n, costs):
    answer = 0
    costs.sort(key=lambda x : x[2])
    parents = [i for i in range(n)]
    
    
    def union(a, b):
        if a < b:
            parents[b] = a
        else:
            parents[a] = b
    
    def find(x):
        if parents[x] == x:
            return x
        parents[x] = find(parents[x])
        return parents[x]
    
    for f, t, c in costs:
        root_f = find(f)
        root_t = find(t)
        
        if root_f != root_t:
            union(root_f, root_t)
            answer += c
    
            
            
        
    return answer