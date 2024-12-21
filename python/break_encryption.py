#https://www.codewars.com/kata/52cf02cd825aef67070008fa/train/python

def decode(s):
    alphabet = "abcdefghijklmnopqrstuvwxyz" + "abcdefghijklmnopqrstuvwxyz".upper() + "0123456789" + ".,? =/"
    symbols = "!@#$%^&*()_+-"
    offset = 0
    res = ""
    for char in s:
        if char in symbols:
            res += char
	    continue
        else:
            for w in alphabet:
                if encode("_"*offset + w)[-1] == char:
                    res += w
                    break
        offset += 1
    return res;
