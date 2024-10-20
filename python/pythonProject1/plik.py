import math

def main():
    #1a
    temp = 0
    for i in range(2,101,2):
        temp += i
    print(temp)
    #1b
    temp = 0
    for i in range(1,100):
        temp += i**2
    print(temp)
    #1c
    temp = 0
    for i in range(1,63):
        temp += 2**i
    print(temp)
    #1d
    a = int(input('wprowadz liczbe: '))
    b = int(input('wprowadz liczbe: '))
    temp = 0
    if a > b:
        print(0)
    else:
        for a in range(a,b+1) :
            temp += a
        print(temp)
    #2a
    temp = 0
    n = int(input('podaj ilosc: '))
    a = int(input('wprowadz liczbe: '))
    for i in range(1,n+1,1):
        temp += a
        a += 1
    print(temp)
    # 2b
    temp = 1
    n = int(input('podaj ilosc: '))
    a = int(input('wprowadz liczbe: '))
    for i in range(1, n + 1, 1):
        temp *= a
        a += 1
    print(temp)
    # 2c
    temp = 0
    n = int(input('podaj ilosc: '))
    a = int(input('wprowadz liczbe: '))
    for i in range(1, n + 1, 1):
        temp += abs(a)
        a += 1
    print(temp)
    # 2d
    temp = 0
    n = int(input('podaj ilosc: '))
    a = int(input('wprowadz liczbe: '))
    for i in range(1, n + 1, 1):
        temp += math.sqrt(abs(a))
        a += 1
    print(temp)
    # 2e
    temp = 1
    n = int(input('podaj ilosc: '))
    a = int(input('wprowadz liczbe: '))
    for i in range(1, n + 1, 1):
        temp *= abs(a)
        a += 1
    print(temp)
    # 2f
    temp = 0
    n = int(input('podaj ilosc: '))
    a = int(input('wprowadz liczbe: '))
    for i in range(1, n + 1, 1):
        temp += a**2
        a += 1
    print(temp)
    # 2g
    temp = 0
    temp1 = 1
    n = int(input('podaj ilosc: '))
    a = int(input('wprowadz liczbe: '))
    b = a
    for i in range(1, n + 1, 1):
        temp += a
        a += 1
    for i in range(1, n + 1, 1):
        temp1 *= b
        b += 1
    print(temp,temp1)
    # 2h
    n = int(input('podaj ilosc: '))
    a = int(input('wprowadz liczbe: '))
    temp = 0
    for i in range(1,n+1,1):
        temp += a*(-1)**(i+1)
        a += 1
    print(temp)
    # 2i
    n = int(input('podaj ilosc: '))
    a = int(input('wprowadz liczbe: '))
    temp = 0
    for i in range(1, n+1, 1):
        temp += (a * (-1) ** (i))/(math.factorial(i))
        a += 1
    print(temp)
    #3
    n = int(input('podaj ilosc: '))
    temp = 0
    liczby = []
    for i in range(n):
        liczba = float(input(f"Wprowadź liczbę {i + 1}: "))
        liczby.append(liczba)
    for i in range(1, n):
        print(liczby[i])
    print(liczby[0])
    for i in range(1, 65):
        print('Mężny bądź, chroń pułk twój i sześć flag')

if __name__ == '__main__':
    main()