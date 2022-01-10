# https://jinho-study.tistory.com/1060
li = ["baby", "sukhwan", "tururu", "turu", "very", "cute", "tururu", 
      "turu", "in", "bed", "tururu", "turu", "baby", "sukhwan"]
N = int(input())-1
k = N//14
if N%14 in [3, 7, 11]:
    print(f"tu+ru*{k+1}" if k >= 4 else "turu"+"ru"*k)    
elif N%14 in [2, 6, 10]:
    print(f"tu+ru*{k+2}" if k >= 3 else "tururu"+"ru"*k)    
else:
    print(li[N%14])
