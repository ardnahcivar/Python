import math

#from Tools.i18n.pygettext import safe_eval

n, m = map(int, input().split())
main_lis = []
lis = []
count_lst = []
cords = []

for i in range(n):
    lis = [list(i) for i in input().split()]
    main_lis.append(lis[0])
#print(main_lis)


def check(i, j, incr=1,count=0):
    try:
        if i - incr < 0 or j-incr < 0 or main_lis[i-incr][j] == 'X' or main_lis[i][j+incr] == 'X' or main_lis[i+incr][j] == 'X' or main_lis[i][j-incr] == 'X':
            raise IndexError
        else:
            #print('indide')
            if main_lis[i-incr][j] == 'G' and main_lis[i][j+incr] == 'G' and main_lis[i+incr][j] == 'G' and main_lis[i][j-incr] == 'G':
                #print('insode')
                count += 4
                incr += 1
                check(i, j, incr,count)
    except IndexError as e:
        if count != 0:
            count_lst.append(count)
            temp = [i, j]
            cords.append(temp)

def first_time():
    for i in range(n):
        for j in range(m):
                if i == 0 or i == n-1 or j==0 or j==m-1:
                    pass
                else:
                    if main_lis[i][j] == 'G':
                        print('found at ', i, j)
                        check(i,j)




def marked(i, j, incr=1, count=0):
    global main_lis
    try:
        if i - incr < 0 or j-incr < 0 :
            raise IndexError
        else:
            print('in marking')
            if main_lis[i-incr][j] == 'G' and main_lis[i][j+incr] == 'G' and main_lis[i+incr][j] == 'G' and main_lis[i][j-incr] == 'G':
                main_lis[i][j] = 'X'
                main_lis[i - incr][j] = 'X'
                main_lis[i][j + incr] = 'X'
                main_lis[i + incr][j] = 'X'
                main_lis[i][j - incr] = 'X'
                print('marked ',i,j)
                count += 1
                incr += 1
                marked(i, j, incr,count)
    except IndexError as e:
        print('marked list is',main_lis)


first_time()
print(count_lst)
print(cords)

#copy = main_lis.copy()
copy = [i for i in main_lis]
print('mai list ais',copy)
#copyCount = count_lst.copy()
copyCount = [i for i in count_lst]
#copyCords = cords.copy()
copyCords = [i for i in cords]
secondLs= []

'''
print(count_lst)
print(cords)
print(len(count_lst))
print(len(cords))
print(max(count_lst))
max_cords = cords[count_lst.index(max(count_lst))]
print(max_cords)
first = max(count_lst)+1
print('first value is {}'.format(first))
'''

print(copyCords)
for p in copyCords:
    print(p[0],p[1])
    marked(p[0],p[1])
    print('main list is',main_lis)
    print('copy list is',copy)
    #main_lis = copy.copy()
    main_lis = [i for i in copy]
   #print(main_lis)

print('secondlists are')
print(secondLs)

'''
marked(max_cords[0], max_cords[1])

print(main_lis)

count_lst.clear()
cords.clear()

first_time()
print('lst is')
print(count_lst)
print(cords)
print(len(cords))
if len(count_lst) == 0:
    second = 1
else:
    second = max(count_lst)+1
print('second value is {}'.format(second))


print('final val is {}'.format(first*second))
'''
