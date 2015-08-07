


def func(a, b):
    if a < b:
        return 1
    else:
        return -1

a = [5,3,6,1,7]
a.sort(cmp=func)
print a


