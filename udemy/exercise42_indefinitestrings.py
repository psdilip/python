def indefinite_strings(*args):
    uppercase = []
    for i in args:
        uppercase.append(i.upper())
    order = sorted(uppercase)
    return order

print(indefinite_strings('bbb','aaa','ccc'))