def getN():
    n = int(input("Input n: "))
    return n


def recurs(text, n):
    if n == 1:
        text = (len(text) // 5) * '(' + "1" + text
        print(text)
    elif n < 1:
        print("No way")
    else:
        if n % 10 == 6 or n % 10 == 1:
            text = " + 5)" + text
            recurs(text, n - 5)
        elif n % 3 == 0:
            text = " * 3)" + text
            recurs(text, n / 3)
        else:
            text = " + 5)" + text
            recurs(text, n - 5)
