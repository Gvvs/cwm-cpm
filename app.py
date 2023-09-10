""" Practice """


def fizz_buzz(inpt):
    """func"""
    result = ""
    if inpt % 3 == 0:
        result += "Fizz"
    if inpt % 5 == 0:
        result += "Buzz"
    if result == "":
        result = str(inpt)
    return result


print(fizz_buzz(104))
