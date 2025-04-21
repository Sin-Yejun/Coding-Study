def base(n1, n2, base):
    n1 = int(n1, base)
    n2 = int(n2, base)
    result = int(str(n1+n2), base)
    print(result)


base('57', '12', 5)
