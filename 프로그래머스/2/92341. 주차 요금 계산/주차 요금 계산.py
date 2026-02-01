from collections import defaultdict
import math
def time_to_min(time):
    hour, minutes = time.split(":")
    return int(hour) * 60 + int(minutes)


def solution(fees, records):
    answer = []
    car_records = defaultdict(lambda: defaultdict(list))
    df_time, df_won, st_time, st_won = fees[0], fees[1], fees[2], fees[3]
    
    for r in records:
        time,car_id, direction = r.split()
        time_in_min = time_to_min(time)
        if direction == "IN":
            car_records[car_id]["in_out_record"].append(time_in_min)
        else:
            tim = car_records[car_id]["in_out_record"].pop()
            result = time_in_min - tim
            car_records[car_id]["bills"].append(result)
    for i in car_records.values():
        bills = i["bills"]
        
        if i["in_out_record"]:
            bills.append(time_to_min("23:59") - i["in_out_record"].pop())
        total_time = sum(bills)
        if total_time <= df_time:
            
            i["total_fee"] = df_won
            continue
        else:
            i["total_fee"] = df_won + math.ceil((total_time - df_time)/ st_time) * st_won
            
    for car_id, record in sorted(car_records.items()):
        answer.append(record["total_fee"])
                
        
           
    return answer