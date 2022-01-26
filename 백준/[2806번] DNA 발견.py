# http://codersbrunch.blogspot.com/2016/12/2806-dna.html
n = int(input())
s = input()
s = list(s)
s.append('A')
cnt = 0 
for i in range(n):
    if s[i] != s[i+1]:
        cnt += 1
        if i and s[i-1] == s[i+1]:
            cnt -= 1
            s[i] = s[i+1]
   
print(cnt)
            

