def draw_stars(n, x, y, stars):
    if n == 3:
        stars[y][x] = '*'
        stars[y+1][x-1] = stars[y+1][x+1] = '*'
        for i in range(-2, 3):
            stars[y+2][x+i] = '*'
    else:
        draw_stars(n//2, x, y, stars)
        draw_stars(n//2, x-(n//2), y+(n//2), stars)
        draw_stars(n//2, x+(n//2), y+(n//2), stars)

def print_stars(stars):
    for row in stars:
        print(''.join(row))

n = int(input())

# 빈 공간으로 초기화된 별 찍기 배열 생성
stars = [[' ']*(2*n-1) for _ in range(n)]

draw_stars(n, n-1, 0, stars)
print_stars(stars)
