
# Primer ejercicio


def func1(n):
    lst = n.split(",")
    temp = []
    for i in lst:
        temp.append(int(i))
    return sum(temp)


# Segundo ejercicio


def func2(lst):
    for i in lst:
        counter = 0
        while counter < len(i):
            if i[counter] % 2 == 0:
                i[counter] = True
                counter += 1
            else:
                i[counter] = False
                counter += 1
    return(lst)
