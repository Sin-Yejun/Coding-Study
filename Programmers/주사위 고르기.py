from itertools import combinations, product
from bisect import bisect_right

def solution(dice):
    n = len(dice) // 2
    alls = []
    
    # 모든 조합을 고려 (주사위를 n개씩 나누는 방법)
    for indices in combinations(range(len(dice)), n):
        A = [dice[i] for i in indices]
        B = [dice[i] for i in range(len(dice)) if i not in indices]
        
        # A vs B 승리 확률 계산 (이전보다 최적화된 함수 사용)
        win_rate = optimized_caculation(A, B)
        
        alls.append((win_rate, sorted(indices)))  # 인덱스 정렬 (출력 통일)

    # 승리 확률이 가장 높은 경우 반환
    alls.sort(key=lambda x: x[0], reverse=True)
    return [i + 1 for i in alls[0][1]]  # 1-based index로 변환

def optimized_caculation(A, B):
    temp_A = sorted(sum(combination) for combination in product(*A))
    temp_B = sorted(sum(combination) for combination in product(*B))  # 정렬

    # A가 이기는 횟수 계산 (Binary Search 활용)
    A_wins = sum(bisect_right(temp_B, a - 1) for a in temp_A)  # O(N log N)
    total = len(temp_A) * len(temp_B)  # 전체 경우의 수

    return A_wins / total
