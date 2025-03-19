def solution(routes):
    routes = sorted(routes, key = lambda x:x[1])
    last_camera = -30001
    camera = 0
    for start, end in routes:
        if last_camera < start:
            camera += 1
            last_camera = end
    return camera