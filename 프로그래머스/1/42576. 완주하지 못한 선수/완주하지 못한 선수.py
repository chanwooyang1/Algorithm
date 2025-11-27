def solution(participant, completion):
    answer = ''
    partimap = {}
    for part in participant:
        partimap[part] = partimap.get(part, 0) + 1
    for comp in completion:
        partimap[comp] = partimap.get(comp) - 1
    
    answer = max(partimap, key=partimap.get)
    return answer