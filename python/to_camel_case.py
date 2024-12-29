#https://www.codewars.com/kata/517abf86da9663f1d2000003/python

def to_camel_case(text):
    res = ''
    i = 0

    while i < len(text):
        if text[i] == '-' or text[i] == '_':
            res += text[i+1].upper()
            i += 1
        else:
            res += text[i]
        i += 1
        
    return res

#With using text.title for each word
def to_camel_case_title(text):
    return text[:1] + text.title()[1:].replace('_', '').replace('-', '')
