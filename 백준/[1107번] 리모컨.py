# https://javaiyagi.tistory.com/585
# 희망 채널
N = int(input())

# 고장난 버튼 수
M = int(input())

#0~9 까지 버튼이 있는 리모컨
remote = {str(i) for i in range(10)}

#고장난 버튼 제거
if M > 0:
    remote -= set(map(str,input().split()))
    
#현재 보고 있는 채널
current = 100

answer = abs(current - N)

for channel in range(1000000):
    # 채널 각 숫자리 순회
    for j in range(len(str(channel))):
        # 누를 수 없는 버튼이라면 pass
        if str(channel)[j] not in remote:
            break
        elif len(str(channel)) - 1 == j:
                   answer = min(answer, abs(channel-N) + len(str(channel)))

print(answer)



