def changecode(music_): 
    music_ = music_.replace('C#', 'c')
    music_ = music_.replace('D#', 'd')
    music_ = music_.replace('F#', 'f')
    music_ = music_.replace('G#', 'g')
    music_ = music_.replace('A#', 'a')    
    return music_

def solution(m, musicinfos):
    m = changecode(m)
    arr = []
    for music in musicinfos:
        tmp = music.split(',')
        start_time = int(tmp[0][:2])*60 + int(tmp[0][3:5])
        finish_time = int(tmp[1][:2])*60 + int(tmp[1][3:5])
        time = finish_time - start_time
        tmp[3] = changecode(tmp[3])
        arr.append([time, tmp[2], tmp[3]])
    arr.sort(key = lambda x:-x[0])
    
        
    for time, name, info in arr:
        temp = ''
        cnt = 0
        for j in range(time):
            temp += info[cnt]
            cnt += 1
            if cnt == len(info):
                cnt = 0
        if m in temp:
            return name
        
    return "(None)"
