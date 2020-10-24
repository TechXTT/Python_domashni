def First():
    for x in range(2, 5, 2):
        for y in range(2, 10, 2):
            for z in range(2, 10, 2):
                for c in range(2, 10, 2):
                    print(x, y, z, c, end=",")
    print(",")

def Second():
    list=[34,34353,1,2,534,752,36,568]
    n=len(list)-1

    for x in range(n):
        for y in range(n-x):

            if list[y] > list[y+1]:
                list[y], list[y + 1] = list[y + 1], list[y]
    difference = list[n] - list[0]
    print(difference)

def Third():
    print("Give a String : ")
    strth = input()
    print(strth.count("")-1)

print("First function:")
First()
print("Second function:")
Second()
print("Third function:")
Third()