# https://geonyeongkim-development.tistory.com/22
costs = [[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]
answer = 0
a_count = b_count = int(len(costs) / 2)
for cost in costs:
    cost.append(abs(cost[0]-cost[1]))
sorted_costs = sorted(costs, key = lambda x:x[2], reverse = True)


for cost in sorted_costs:
    print(cost)
    if a_count == 0:
        answer += cost[1]
        continue
    if b_count == 0:
        answer += cost[0]
        continue
    if cost[0] < cost[1]:
        a_count -= 1
        answer += cost[0]
    else:
        b_count -= 1
        answer += cost[1]
print(answer)
