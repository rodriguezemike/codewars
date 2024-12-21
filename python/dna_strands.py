import string
def DNA_strand(dna):
    # code here
    complements = {
        "A" : "T",
        "T" : "A",
        "C" : "G",
        "G" : "C"
    }
    return "".join([complements[letter] if letter in complements else letter for letter in dna])

#Python 3 style
def DNA_strand(dna):
    return dna.translate(string.maketrans("ATCG","TAGC"))
    # Python 3.4 solution || you don't need to import anything :)
    # return dna.translate(str.maketrans("ATCG","TAGC"))
