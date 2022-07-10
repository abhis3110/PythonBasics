# main scope or global scope, function calling, variable and input output on console
def fun():
    print("enter first no")
    x = int(input())
    print("Print second number")
    y = int(input())
    print("Sum of two number is ")
    print(x + y)


def var_types():
    x = 3
    print(type(x))
    y = 3.7
    print(type(y))
    s = "Abhishek"
    print(type(s))
    si = "3"
    i = int(si)
    print(i)


def condition():
    print("Enter the Grade Score")
    x = int(input())
    if x >= 90:
        print("A")
    elif x >= 80:
        print("B")
    elif x >= 70:
        print("C")
    elif x >= 60:
        print("D")
    else:
        print("E")


def leapyear():
    print("Enter year")
    x = int(input())
    if x % 400 == 0:
        print("Leap Year")
    elif x % 4 == 0 and x % 100 != 0:
        print("Leap year")
    else:
        print("Not Leap year")


if __name__ == "__main__":
    # fun()
    # var_types()
    # condition()
    leapyear()
