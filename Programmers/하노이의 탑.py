def hanoi(n, from_pos, to_pos, aux_pos):
    if n == 1:
        print(from_pos,'->',to_pos)
        return
    hanoi(n-1, from_pos, aux_pos, to_pos)
    print(from_pos,'->',to_pos)
    hanoi(n-1, aux_pos, to_pos, from_pos)
def solution(n):
    def hanoi(n, from_pos, to_pos, aux_pos):
        if n == 1:
            answer.append([from_pos,to_pos])
            return
        hanoi(n-1, from_pos, aux_pos, to_pos)
        answer.append([from_pos,to_pos])
        hanoi(n-1, aux_pos, to_pos, from_pos)

    answer = []
    hanoi(n,1,3,2)
    return answer
