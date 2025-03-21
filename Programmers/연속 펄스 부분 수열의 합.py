def solution(sequence):
    # [-1, 1, -1 , ...] 펄스 시퀀스1
    seq1 = [sequence[i] if i % 2 == 0 else -sequence[i] for i in range(len(sequence))]

    # [1, -1, 1 , ...] 펄스 시퀀스2
    seq2 = [sequence[i] if i % 2 == 1 else -sequence[i] for i in range(len(sequence))]

    n = len(sequence)
    dp1 = [0] * n
    dp2 = [0] * n
    # 최대 연속합 찾기
    for i in range(len(sequence)):
        dp1[i] = max(seq1[i], dp1[i-1]+seq1[i])
        dp2[i] = max(seq2[i], dp2[i-1]+seq2[i])

    return max(max(dp1), max(dp2))