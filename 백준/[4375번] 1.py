while True:
    try:
        n = int(input())
        if n == 1:
            print(1)
            break
        ct = 1
        z = 1
        for i in range(n):
            ct += 10**z
            z += 1
            if ct%n == 0 and ct % 2 != 0 and ct % 5 != 0:
                break
        print(len(str(ct)))
    except EOFError:
        break
