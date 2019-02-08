string = 'mostafa is the best'


def explode(str,delimeter = ' '):
    start = 0
    arr = []
    length =len(str)
    for i in range(length):
        print(str[i])
        if str[i] == delimeter:
            arr.append(str[start:i])
            start = i+1
        elif i == length -1:
            arr.append(str[start:])
    return arr



print(explode(string))