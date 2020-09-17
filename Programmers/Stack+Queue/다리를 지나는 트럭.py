from collections import deque

def solution(bridge_length, weight, truck_weights):
    truck_weights = deque(truck_weights)
    answer, current_time, crossing_truck_weight = 0, 0, 0
    crossing_truck_list = deque([])
    while truck_weights or crossing_truck_list:
        current_time += 1
        if crossing_truck_list:
            front_truck, entry_time = crossing_truck_list[0][0], crossing_truck_list[0][1]
            if current_time - entry_time == bridge_length:
                crossing_truck_list.popleft()
                crossing_truck_weight -= front_truck
        if truck_weights:
            if crossing_truck_weight + truck_weights[0] <= weight:  # 진입이 가능할 때
                entering_truck = truck_weights.popleft()
                crossing_truck_list.append([entering_truck, current_time])
                crossing_truck_weight += entering_truck
    answer = current_time
    print(answer)
    return answer