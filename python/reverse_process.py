https://www.codewars.com/kata/5dad6e5264e25a001918a1fc/python

def decode(r):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    num = "".join([i for i in r if i in '0123456789'])
    string = r[len(num):]
    lookup = ""
    res = ""
    for i in range(len(alphabet)):
        letter = alphabet[(i * int(num)) % 26]
        if letter in lookup:
            return "Impossible to decode"
        lookup += letter
    for char in string:
        res += alphabet[lookup.index(char)]
    return res
