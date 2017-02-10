names = ['css45','java8']
mystr = 'piyush is sdsdsds css3 CSS java8'
splited = mystr.split()
print(splited)

for i in names:
    for j in splited:
        if i.lower() == j.lower():
            print(j)
            break
        



