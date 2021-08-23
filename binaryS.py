from collections import namedtuple

Node = namedtuple('Node', ['left', 'right', 'value'])

def contains(root, value):
    parent = root
    while(True):
        if parent.value == value:
            return True
        elif (parent.left != None and parent.value > value):
            parent = parent.left
        elif (parent.right != None and parent.value < value):
            parent = parent.right
        else:
            return False
        
n1 = Node(value=1, left=None, right=None)
n3 = Node(value=3, left=None, right=None)
n2 = Node(value=2, left=n1, right=n3)
        
print(contains(n2, 3))