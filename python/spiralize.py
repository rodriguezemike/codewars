#https://www.codewars.com/kata/534e01fbbb17187c7e0000c6/train/python

def look_ahead(current_location, current_direction, spiral_map):
    if current_direction == "S":
        path = [spiral_map[i][current_location[1]] for i in range(len(spiral_map))]
        return current_location[0] + 1 >= len(path) or path[min(current_location[0] + 2, len(path) - 1)] == 1
    elif current_direction == "N":
        path = [spiral_map[i][current_location[1]] for i in range(len(spiral_map))]
        return current_location[0] - 1 < 0 or path[max(current_location[0] - 2, 0)] == 1
    elif current_direction == "E":
        path = spiral_map[current_location[0]]
        return current_location[1] + 1 >= len(path) or path[min(current_location[1] + 2, len(path) - 1)] == 1
    else:
        path = spiral_map[current_location[0]]
        return current_location[1] - 1 < 0 or path[max(current_location[1] - 2, 0)] == 1

def should_update_direction(current_location, current_direction, spiral_map):
    return look_ahead(current_location, current_direction, spiral_map)
                
def should_update(current_location, current_direction, spiral_map):
    return not look_ahead(current_location, current_direction, spiral_map)

def update_location(current_location, current_direction, spiral_map, spiral_directions):
    if should_update_direction(current_location, current_direction, spiral_map):
        current_direction = spiral_directions[current_direction]
    if should_update(current_location, current_direction, spiral_map):
        if current_direction == "S":
            current_location[0] += 1
        elif current_direction == "N":
            current_location[0] -= 1
        elif current_direction == "E":
            current_location[1] += 1
        else:
            current_location[1] -= 1
    return current_location, current_direction
    
def spiralize(size):
    print(size)
    spiral_directions = {
        "E" : "S",
        "S" : "W",
        "W" : "N",
        "N" : "E"
    }
    current_direction = "E"
    spiral_map = [[0 for _ in range(size)] for _ in range(size)]
    path_completed = False
    current_location = [0,0]
    path = []
    while not path_completed:
        spiral_map[current_location[0]][current_location[1]] = 1
        past_location = [current_location[0], current_location[1]]
        current_location, current_direction = update_location(current_location, current_direction, spiral_map, spiral_directions)
        if current_location == past_location:
            path_completed = True
        elif current_location in path:
            path_completed = True
            spiral_map[past_location[0]][past_location[1]] = 0
        path.append(past_location)
    return spiral_map
