from collections import defaultdict
import math
def time_to_min(time):
    hour, minutes = map(int, time.split(":"))
    return hour * 60 + minutes



def solution(fees, records):
    answer = []
    df_time, df_won, st_time, st_won = fees
    
    in_storage = {}
    total_duration = defaultdict(int)
    
    for rcd in records:
        time_str, car_id, status = rcd.split()
        time = time_to_min(time_str)
        
        if status == "IN":
            in_storage[car_id] = time
        else:
            total_duration[car_id] += time - in_storage.pop(car_id)
    
    end_time = time_to_min("23:59")
    for car_id, in_time in in_storage.items():
        total_duration[car_id] += end_time - in_time
        
    
    for car_id in sorted(total_duration.keys()):
        total_time = total_duration[car_id]
        
        if total_time <= df_time:
            fee = df_won
        else:
            fee = df_won + math.ceil((total_time - df_time) / st_time) * st_won
        answer.append(fee)
    
    
    
    return answer