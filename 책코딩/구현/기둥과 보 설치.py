def possible(answer):
    for x, y, a in answer:
        if a == 0:  # 기둥
            # 바닥 위에 있거나, 보의 한쪽 끝부분 위에 있거나, 다른 기둥 위에 있어야 설치 가능
            if y == 0 or [x, y-1, 0] in answer or [x-1, y, 1] in answer or [x, y, 1] in answer:
                continue
            return False
        else:  # 보
            # 한쪽 끝이 기둥 위에 있거나, 양쪽 끝이 다른 보와 연결되어 있어야 설치 가능
            if [x, y-1, 0] in answer or [x+1, y-1, 0] in answer or ([x-1, y, 1] in answer and [x+1, y, 1] in answer):
                continue
            return False
    return True

def solution(n, build_frame):
    answer = []
    
    for x, y, a, b in build_frame:
        if b == 1:  # 설치
            answer.append([x, y, a])
            if not possible(answer):  # 설치 불가능하면 되돌리기
                answer.remove([x, y, a])
        else:  # 삭제
            answer.remove([x, y, a])
            if not possible(answer):  # 삭제 불가능하면 되돌리기
                answer.append([x, y, a])
    
    return sorted(answer)  # 정렬하여 반환
