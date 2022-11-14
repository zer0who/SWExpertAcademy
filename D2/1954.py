T = int(input())
direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
for t in range(1, T+1):
    N = int(input())
    snail = [[0 for col in range(N)] for row in range(N)]
    row_index = 0
    col_index = 0
    number = 1

    while True:
        for d in direction:
            while True:
                snail[row_index][col_index] = number
                print(snail)
                number += 1
                row_index += d[0]
                col_index += d[1]
                if col_index == N:
                    print("case1")
                    col_index -= 1
                    row_index += 1
                    break
                elif col_index == -1:
                    print("case2")
                    col_index += 1
                    row_index -= 1
                    break
                elif row_index == N:
                    print("case3")
                    row_index -= 1
                    col_index -= 1
                    break
                elif snail[row_index][col_index] != 0:
                    print("wall")
                    break

        if number == N*N:
            break

    print("#{}".format(t))
    for r in snail:
        print(r)