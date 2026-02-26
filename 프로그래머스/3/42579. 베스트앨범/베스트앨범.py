from collections import defaultdict

def count_total(song_list): # 장르당 총 횟수 list-> int
    total_count = 0
    for idx, count in song_list:
        total_count += count
    return total_count

def solution(genres, plays):
    answer = []
    songs = defaultdict(list)
    
    for idx, (genre, play) in enumerate(zip(genres, plays)):
        songs[genre].append((idx, play))
    
    
    genre_order = sorted(((sum(play for _, play in lst), genre) for genre, lst in songs.items()), reverse = True)
   
    for _, genre in genre_order:
        genre_list = songs[genre]
        genre_list.sort(key=lambda x : (-x[1], x[0]))
        answer.extend([idx for idx, _ in genre_list[:2]])
        
        # if len(genre_list) == 1:
        #     answer.append(genre_list[0][0])
        #     continue
        # genre_list.sort(key = lambda x: (-x[1], x[0]))
        
        # for i in range(2):
        #     answer.append(genre_list[i][0])
   
    return answer