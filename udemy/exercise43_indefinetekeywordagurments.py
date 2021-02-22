def find_sum(**kwargs):
    for i in kwargs:
        print(i)
    return sum(kwargs.values())
    
print(find_sum(a=3,b=3,c=4))