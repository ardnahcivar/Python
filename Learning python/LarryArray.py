if __name__ ==  "__main__":
    t = int(input())

    for i in range(t):
        inversion_count = 0
        n = int(input())
        a = [int(i) for i in input().split()]
        #print(a)
        b = sorted(a)
       # print('sorted list is:', b)

        for i, j in enumerate(a):
            b = a[i+1:]
            for k in b:
                if k < j:
                    inversion_count = inversion_count+1

        #print(inversion_count)
        if(inversion_count%2 ==0):
            print('YES')
        else:
            print('NO')