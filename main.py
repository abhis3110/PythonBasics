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


if __name__ == "__main__":
    # fun()
    var_types()
