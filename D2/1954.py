T = int(input())
direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
for t in range(1, T+1):
    N = int(input())
    snail = [[0 for col in range(N)] for row in range(N)]
    row_index = 0
    col_index = 0
    number = 1

    while True:
        if number == N*N:
            break
        for d in direction:
            if number == N*N:
                snail[row_index][col_index] = number
                break
            while True:
                print(row_index, col_index)
                snail[row_index][col_index] = number
                print(snail)
                number += 1
                row_index += d[0]
                col_index += d[1]

                if col_index == N:
                    col_index -= 1
                    row_index += 1
                    break
                elif col_index == -1:
                    col_index += 1
                    row_index -= 1
                    break
                elif row_index == N:
                    row_index -= 1
                    col_index -= 1
                    break
                elif snail[row_index][col_index] != 0:
                    break

    print("#{}".format(t))
    for r in snail:
        print(r)