from itertools import combinations
def solution(orders, course):
    recipe_dict = {}
    for i in orders:
        i = sorted(list(i))
        for j in range(2,len(i)+1):
            for com in combinations(i,j):
                tmp = ''.join(com)
                if tmp in recipe_dict:
                    recipe_dict[tmp] += 1
                else:
                    recipe_dict[tmp] = 1
    result = []
    for i in course:
        temp = []
        for key, val in recipe_dict.items():
            if len(key) == i and val > 1:
                temp.append((key, val))
        if temp:
            for key, val in temp:
                if val == max(temp,key= lambda x : x[1])[1]:
                    result.append(key)
    result.sort()
    return result
