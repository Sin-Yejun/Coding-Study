def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        temp_array = array
        start = commands[i][0]
        end = commands[i][1]
        index = commands[i][2]
        temp_array = temp_array[start-1:end]
        temp_array.sort()
        answer.append(temp_array[index-1])
    return answer
        
            
