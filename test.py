class Node:
    def __init__(self, i: int):
        self.data = i
        self.left = self.right = None
        self.parent = None
        
if __name__ == "__main__":
    root = Node(1)
    tmp = Node(2)
    root.right = tmp
    print(type(tmp.right))