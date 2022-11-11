T = int(input())

for t in range(1, T+1):
    answer = 1
    puzzle = []
    for i in range(9):
        puzzle.append([*map(int, input().split())])
    
    
    print("#{0}".format(t), answer)