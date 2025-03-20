from heapq import heappush, heappop
jobs = [[0, 3], [1, 9], [3, 5]]
jobs.sort()
q = []
answer = 0
time = 0
wait_time = 0
compelete = 0
i = 0

while compelete < len(jobs):

    while i < len(jobs) and jobs[i][0] <= time:
        heappush(q, (jobs[i][1], jobs[i][0]))
        i += 1
    
    if q:
        job_time, start = heappop(q)
        time += job_time
        wait_time += time - start
        compelete += 1
    else:
        time = jobs[i][0]
print(wait_time//len(jobs))