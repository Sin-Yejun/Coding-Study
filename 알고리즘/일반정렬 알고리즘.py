# 버블 정렬 O(n²)
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# 선택 정렬 O(n²)
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# 삽입 정렬 O(n²)
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Merge Sort (합병 정렬) O(n log n)
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    sorted_arr = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_arr.append(left[i])
            i += 1
        else:
            sorted_arr.append(right[j])
            j += 1

    sorted_arr.extend(left[i:])
    sorted_arr.extend(right[j:])
    return sorted_arr

# 힙 정렬 O(n log n)
import heapq

def heap_sort(arr):
    heapq.heapify(arr)  # 최소 힙 생성
    return [heapq.heappop(arr) for _ in range(len(arr))]

# 퀵 정렬 O(n log n)
def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


# 예제 실행
print(bubble_sort([64, 34, 25, 12, 22, 11, 90]))
print(selection_sort([64, 34, 25, 12, 22, 11, 90]))
print(insertion_sort([64, 34, 25, 12, 22, 11, 90]))
print(merge_sort([64, 34, 25, 12, 22, 11, 90]))
print(heap_sort([64, 34, 25, 12, 22, 11, 90]))
print(quick_sort([64, 34, 25, 12, 22, 11, 90]))


'''
    📌 특징 정리

    Bubble Sort / Selection Sort / Insertion Sort → 간단하지만 비효율적 (O(n²))

    Merge Sort / Heap Sort / Quick Sort → O(n log n) 성능으로 대규모 데이터 정렬 가능

    Quick Sort는 평균적으로 빠르지만, 최악의 경우 O(n²) 발생 가능

    Merge Sort는 안정적이지만 추가 공간이 필요

    ✅ 가장 일반적으로 사용되는 정렬 알고리즘: 퀵 정렬(Quick Sort)'

'''