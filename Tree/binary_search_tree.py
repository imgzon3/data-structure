'''
binary search tree
함수 목록
1. insert
2. delete
3. get
'''
class Node:
    def __init__(self, i: int):
        self.data = i # data 값
        self.left = self.right = None # 두 자식 주소
        self.parent = None # 부모 주소

class SearchTree:
    def __init__(self):
        self.root = None

    def insert(self, nd, i:int): # insert, root 비었으면 root에 삽입, 아닐 시 재귀
        curNode = nd
        if self.root == None: # root가 비어있을 경우
            self.root = tmpNode
        else:
            if curNode.data <= i: # data가 현재 노드의 데이터 보다 크면 오른쪽 node로
                if curNode.right == None:
                    tmp = Node(i)
                    curNode.right = tmp
                    tmp.parent = curNode
                else:
                    insert(curNode.right, i)
            elif curNode.data > i: # data가 현재 노드의 데이터보다 작으면 왼쪽 node로
                if curNode.left == None:
                    tmp = Node(i)
                    curNode.left = tmp
                    tmp.parent = curNode
                else:
                    insert(curNode.left, i)

if __name__ == "__main__":
    searchTree = SearchTree()