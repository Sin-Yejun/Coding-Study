from collections import Counter

c1 = Counter("abcaa")
c2 = Counter("aabb")

print(c1, c2)
print(c1 + c2)  # 합집합처럼 누적
print(c2 - c1)  # 빼기 (음수는 제거됨)
