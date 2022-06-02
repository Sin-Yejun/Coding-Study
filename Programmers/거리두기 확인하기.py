def solution(places):
    result = []

    for room in places:
        signal = True
        for i in range(5):
            for j in range(5):
                if room[i][j] == 'P':
                    if (i > 0 and room[i-1][j] == 'P') or  (i < 4 and room[i+1][j] == 'P') or (j > 0 and room[i][j-1] == 'P') or (j < 4 and room[i][j+1] == 'P'):
                        signal = False
                        break
                    if ((i > 1 and room[i-2][j] == 'P') and (room[i-1][j] != 'X')) or ((i < 3 and room[i+2][j] == 'P') and (room[i+1][j] != 'X')) or ((j > 2 and room[i][j-2] == 'P') and (room[i][j-1] != 'X')) or ((j < 3 and room[i][j+2] == 'P') and (room[i][j+1] != 'X')):
                        signal = False
                        break
                    if ((i> 0 and j>0 and room[i-1][j-1] == 'P') and (room[i-1][j] != 'X' or room[i][j-1] != 'X')) or ((i< 4 and j<4 and room[i+1][j+1] == 'P') and (room[i+1][j] != 'X' or room[i][j+1] != 'X')) or ((i>0 and j<4 and room[i-1][j+1] == 'P') and (room[i-1][j] != 'X' or room[i][j+1] != 'X')) or ((i<4 and j>0 and room[i+1][j-1] == 'P') and (room[i+1][j] != 'X' or room[i][j-1] != 'X')):
                        signal = False
                        break
            if signal == False:
                break
        if signal == True:
            result.append(1)
        else:
            result.append(0)
    return result
