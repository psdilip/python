def zeros(input):
    numbers = [i if type(i) != str else 0 for i in input]
    return numbers