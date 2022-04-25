def solution(numbers, hand):
    pad = {
        1:[0,0], 2:[0,1], 3:[0,2],
        4:[1,0], 5:[1,1], 6:[1,2],
        7:[2,0], 8:[2,1], 9:[2,2],
        '*':[3,0], 0:[3,1], '#':[3,2]
    }
    left = '*'
    right = '#'
    result = ''
    left_distance = 0
    right_distance = 0
    for i in numbers:
        if i in [1,4,7]:
            left = i
            result += 'L'
        elif i in [3,6,9]:
            right = i
            result += 'R'
        else:
            left_distance = abs(pad[i][0]-pad[left][0]) + abs(pad[i][1]-pad[left][1])
            right_distance = abs(pad[i][0]-pad[right][0]) + abs(pad[i][1]-pad[right][1])
            if left_distance < right_distance:
                left = i
                result += 'L'
            elif left_distance > right_distance:
                right = i
                result += 'R'
            else:
                if hand == 'left':
                    left = i
                    result += 'L'
                else:
                    right = i
                    result += 'R'
    return result
            
