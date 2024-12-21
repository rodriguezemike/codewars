#Weird case 1 liner:

def to_weird_case(words):
    return " ".join([("".join([word[i].upper() if i % 2 == 0 else word[i].lower() for i in range(len(word))])) for word in words.split()])
