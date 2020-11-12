def first():
    num = int(input("Кратно число:"))
    count = int(input("Брой на кратни:"))
    for i in range(num, count * num + 1, num):
        print(i)


def second():
    vocalsstr = str(input("Please type a sentence: "))
    vocalseng = "aeiou"
    vocalsbg = "аъеиоу"
    for v in vocalseng:
        if (vocalsstr.lower().count(v)) != 0:
            print(v, vocalsstr.lower().count(v))
    for v in vocalsbg:
        if (vocalsstr.lower().count(v)) != 0:
            print(v, vocalsstr.lower().count(v))


def third():
    listth = ["Everybody", "1", "is","55", "very", "3", "debel"]
    for item in listth:
        if item.isdigit():
            listth.remove(item)
    print(listth)


def fourth():
    inpstr = input("Give a number to check if symmetric:")
    if (int(inpstr) > 9):
        print(str(inpstr) == str(inpstr)[::-1])
    else:
        print("Not symmetrical")


print("First exercise")
first()
print("Second exercise")
second()
print("Third exercise")
third()
print("Fourth exercise")
fourth()

def Bonus():
    stri = "Marto iska da mnogo debel"
    words = stri.split()
    for i in range(len(words)):
        words[i] = str(words[i])[:1] + "*" + str(words[i])[2:]
    stri = ' '.join(words)
    print(stri)

print("Bonus")
Bonus()