def solution(cookie):
    max_value = 0
    for i in range(len(cookie)-1):
        # 분기점을 만들 수 있는 모든 경우의 수를 확인한다.
        # 맨 뒤에서부터, 앞부분의 합을 front / 뒷부분의 합을 end로 정의한다.
        front_value, front_idx = cookie[i], i
        end_value, end_idx = cookie[i+1], i+1
        while True:
            # 앞부분의 합 == 뒷부분의 합, 이전의 max 값보다 클 경우 max_value 업데이트
            if front_value == end_value and front_value > max_value:
                max_value = front_value
            # 앞부분의 값이 뒷부분보다 작을 경우, 앞부분의 element 추가
            if front_idx > 0 and front_value <= end_value:
                front_idx -= 1
                front_value += cookie[front_idx] 
            # 뒷부분의 값이 앞부분보다 작을 경우 뒷부분의 element 추가
            elif end_idx < len(cookie)-1 and front_value >= end_value:
                end_idx += 1
                end_value += cookie[end_idx]
            else:
                break
    return max_value
