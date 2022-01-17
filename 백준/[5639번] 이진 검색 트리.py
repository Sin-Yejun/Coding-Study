import sys
sys.setrecursionlimit(10 ** 9)
preorder = []
while True:
    try:
        preorder.append(int(sys.stdin.readline()))
    except:
        break
postorder = []

def postorderset(preorder, left, right):
    if left > right:
        return
    root = preorder[left]
    ls = left + 1
    re = right
    rs = right + 1
    for i in range(right - left + 1):
        if i == 0:
            continue
        if preorder[left + i] > root:
            rs = i + left # 루트보다 첫번째로 커지는 수를 오른쪽 프리오더의 시작으로 정해준다
            break
    le = rs - 1
    postorderset(preorder, ls, le) # 왼쪽 프리오더 순환
    postorderset(preorder, rs, re) # 오른쪽 프리오더 순환
    postorder.append(root) # root를 preorder 리스트에 추가


postorderset(preorder, 0, len(preorder) - 1)
for i in postorder:
    print(i)

# 출처: https://ca.ramel.be/115 [MemoLOG]
