# ?
def hamming(n):
    h = 0
    x2 = 2
    x3 = 3
    x5 = 5
    i = 0
    j = 0
    k = 0
    
    for m in range(n):
        h = min(x2, x3, x5)
        print("h after Min %s" % h)
        if x2 == h:
            i += 1
            x2 = 2 * i
        if x3 == h:
            j += 1
            x3 = 3 * j
        if x5 == h:
            k += 1
            x5 = 5 * k
        print(h)
        print("h after ifs %s\n" % h)
        
    print("Final h %s" % h)
    return h


def _hamming():
    hamming_numbers = [1]
    x2, x3, x5 = 0, 0, 0
    while True:
        next_hamming = min(hamming_numbers[x2]*2, hamming_numbers[x3]*3, hamming_numbers[x5]*5)
        yield next_hamming
        
        if next_hamming == hamming_numbers[x2]*2:
            x2 += 1
        if next_hamming == hamming_numbers[x3]*3:
            x3 += 1
        if next_hamming == hamming_numbers[x5]*5:
            x5 += 1
            
        hamming_numbers.append(next_hamming)

def hamming_generator_version(n):
    hamming_gen = _hamming()
    hamming_numbers = [0,1] + [next(hamming_gen) for _ in range(n)]
    return hamming_numbers[n]
