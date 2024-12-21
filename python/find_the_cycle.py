'''

Count da Loop 

You are given a node that is the beginning of a linked list. This list contains a dangling piece and a loop. Your objective is to determine the length of the loop.

'''

def loop_size(node):
    start_node = node
    next_node = node.next
    next_next_node = next_node.next
    loop_size = 1
    while start_node != next_node and start_node != next_next_node and next_node != next_next_node:
        start_node = start_node.next
        next_node = next_node.next
        next_next_node = next_next_node.next.next
    start_node = next_next_node.next
    while start_node != next_next_node:
        loop_size += 1
        start_node = start_node.next
    return loop_size 
