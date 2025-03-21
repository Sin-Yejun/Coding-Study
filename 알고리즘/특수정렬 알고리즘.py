# 계수 정렬
def counting_sort(arr):
    if not arr:
        return []

    max_val = max(arr)
    count = [0] * (max_val + 1)

    # 각 숫자의 개수를 센다
    for num in arr:
        count[num] += 1

    # 결과 정렬 배열 생성
    result = []
    for i in range(len(count)):
        result.extend([i] * count[i])

    return result

# 예제 실행
print(counting_sort([4, 2, 2, 8, 3, 3, 1]))


# 기수 정렬
def counting_sort_for_radix(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10  # 자릿수는 0~9

    # 현재 자릿수 기준으로 개수 세기
    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1

    # 누적합을 구해서 위치 계산
    for i in range(1, 10):
        count[i] += count[i - 1]

    # 출력 배열에 값 채우기 (뒤에서부터 해야 안정 정렬 유지됨)
    for i in reversed(range(n)):
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1

    # 원래 배열에 복사
    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    if not arr:
        return []

    max_val = max(arr)
    exp = 1
    while max_val // exp > 0:
        counting_sort_for_radix(arr, exp)
        exp *= 10

    return arr

# 예제 실행
print(radix_sort([170, 45, 75, 90, 802, 24, 2, 66]))

# 문자열용 Radix Sort (LSD 방식)
from collections import defaultdict

def counting_sort_strings(arr, index, max_length):
    buckets = defaultdict(list)  # 각 문자에 대한 버킷
    fill_char = ""  # 빈 문자열은 가장 앞에 와야 하므로 공백 문자로 패딩

    for word in arr:
        char = word[-(index + 1)] if index < len(word) else fill_char  # 해당 자리 문자 가져오기
        buckets[char].append(word)

    # 버킷을 사전순으로 정렬하여 반환
    sorted_arr = []
    for key in sorted(buckets.keys()):
        sorted_arr.extend(buckets[key])
    
    return sorted_arr

def radix_sort_strings(arr):
    if not arr:
        return []

    max_length = max(len(word) for word in arr)  # 가장 긴 문자열 길이 구하기
    
    # 자릿수별로 Counting Sort 수행
    for i in range(max_length):
        arr = counting_sort_strings(arr, i, max_length)

    return arr

# 예제 실행
words = ["banana", "apple", "orange", "grape", "kiwi", "melon", "berry"]
sorted_words = radix_sort_strings(words)
print(sorted_words)
