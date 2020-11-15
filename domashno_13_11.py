from math import sqrt

def first():
    vocalsstr = str(input("Input your string:"))
    vocalseng = "aeiou"
    for v in vocalseng:
        for i in range(len(vocalsstr) - 1, -1, -1):
            if vocalsstr[i] == v:
                vocalsstr = vocalsstr[:i] + 4 * v + vocalsstr[i:]

    print(vocalsstr)


def second():
    integer = str(input("Input your integer:"))
    counter = 0
    ints = "0123456789"
    for i in ints:
        for l in range(len(integer) - 1, -1, -1):
            if integer[l] == i:
                counter += 1
    print(counter)


def third():
    def is_square(i):
        counter = 0
        while i >= 2:
            i = sqrt(i)
            counter += 1
        return counter

    integer = input("Input your integer:")
    print(is_square(int(integer)))
def fourth():
    prime_inp = int(input("Input your integer:"))
    prime_list = []
    primes = 0
    def is_prime(x):
        if x<2:
            return False
        for i in range(2,x):
            if not x%i:
                return False
        return True

    for z in range(prime_inp+1):
        if is_prime(z):
            prime_list.append(z)
    for x in range(len(prime_list)):
        primes += prime_list[x]
    print(primes)


print("First exercise")
first()
print("Second exercise")
second()
print("Third exercise")
third()
print("Fourth exercise")
fourth()