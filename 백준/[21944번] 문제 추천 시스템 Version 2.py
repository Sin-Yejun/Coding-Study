import sys
import bisect

input = sys.stdin.readline
n = int(input())

# 전체 문제를 (난이도, 문제번호) 순으로 저장하는 리스트
global_list = []

# 그룹별 문제를 저장하는 딕셔너리 (key: 그룹번호, value: 해당 그룹의 (난이도, 문제번호) 정렬 리스트)
groups = {}

# 문제 번호를 key로, (난이도, 그룹) 정보를 저장하는 딕셔너리
problem_info = {}

# 초기 문제 등록
for _ in range(n):
    P, L, G = map(int, input().split())
    problem_info[P] = (L, G)
    bisect.insort(global_list, (L, P))
    if G not in groups:
        groups[G] = []
    bisect.insort(groups[G], (L, P))

m = int(input())
output_lines = []

for _ in range(m):
    command = input().split()
    cmd = command[0]
    
    if cmd == "add":
        # add P L G
        P = int(command[1])
        L = int(command[2])
        G = int(command[3])
        problem_info[P] = (L, G)
        bisect.insort(global_list, (L, P))
        if G not in groups:
            groups[G] = []
        bisect.insort(groups[G], (L, P))
        
    elif cmd == "solved":
        # solved P
        P = int(command[1])
        L, G = problem_info[P]
        # 전역 리스트에서 삭제
        idx = bisect.bisect_left(global_list, (L, P))
        if idx < len(global_list) and global_list[idx] == (L, P):
            global_list.pop(idx)
        # 그룹 리스트에서 삭제
        idx2 = bisect.bisect_left(groups[G], (L, P))
        if idx2 < len(groups[G]) and groups[G][idx2] == (L, P):
            groups[G].pop(idx2)
        # 문제 정보 삭제
        del problem_info[P]
        
    elif cmd == "recommend":
        # recommend G x
        G = int(command[1])
        x = int(command[2])
        # x가 1이면 해당 그룹에서 가장 어려운 문제(리스트의 마지막 요소),
        # x가 -1이면 해당 그룹에서 가장 쉬운 문제(리스트의 첫 번째 요소)를 반환.
        if x == 1:
            _, P = groups[G][-1]
            output_lines.append(str(P))
        else:
            _, P = groups[G][0]
            output_lines.append(str(P))
            
    elif cmd == "recommend2":
        # recommend2 x : 전체 문제 중 추천
        x = int(command[1])
        if x == 1:
            _, P = global_list[-1]
            output_lines.append(str(P))
        else:
            _, P = global_list[0]
            output_lines.append(str(P))
            
    elif cmd == "recommend3":
        # recommend3 x L
        x = int(command[1])
        L_req = int(command[2])
        if x == 1:
            # 난이도가 L_req 이상인 문제 중 가장 쉬운 문제 찾기 (lower_bound)
            idx = bisect.bisect_left(global_list, (L_req, 0))
            if idx < len(global_list):
                _, P = global_list[idx]
                output_lines.append(str(P))
            else:
                output_lines.append(str(-1))
        else:
            # 난이도가 L_req 미만인 문제 중 가장 어려운 문제 찾기
            idx = bisect.bisect_left(global_list, (L_req, 0))
            if idx - 1 >= 0:
                _, P = global_list[idx - 1]
                output_lines.append(str(P))
            else:
                output_lines.append(str(-1))

print("\n".join(output_lines))