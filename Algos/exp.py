def paw(num,exp):
    if(exp == 0):
        return 1
    return num * paw(num,exp-1)



def paw2(num,exp):
    if exp == 0:
        return 1
    half = paw(num,exp//2) 
    if num % 2 == 0:
        return half * half
    return half * half * num

print(paw(2,2))
print(paw2(2,2))



