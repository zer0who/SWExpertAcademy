T = int(input())
direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
for t in range(1, T+1):
    N = int(input())
    result = [[0 for col in range(N)] for row in range(N)]
    row_index = 0
    col_index = 0
    number = 1

    while True:
        for d in direction:
            while True:



    print("#{}".format(t))
    for r in result:
        for i in len(r):
            print(r[i], end=" ")
        print("")
