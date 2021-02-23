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
    
    def insert_child(self, n:Node): # 해당 node에 자식을 삽입할 때 사용하는 함수
        self.child.append(n)
    
    def del_child(self, n:Node): # 현재 node의 자식 node 중 특정 node를 제거
        for i in self.child:
            if i==n:
                self.child.remove(i)
                break
            
    
    def set_parent(self, n:Node): # 현재 node의 부모를 바꾸는 함수
        self.parent = n

class Tree:
    def __init__(self, e: object): # root가 될 node의 element 받음
        node = Node(e) # root가 될 node
        self.root = node
        self.node_list = [] # 해당 tree node의 주소들을 저장해 놓는 list
        self.node_list.append(node)
    
    def insert_node(self, par_el: object, el: object): # 해당 부모 node를 찾고, 자식 node를 만들어 추가
        node = Node(el)
        tmp = True
        for i in self.node_list:
            if i.element==par_el:
                i.child.append(node) # 자식에 추가
                self.node_list.append(node) # tree의 node 리스트에 추가
                tmp = False
                break
        
        if tmp: # 해당 부모 node가 없다면
            print(f'error: there is no node with {par_el}')