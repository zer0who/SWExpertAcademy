T = int(input())
for i in range(1, T+1):
    N = int(input())
    zero_to_nine = [0] * 10
    count = 0
    while(True):
        count += 1
        while(True):
            zero_to_nine[N//10] += 1
            N = N
    
    print("#{0} {1}".format(i, count))