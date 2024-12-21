#https://www.codewars.com/kata/5659c6d896bc135c4c00021e
def next_smaller(n):
    num = list(str(n))
    index = len(num) - 2
    j = len(num) - 1
    while index >=0 and num[index] <= num[index+1]:
        index -= 1
    if index == -1:
        return index
    while num[j] >= num[index]:
        j -= 1
    num[index], num[j] = num[j], num[index]
    num[index+1:] = reversed(num[index+1:])
    if ''.join(num).startswith("0"):
        return -1
    else:
        return int(''.join(num))

