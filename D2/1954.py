T = int(input())

for t in range(1, T+1):
    N = int(input())
    num = 0
    result = [[0 for col in range(N)] for row in range(N)]
    



    print("#{0}".format(t))
    for res in result:
        for r in res:
            print(r, end = " ")
        print("")