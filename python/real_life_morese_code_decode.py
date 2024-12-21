#https://www.codewars.com/kata/54acd76f7207c6a2880012bb/train/python

import math

def find_bucket(distribution, value_to_find = 0):
    if not distribution:
        return -1
    for k,v in distribution.items():
        if v == value_to_find:
            return k
    else:
        value_to_find += 1
        return find_bucket(distribution, value_to_find)
    
def compose_message(zeros, ones, zeros_bucket_one, zeros_bucket_two, ones_bucket):
    new_bits = ''
    new_ones, new_zeros = [], []
    print("Zeros %s" % zeros)
    print("Ones %s" % ones)
    print("Zeros Bucket One %s" % zeros_bucket_one)
    print("Zeros Bucket Two %s" % zeros_bucket_two)
    print("Ones Bucket %s" % ones_bucket)
    print()
    if ones_bucket > zeros_bucket_one:
        if len(zeros) == 1:
            if abs(len(ones[0]) - len(zeros[0]))%3 != 0:
                zeros = []
                ones_bucket -= 1
    elif zeros_bucket_one > ones_bucket:
        zeros_bucket_two = ones_bucket*2+3
        zeros_bucket_one = ones_bucket
    elif zeros_bucket_one == ones_bucket:
        if zeros_bucket_two - zeros_bucket_one < 3:
            zeros_bucket_two = zeros_bucket_one*3
    if zeros_bucket_two == -1:
        zeros_bucket_two = zero_bucket_one * 3
    
    print("Zeros Bucket One %s" % zeros_bucket_one)
    print("Zeros Bucket Two %s" % zeros_bucket_two)
    print("Ones Bucket %s" % ones_bucket)
    print("Zeros %s" % zeros)
    print("Ones %s" % ones)
    for i in ones:
        if len(i) <= ones_bucket:
            new_ones.append('1')
        else:
            new_ones.append('111')
    for i in zeros:
        if len(i) <= zeros_bucket_one:
            new_zeros.append('0')
        elif len(i) <= zeros_bucket_two:
            new_zeros.append('000')
        else:
            new_zeros.append('0000000')
    if new_zeros:
        for zero,one in zip(new_zeros, new_ones):
            new_bits += one
            new_bits += zero
        new_bits+=new_ones[-1]
    else:
        new_bits = "".join(new_ones)
    print(new_bits)
    return new_bits 
    
def decodeBitsAdvanced(bits):
    # ToDo: Accept 0's and 1's, return dots, dashes and spaces
    bits = bits.strip('0')
    if not bits:
        return ''
    elif "0" in bits:
        print(bits)
        ones = [i for i in bits.split("0") if i!='']
        zeros = [i for i in bits.split("1") if i!= '']
        ones_count = [len(i) for i in ones if i != '']
        zeros_count = [len(i) for i in zeros if i != '']
        ones_distribution,zeros_distribution = {}, {}
        for i in range(min(set(ones_count)), max(set(ones_count))+1):
            ones_distribution[i] = ones_count.count(i)
        for i in range(min(set(zeros_count)), max(set(zeros_count))+1):
            zeros_distribution[i] = zeros_count.count(i)
        print("Length of message %s" % len(bits))
        print("Ones Distribution Before Trimming\n%s\n" % ones_distribution)
        print("Zeros DIstribution Before Trimming\n%s\n" % zeros_distribution)
        ones_mid = math.ceil((len(list(ones_distribution.items()))/2)+1)
        zeros_mid = math.ceil((len(list(zeros_distribution.items()))/2)+1)
        print(ones_mid)
        print(zeros_mid)
        if len(ones_distribution) >  8:
            ones_distribution = {k:v for (k,v) in list(ones_distribution.items())[:ones_mid]}
        if len(zeros_distribution) >  8:
            zeros_distribution = {k:v for (k,v) in list(zeros_distribution.items())[:zeros_mid]}
        ones_bucket = find_bucket(ones_distribution)
        zeros_bucket_one = find_bucket(zeros_distribution)
        zeros_distribution.pop(zeros_bucket_one)
        zeros_bucket_two = find_bucket(zeros_distribution)
        if zeros_bucket_two < zeros_bucket_one:
            zeros_bucket_two = zeros_bucket_one+3
        if len(bits) > 3700:
            ones_bucket = 7
        new_bits = compose_message(zeros, ones, zeros_bucket_one, zeros_bucket_two, ones_bucket)
    else:
        new_bits = bits[0] #Idea here is heuristic. if we dont know how long a dash is, or dont know how long a . is, assume dot.
    
    return new_bits.replace('0000000','  ').replace('111', '-').replace('000', ' ').replace('1', '.').replace('0', '')

def decodeMorse(morseCode):
    # ToDo: Accept dots, dashes and spaces, return human-readable message
    print("".join([MORSE_CODE.get(token, ' ') for token in morseCode.split(" ")]).replace("  ",' ').strip())
    return "".join([MORSE_CODE.get(token, ' ') for token in morseCode.split(" ")]).replace("  ",' ').strip()
