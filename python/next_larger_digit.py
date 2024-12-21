#https://www.codewars.com/kata/55983863da40caa2c900004e/train/python

def next_bigger(n):
    num = list(str(n))
    index = len(num) - 2
    j = len(num) - 1
    while index >=0 and num[index] >= num[index+1]:
        index -= 1
    if index == -1:
        return index
    while num[j] <= num[index]:
        j -= 1
    num[index], num[j] = num[j], num[index]
    num[index+1:] = reversed(num[index+1:])
    return int(''.join(num))

