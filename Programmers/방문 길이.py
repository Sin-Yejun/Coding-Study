# https://velog.io/@tjdud0123/%EB%B0%A9%EB%AC%B8-%EA%B8%B8%EC%9D%B4
def solution(dirs):
    DELTA = {'U': (0, 1), 'D': (0, -1), 'R': (1, 0), 'L': (-1, 0)}
    visited = set()
    x, y = 0, 0   # position
    for command in dirs:
        dx, dy = DELTA[command]
        nx, ny = x + dx, y + dy
        go = (x, y, nx, ny)
        back = (nx, ny, x, y)
        x, y = nx, ny   # move position

    if go not in visited:
        visited.add(go)
        visited.add(back)
    print(visited)
