def plain(str):
    length = len(str)
    for i in range( length // 2) :
        if(str[i] != str[length-1-i]):
            return False
    return True

print(plain('mommom'))