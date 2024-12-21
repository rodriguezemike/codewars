#https://www.codewars.com/kata/5870fa11aa0428da750000da/train/python/6712f25bfb91b5461b0feb7b

import re

def expansion(match_obj):
    return match_obj.group(0)[0] * int(match_obj.group(1))

def unpack_code(code):
    code = re.sub(r"F(\d+)", expansion, code)
    code = re.sub(r"L(\d+)", expansion, code)
    code = re.sub(r"R(\d+)", expansion, code)
    return code

def move_left_and_right(grid, x, y, direction):
    if direction == "E":
        if x >= len(grid[y])-1:
            for i in range(len(grid)):
                grid[i].append(" ")
            x=len(grid[y])-1
        else:
            x+=1
    elif direction == "W":
        if x <= 0:
            for i in range(len(grid)):
                grid[i].insert(0, " ")
            x=0
        else:
            x -= 1
    return grid, x, y

def move_up_and_down(grid, x, y, direction):
    if direction == "N":
        if y <= 0:
            row = [" " for i in range(len(grid[y]))]
            grid.insert(0, row)
            y=0
        else:
            y -= 1
    elif direction == "S":
        if y >= len(grid) - 1:
            row = [" " for i in range(len(grid[y]))]
            grid.append(row)
            y = len(grid) - 1
        else:
            y+=1
    return grid, x, y

def move(grid, x, y, direction):
    if direction in ["N", "S"]:
        return move_up_and_down(grid, x, y, direction)
    else:
        return move_left_and_right(grid, x, y, direction)

def execute(code):
    clockwise = {
        "E" : "S",
        "S" : "W",
        "W" : "N",
        "N" : "E"
    }
    anticlockwise = {
        "E" : "N",
        "N" : "W",
        "W" : "S",
        "S" : "E"
    }
    direction = "E"
    code = unpack_code(code)
    grid = [["*"]]
    x,y = 0,0
    for c in code:
        if c == "F":
            grid, x, y = move(grid, x, y, direction)
            grid[y][x] = "*"
        else:
            direction = clockwise[direction] if c == "R" else anticlockwise[direction]

    return "\r\n".join(["".join(line) for line in grid])
