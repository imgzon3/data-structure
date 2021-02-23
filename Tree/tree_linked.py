'''
Node에 필요한 함수
1. insert_child
2. del_child
3. set_parent

Tree에 필요한 함수
1. insert_node
2. del_node
3. print_chi
4. print_sib
5. print_tree
'''

class Node:
    def __init__(self, e: object):
        self.element = e
        self.parent = None
        self.child = []
    
    def insert_child(self, e:Node): # 해당 node에 자식을 삽입할 때 사용하는 함수
        self.child.append(e)
    
    def del_child(self, e:Node): # 현재 node의 자식 node 중 특정 node를 제거
        for i in self.child:
            if i==e:
                self.child.pop(i)