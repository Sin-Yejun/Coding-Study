import sys
input = sys.stdin.readline
N, M = map(int, input().split())
pack = []
piece = []

for _ in range(M):
    a, b = map(int,input().split())
    pack.append(a)
    piece.append(b)

min_pack = min(pack)
min_piece = min(piece)

com1 = (N//6+1) * min_pack
com2 = N*min_piece
com3 = (N//6)*min_pack + (N- N//6*6)*min_piece
compare = [com1, com2, com3]
print(min(compare))
    
