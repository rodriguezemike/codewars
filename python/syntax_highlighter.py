#https://www.codewars.com/kata/58708934a44cfccca60000c4
def highlight(code):
    # Implement your syntax highlighter here
    wrap_dictionary = {
        "F" : '<span style="color: pink">%s</span>',
        "L" : '<span style="color: red">%s</span>',
        "R" : '<span style="color: green">%s</span>',
        "numeric" : '<span style="color: orange">%s</span>',
        "(" : "%s",
        ")" : "%s"
    }
    i = 0
    wrapped = ""
    numerics = [str(i) for i in range(10)]
    while i < len(code):
        j = i + 1
        char = code[i]
        if char in numerics:
            char = "numeric"
            while j < len(code) and code[min(len(code),j)] in numerics:
                j+=1
        else:
            while j< len(code) and code[min(len(code),j)] == char:
                j+=1
        wrapped += wrap_dictionary[char] % code[i:j]
        i = j 
    return wrapped

