# https://leedakyeong.tistory.com/entry/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EA%B5%AC%EB%AA%85%EB%B3%B4%ED%8A%B8-in-python
def solution(people, limit):
    people.sort()
    i = 0
    j = len(people) -1
    cnt = 0
    while i<=j:
        cnt += 1
        if people[i] + people[j]<=limit:
            i+=1
        j-=1
    return cnt
