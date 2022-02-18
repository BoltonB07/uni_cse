# Question 1
from math import *


def swap():
    a, b = 5, 10
    print(a, "&", b)
    c = a
    a = b
    b = c
    print(a, "&", b)


# Question 2
def leap():
    year = 2048
    if year % 4 == 0:
        print("it is a leap year")
    else:
        print("It is not a leap year")


# Question 3
def Sum():
    UpLim = 46
    for x in range(UpLim + 1):
        x += x
    print(x)


# Question 4
def armstrongnumber():
    num = 153
    numstr = str(num)
    counter = 0
    armstrong = 0
    for x in numstr:
        armstrong += (int(numstr[counter]) ** 3)
        counter += 1
    if armstrong == num:
        print("It is an Armstrong Number")
    else:
        print("It isn't an Armstrong Number")


# Question 5
def fibonacci():
    fib1, fib2, x = 0, 1, 0
    while x < 10:
        print(fib1)
        fib3 = fib1 + fib2
        fib1 = fib2
        fib2 = fib3
        x += 1


# Swap values with XOR
def SwapXOR():
    x, y = 5, 10
    x = x ^ y
    y = x ^ y
    x = x ^ y
    print("x=" + str(x), "y=" + str(y))


# Swap with arithmetic values
def ArithSwap():
    x, y = 5, 10
    x = x * y
    y = x / y
    x = x / y
    print("x=" + str(x), "y=" + str(y))


# Using Count
def Counting():
    parts = ["GPU", "CPU", "PSU", "Motherboard", "GPU", "GPU", "RAM"]
    x = parts.count("GPU")
    print(x)
    arr = [2, 3, 4, 5, 6, 3, 4, 56, 7, 346, 69, 420]
    y = sum(arr)
    print(y)


# Factorial
def factorial(x):
    fac = 1
    for y in range(1, x + 1):
        fac *= y
    return (fac)


# reversing a string
def reverseString(str):
    str1 = ""
    for i in str:
        str1 = i + str1
    return str1


# explicit type conversion
def typeConvert():
    a, b = 69, 1337.420
    c = int(a + b)
    print(c)


# Set
def Settest():
    c = "applesauce"
    s = set(c)
    print(s)
    s = set(c)
    print(s)
    s = set(c)
    print(s)


# Converting a tuple to a dictionary
def tupleToDictionary():
    t = (("a", 1), ("b", 2), ("c", 3), ("d", 4))
    d = dict((x, y) for x, y in t)
    print(d)


# using a nested for loop
def array():
    l = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    count = 0
    for x in range(len(l)):
        for y in range((len(l[x]))):
            print(l[x][y], "\t", end='')
        print()


# ppt
def toSubway():
    # Function to find a route to Subway
    pass


def toMcDonalds():
    # Function to find a route to McDonald's
    pass


def f(x):
    return x * (sin(x) ** 2)


def g(x):
    return 8 * (x ** 2) + 4 * x + 3


def display(x, y):
    print("At x= " + str(x) + " f(x)= " + str(y))


def calc():
    for x in range(-100, 101):
        if x < -25:
            y = f(x)
            display(x, y)
        elif -25 <= x <= 25:
            display(x, g(x))
        else:
            display(x, f(x))


def calc2():
    for x in range(100, -101):
        if x <= 25:
            y = x * (sin(x) ** 2)
            print("At x= " + str(x) + " f(x)= " + str(y))
        elif -25 <= x <= 25:
            y = 8 * (x ** 2) + 4 * x + 3
            print("At x= " + str(x) + " f(x)= " + str(y))
        else:
            y = x * (sin(x) ** 2)
            print("At x= " + str(x) + " f(x)= " + str(y))


def f1bonacci():
    fib1, fib2, x = 0, 1, 0
    while x < 10:
        print(fib1)
        fib3 = fib1 + fib2
        fib1 = fib2
        fib2 = fib3
        x += 1


def inverseFib(n):
    Fn = (1 / 5 ** (1 / 2)) * (((1 + 5 ** (1 / 2)) / 2) ** n - ((1 - 5 ** (1 / 2)) / 2) ** n)  # Binet's Formula
    while Fn >= 1:
        Fn_1 = 0.382 * Fn  # Golden Ratio
        Fn_2 = Fn - Fn_1
        if round(Fn) != 0:
            print(round(Fn))
        if round(Fn_1) != 0:
            print(round(max(Fn_1, Fn_2)))
        if round(Fn_2) != 0:
            print(round(min(Fn_1, Fn_2)))
        Fn = 0.382 * Fn_2
    if round(Fn) != 0:
        print(round(Fn))


def squareRoot(n):
    return n ** (1 / 2)


def cubeRoot(n):
    return n ** (1 / 3)


def squareRootComplex(a, b):
    modZ = ((a ** 2) + (b ** 2)) ** (1 / 2)
    x = ((modZ + a) / 2) ** (1 / 2)
    y = ((modZ - a) / 2) ** (1 / 2)
    if b > 0:
        print(str(x) + " + i" + str(y))
    else:
        print(str(x) + " - i" + str(y))


def smallestDivisor(n):
    d = 2
    while d <= n // 2:
        if (n % d == 0):
            break
        else:
            d += 1
    print(d)


def HCF(n):
    d = 2
    flag = 0
    greatest = 0
    HCF = 1
    for x in n:
        if x > greatest:
            greatest = x
    # to find HCF
    while d <= greatest // 2:
        for x in n:
            if x % d != 0:
                flag = 0
            else:
                flag = 1
            if flag == 0:
                break
        if flag == 1:
            HCF = d
        d += 1
    print(HCF)


