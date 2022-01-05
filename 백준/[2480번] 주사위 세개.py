arr = list(map(int,input().split()))
dic = {}
for i in arr:
    try: dic[i] +=1
    except: dic[i] =1
dic_rev = {v:k for k, v in dic.items()}
if max(dic.values()) == 1:
    print(max(dic.keys())*100)
elif max(dic.values()) == 2:
    print(dic_rev.get(2)*100+1000)
else:
    print(dic_rev.get(3)*1000+10000)
