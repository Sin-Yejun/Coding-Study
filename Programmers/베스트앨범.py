from collections import defaultdict
def solution(genres, plays):
    index = [i for i in range(len(plays))]
    d = defaultdict(int)
    alls = []
    for i, g, p in zip(index ,genres, plays):
        alls.append((i, g, p))
        d[g] += p
    d = dict(sorted(d.items(), key=lambda x:x[1], reverse=True))
    genre_order = defaultdict(int)
    i = 0
    for key in d.keys():
        genre_order[key] = i
        i += 1
    alls = sorted(alls, key= lambda x: (genre_order[x[1]], -x[2]))
    genres_count = 0
    prev_genre = ''
    answer = []
    for i, g, p in alls:
        if not prev_genre:
            genres_count += 1
            prev_genre = g
            answer.append(i)
            continue
        if prev_genre == g:
            if genres_count < 2:
                genres_count += 1
                answer.append(i)
            else:
                continue
        else:
            genres_count = 1
            prev_genre = g
            answer.append(i)
    return answer