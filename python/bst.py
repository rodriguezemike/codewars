#https://www.codewars.com/kata/571a551a196bb0567f000603/train/python

class Tree(object):
    
    def __init__(self, root, left=None, right=None):
        assert root and type(root) == Node
        if left: assert type(left) == Tree and left.root < root
        if right: assert type(right) == Tree and root < right.root

        self.left = left
        self.root = root
        self.right = right
        
    def is_leaf(self):
        return not(self.left or self.right)
        
    def __str__(self):
        if self.is_leaf():
            return ("[%s]" % str(self.root))
        elif not self.left:
            return "[_ %s %s]" % (str(self.root),self.right.__str__())
        elif not self.right:
            return "[%s %s _]" % (self.left.__str__(),str(self.root))
        else:
            return "[%s %s %s]" % (self.left.__str__(), str(self.root), self.right.__str__())
    
    def __eq__(self, other):
        if other is None or not self.root == other.root or not self.left == other.left or not self.right == other.right:
            return False
        return True
    
    def __ne__(self, other):
        return not self.__eq__(other)

class Node(object):
    
    def __init__(self, value, weight=1):
        self.value = value
        self.weight = weight
    
    def __str__(self):
        return str(self.value)   
    
    def __lt__(self, other):
        return self.value < other.value
    
    def __gt__(self, other):
        return self.value > other.value
    
    def __eq__(self, other):
        return self.value == other.value 

    def __ne__(self, other):
        return self.value != other.value 

