from collections import defaultdict
def solution(tickets):
    answer = []
    routes = defaultdict(list)
    for ticket in tickets:
        routes[ticket[0]].append(ticket[1])
    
    for key in routes.keys():
        routes[key].sort(reverse=True)
    
    stack = ['ICN']
    while stack:
        temp = stack[-1]
        if not routes[temp]:
            answer.append(stack.pop())
        else:
            stack.append(routes[temp].pop())
    answer.reverse()
    return answer
