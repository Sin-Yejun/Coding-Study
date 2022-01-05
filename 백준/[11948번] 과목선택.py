a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())

s1 = [a,b,c,d]
s2 = [e,f]

s1.remove(min(s1))

print(sum(s1)+max(s2))
