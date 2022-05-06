def solution(phone_number):
    n = len(phone_number)-4
    return '*'*n+phone_number[-4:]
