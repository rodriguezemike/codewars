'''
Snail Sort
Given an n x n array, return the array elements arranged from outermost elements to the middle element, traveling clockwise.

array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
snail(array) #=> [1,2,3,6,9,8,7,4,5]
For better understanding, please follow the numbers of the next array consecutively:

array = [[1,2,3],
         [8,9,4],
         [7,6,5]]
snail(array) #=> [1,2,3,4,5,6,7,8,9]
This image will illustrate things more clearly:
'''
def get_horizontal_values(left, snail_map):
    if left:
        return snail_map[0], snail_map[1:]
    else:
        return snail_map[-1][::-1], snail_map[:-1]


def get_vertical_values(down, snail_map):
    if down:
        values = [snail_map[i][-1] for i in range(len(snail_map))]
        snail_map = [snail_map[i][:-1] for i in range(len(snail_map))]
    else:
        values = [snail_map[i][0] for i in reversed(range(len(snail_map)))]
        snail_map = [snail_map[i][1:] for i in range(len(snail_map))]
    return values, snail_map

def snail(snail_map):
    sorted = []
    left = True
    down = True
    number_of_paths = len(snail_map) + len(snail_map) - 1
    for path in range(number_of_paths):
        if path%2==0:
            #Even paths go left or right
            values, snail_map = get_horizontal_values(left, snail_map)
            left = not left
        else:
            #Odd paths go up or down
            values, snail_map = get_vertical_values(down, snail_map)
            down = not down
        sorted.extend(values)
    return sorted
