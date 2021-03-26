'''
binary search tree
함수 목록
1. insert
2. delete
3. get
'''
class Node:
    def __init__(self, i: int):
        self.data = i
        self.left = self.right = None

class SearchTree:
    def __init__(self, i: int):
        self.root = Node(i)

if __name__ == "__main__":
    