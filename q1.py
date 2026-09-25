def sumofnum(num):
    if num<10:
        return num
    return sumofnum(num//10)+num%10
num=154
print(sumofnum(num))
        