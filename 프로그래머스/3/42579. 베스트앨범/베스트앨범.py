from collections import defaultdict

def count_total(song_list): # 장르당 총 횟수 list-> int
    total_count = 0
    for idx, count in song_list:
        total_count += count
    return total_count

def solution(genres, plays):
    answer = []
    songs = defaultdict(list)
    idx = 0
    
    for genre, play in zip(genres, plays):
        songs[genre].append((idx, play))
        idx += 1
        
    song_with_count = []
    for key, value in songs.items():
        count = count_total(value)
        song_with_count.append((count, key)) 
    song_with_count.sort(reverse = True)
    
    for count, genre in song_with_count:
        genre_list = songs[genre]
        if len(genre_list) == 1:
            answer.append(genre_list.pop()[0])
            continue
        genre_list.sort(key = lambda x: (-x[1], x[0]))
        
        for i in range(2):
            answer.append(genre_list[i][0])
   
    return answer