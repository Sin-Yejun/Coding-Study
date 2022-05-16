def solution(fees, records):
    normal_time = fees[0]
    normal_fee = fees[1]
    added_time = fees[2]
    added_fee = fees[3]
    
    dic = {}
    dic_count = {}
    for record in records:
        temp_arr = record.split()
        time = temp_arr[0]
        car_num = temp_arr[1]
        info = temp_arr[2]
        
        time_arr = time.split(':')
        time2minutes = int(time_arr[0])*60 + int(time_arr[1])
        if car_num not in dic:
            dic[car_num] = -time2minutes
            dic_count[car_num] = 1
        else:
            if info == 'OUT':
                dic[car_num] += time2minutes
                dic_count[car_num] = 0
            else:
                dic[car_num] -= time2minutes
                dic_count[car_num] = 1
    
    for num in dic_count.keys():
        if dic_count[num] == 1:
            dic[num] += 1439
    sorted_dic = sorted(dic.items())
    results = []
    for num, tim in sorted_dic:
        if tim <= normal_time:
            results.append(normal_fee)
        else:
            temp = normal_fee
            tim -= normal_time
            if tim % added_time == 0:
                temp += (tim // added_time)*added_fee
            else:
                temp += (tim // added_time +1)*added_fee
            results.append(temp)
    return results
            
    
