def solution(n, stations, w):
    answer = 0
    coverage = 2 * w + 1  # 기지국이 커버하는 범위
    
    start = 1  # 첫 번째 아파트부터 시작
    for station in stations:
        left = station - w  # 현재 기지국이 커버하는 왼쪽 경계
        if start < left:  # 전파가 닿지 않는 사각지대가 존재할 경우
            length = left - start  # 사각지대 길이
            answer += (length + coverage - 1) // coverage  # 최소한의 기지국 개수 계산
        start = station + w + 1  # 다음 사각지대의 시작 위치 업데이트
    
    # 마지막 기지국 이후에도 사각지대가 있는 경우 처리
    if start <= n:
        length = n - start + 1
        answer += (length + coverage - 1) // coverage
    
    return answer
