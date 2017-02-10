import sys,math, numpy

def create_grid(s, grid, i, c):
    grid.append(list(s[i:c+i]))
    #print(s[i:c+i])

if __name__ == "__main__":
    grid = []
    s = input().strip()
    #print(len(s))
    r = math.floor(math.sqrt(len(s)))
    c = math.ceil(math.sqrt(len(s)))

    for i in range(0, len(s), c):
        create_grid(s, grid, i, c)

    print('grid created ', grid)

    count = 0

    while(count != c):
        for i in grid:
            try:
                print(i[count], end="")
            except IndexError:
                pass
        count = count+1
        print(" ", end="")