def PrimeNums(a, b):
    for x in range(a, b + 1):
        c = 0
        for n in range(2, (x // 2) + 1):
            if x % n == 0:
                c += 1
        if c == 0:
            print(str(x) + ", ", end="")


def increase(a, b):
    for x in range(1, b + 1):
        a = a ** x
        print(str(a), end=", ")


def PRNG(seed, root, num):  # we take the root of the seed. num is how many random numbers you want to generate
    rn = seed ** (1 / root)
    string = str(rn)
    for i in range(2, num + 2):
        print(string[i])


import array as arr


def array10elements(list):
    a = arr.array('i', list)
    for i in range(0, len(a)):
        for j in range(1 + i, len(a)):
            if i == j:
                continue
            elif a[i] == a[j]:
                print("repetition exists at index " + str(i) + " and " + str(j) + ". Repeated values: " + str(
                    a[i]) + " and " + str(a[j]) + ".")


def concatAndLength(list, concat):
    a = arr.array('i', list)
    a.append(concat)
    print(str(len(a)))


def printAndReverse(list):
    a = arr.array('i', list)
    for i in range(0, len(a)):
        print(a[i])
    for j in range(0, len(a)):
        print(a[len(a) - 1 - j])


import random


def RNG():
    # Random Module in Python:

    print(random.randint(6,
                         9))  # this outputs a random integer between the given limits inclusive of the limits themselves.
    print(random.random())  # This gives a random floating point value between 0 and 1.
    print(random.uniform(6,
                         9))  # This gives you a random floating point value between the specified limits inclusive of them.
    print(random.choice([2, 4, 69, 420, 69420]))  # This chooses a random element from the given list
    print(random.sample([2, 4, 69, 420, 69420],
                        3))  # This chooses a specified number of random elements from the given sequence
    list = [2, 4, 69, 420, 69420]
    print("before shuffle:", end=' ')
    print(list)
    print(random.shuffle(list))  # This function shuffles the given list and returns a "None" value.
    print("after shuffle:", end=' ')
    print(list)
    random.seed(
        6)  # Seed initializes a pseudo-random number generator and helps you to generate the same sequence of random numbers again and again
    for i in range(3):
        print(random.random())
    # sample usage
    guess = int(input(
        "Enter a number from 1 to 14. Your score depends on how close your guess was compared to the randomly generarted number: "))
    rng = random.randint(1, 14)
    if rng - guess < 0:
        diff = -(rng - guess)
    else:
        diff = rng - guess
    score = 13 - diff
    print("score: " + str(score))


def arrayCount(list):
    a = arr.array('i', list)
    count = 0
    for i in a:
        count += 1
    return count


def maxAndMinArray(list):
    a = arr.array('i', list)
    min, max = a[0], a[0]
    for i in a:
        if i < min:
            min = i
        if max < i:
            max = i
    print("min= " + str(min) + ", max= " + str(max))


# Partitioning an array is dividing an array into two or more parts. This program takes a list input and then assigns it to variable a.
# b and c are empty arrays to which the elements have been appended to.
# The first half of the array a has been appended to b and the second half to c.
def twoWayPartition(list):
    a = arr.array('i', list)
    b = arr.array('i', [])
    c = arr.array('i', [])
    for i in range(0, len(a)):
        if 0 <= i <= len(a) // 2:
            b.append(a[i])
        else:
            c.append(a[i])
    print("First partition: ", end='')
    for i in b:
        print(i, end=', ')
    print()
    print("Second partition: ", end='')
    for i in c:
        print(i, end=', ')


def nthSmallest(num, list):
    a = arr.array('i', list)
    # Finding the greatest number
    greatest = a[1]
    for i in a:
        if i > greatest:
            greatest = i
    # Finding the smallest number
    for j in range(1, num + 1):
        smallest = greatest
        for i in range(0, len(a)):
            if a[i] < smallest:
                smallest = a[i]
                a[i] = greatest

    print("The nth smallest element in the list where n = " + str(num) + " is: " + str(smallest))


def applyingListOps(list):
    list.append(69)
    print("append 69420: " + str(list))
    list2 = list.copy()
    print("list2=list.copy() = " + str(list))
    list2.clear()
    print("list.count() = " + str(list.count(3)))
    print("List extended with [1,3,3,7] = " + str(list.extend([1, 3, 3, 7])))
    print("index of 1 = " + str(list.index(1)))
    list.insert(4, 2)
    print("insert 4 at pos 2" + str(list))
    list.pop(2)
    print("pop element at pos 2" + str(list))
    list.remove(1)
    print("removing 1" + str(list))
    list.reverse()
    print("reversed list = " + str(list))
    list.sort()
    print("sorted list = " + str(list))


def applyingTupleOps(tuple):
    print("list.count(3) = " + str(tuple.count(3)))
    print("list.index(3) = " + str(tuple.index(3)))


def applyingSetOps(set):
    print("set.add(69420) = " + str(set.add(69420)))
    set1 = set.copy()
    set.clear()
    set = set1.copy()
    set1.add(1337)
    print("difference = " + str(set.difference(set1)))
    #print("set1.differenceUpdate(set) = " + str(set1.differenceUpdate(set)))
    print("set.discard(4) = " + str(set.discard(4)))
    set1.add(69)
    print("set.intersection(set1) = " + str(set.intersection(set1)))
    #print("set.intersectionUpdate(set1)" + str(set.intersectionUpdate(set1)))
    print("set.isdisjoint(set1) = " + str(set.isdisjoint(set1)))


applyingSetOps({1, 2, 3, 4, 5, 69, 420, 1, 3, 3, 7})
