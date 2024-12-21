# https://www.codewars.com/kata/56f78a42f749ba513b00037f/solutions

from itertools import product

def rolldice_sum_prob(sum_, dice_amount):
    dice_values = [1,2,3,4,5,6]
    counter = 0
    for c in product(dice_values, repeat = dice_amount):
        counter += 1 if sum(list(c)) == sum_ else 0
    prob = counter/6**dice_amount
    return prob             

