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


def print_even():
    print("Input the number")
    x = int(input())
    for i in range(2, x + 1, 2):
        print(i)


def multiplication_table():
    print("Enter any number from  1 to 10")
    i = int(input())
    for i in range(1, i + 1):
        print("Multiplication table for", i)
        for j in range(1, 11):
            print(i, "x", j, "=", i * j)


def demo_array():
    marks = [60, 70, 80, 90, 65, 75]
    total = 0
    for i in range(0, len(marks)):
        total += marks[i]
    print(total)
    for value in marks:
        total += value
    print(total)


def greet(name):
    print("Hi", name, "Welcome to the class")


if __name__ == "__main__":
    # fun()
    # var_types()
    # condition()
    # leapyear()
    # print_even()
    # multiplication_table()
    # demo_array()
    names = ["neha", "raj", "wasim", "atul", "maps", "ankit"]
    for values in names:
        greet(values)
