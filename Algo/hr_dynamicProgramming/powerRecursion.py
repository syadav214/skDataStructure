def pow(num, exp):
    if exp == 1:
        return num
    return num * pow(num, exp -1)
print(pow(2,8))