#https://enhjh.tistory.com/38
# PyPy3로 제출시 시간초과 안
# 최대값 설정
MAX=1000000

# DP 1로 초기화
dp = [1]*(MAX+1)

# S: 값 누적 리스트
s = [0]*(MAX+1)

for i in range(2, MAX+1):
    j=1
    while i*j <= MAX:
    	# i의 배수에 값 추가
        dp[i*j] += i
        j += 1

for i in range(1, MAX+1):
	# 누적 값 계산
    s[i] = s[i-1] + dp[i]

n = int(input())
ans=[]
for _ in range(n):
    a=int(input())
    ans.append(s[a])
print('\n'.join(map(str, ans))+'\n')
