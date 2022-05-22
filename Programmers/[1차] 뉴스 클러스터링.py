import re
import math

def solution(str1, str2):
    # 두칸씩 쪼갠 값이 모두 문자이면 str1, str2에 append 
    str1 = [str1[i:i+2].lower() for i in range(0, len(str1)-1) if not re.findall('[^a-zA-Z]+', str1[i:i+2])]
    str2 = [str2[i:i+2].lower() for i in range(0, len(str2)-1) if not re.findall('[^a-zA-Z]+', str2[i:i+2])]

    # 합집합과 교집합 계산 
    gyo = set(str1) & set(str2)
    hap = set(str1) | set(str2)

    # 합집합이 0이면 65536 출력 
    if len(hap) == 0 :
        return 65536

    # 교집합하고 합집합의 counter를 따로 계산
    gyo_sum = sum([min(str1.count(gg), str2.count(gg)) for gg in gyo])
    hap_sum = sum([max(str1.count(hh), str2.count(hh)) for hh in hap])

    return math.floor((gyo_sum/hap_sum)*65536)
