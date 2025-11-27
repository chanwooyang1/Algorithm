import math
def time_to_minutes(s_time):
    time, minutes = map(int, s_time.split(":"))
    return time * 60 + minutes

def calculate_fee(fees, in_time, out_time):
    if len(in_time) != len(out_time):
        out_time.append(time_to_minutes("23:59"))
    total_park_time = 0
    for i in range(len(in_time)):
        total_park_time += out_time[i] - in_time[i]
        
    if total_park_time <= fees[0]:
        return fees[1]
    else:
        fee = fees[1] + math.ceil((total_park_time - fees[0]) / fees[2]) * fees[3]
        return fee
 
def solution(fees, records):
    answer = []
    cars = {}
    
    for record in records:
        time, car_num, direction = record.split()
        minutes = time_to_minutes(time)
        if car_num in cars:
            if direction == "IN":
                cars.get(car_num)[0].append(minutes)
            else:
                cars.get(car_num)[1].append(minutes)
        else:
            cars[car_num] = [[minutes],[]]    
    
    sorted_cars = {key: cars[key] for key in sorted(cars)}
    for car_num, history in sorted_cars.items():
        total_fee = calculate_fee(fees, history[0], history[1])
        answer.append(total_fee)
    
    
    return answer