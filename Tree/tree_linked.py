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
5. print_tree: tree 출력
'''

class Node:
    def __init__(self, e: object):
        self.element = e
        self.parent = None
        self.child = []
    
    def insert_child(self, n): # 해당 node에 자식을 삽입할 때 사용하는 함수
        self.child.append(n)
    
    def del_child(self, n): # 현재 node의 자식 node 중 특정 node를 제거
        for i in self.child:
            if i==n:
                self.child.remove(i)
                break
            
    
    def set_parent(self, n): # 현재 node의 부모를 바꾸는 함수
        self.parent = n

class Tree:
    def __init__(self, e: object): # root가 될 node의 element 받음
        node = Node(e) # root가 될 node
        self.root = node
        self.node_list = [] # 해당 tree node의 주소들을 저장해 놓는 list
        self.node_list.append(node)
    
    def size(self)-> int: # 해당 tree의 크기 반환
        return len(self.node_list)
    
    def insert_node(self, par_el: object, el: object): # 해당 부모 node를 찾고, 자식 node를 만들어 추가
        node = Node(el)
        tmp = True
        for i in self.node_list:
            if i.element==par_el:
                i.insert_child(node) # 자식에 추가
                self.node_list.append(node) # tree의 node 리스트에 추가
                node.parent = i
                tmp = False
                break
        
        if tmp: # 해당 부모 node가 없다면
            print(f'error: there is no node with {par_el}')
    
    def del_node(self, el: object): # 해당 node 삭제, 자식 node들을 부모의 자식으로 추가
        tmp = True
        for i in self.node_list:
            if i.element==el:
                tmp_chi = i.child
                tmp_par = i.parent
                tmp_par.del_child(i) # 부모에서 해당 node 제거
                for k in tmp_chi:
                    tmp_par.insert_child(k)
                self.node_list.remove(i) # tree의 node 리스트에 제거
                tmp = False
                break
            
        if tmp: # 해당 element를 지닌 node가 없다면
            print(f'error: there is no node with {el}')
    
    def print_chi(self, el: object): # 해당 node의 자식들 출력함
        tmp = True
        for i in self.node_list:
            if i.element==el:
                if len(i.child)==0:
                    print(f'There is no child for node:{el}')
                    tmp = False
                else:
                    res_list = []
                    for k in i.child:
                        res_list.append(k.element)
                    print(f'child list: {res_list}')
                    tmp = False
        
        if tmp:
            print(f'error: there is no node with {el}')
    
    def print_sib(self, el: object): # 해당 node와 같은 부모를 가지는 node 출력
        tmp = True
        for i in self.node_list:
            if i.element==el:
                tmp_par = i.parent
                res_list = []
                for k in tmp_par.child:
                    res_list.append(k.element)
                print(f'sibling list: {res_list}')
                tmp = False
                break
            
        if tmp:
            print(f'error: there is no node with {el}')

if __name__ == "__main__":
    root = input('input your element for root(int): ')
    tree = Tree(int(root)) # 입력받은 root값으로 tree 생성
    n = input('input how many functions you will use: ') # 반복할 입력 값 수
    
    for _ in range(int(n)):
        request = input()
        if 'size' in request:
            print(tree.size())
        elif 'insert' in request:
            tmp, par_el, chi_el = map(str, request.split())
            par_el = int(par_el)
            chi_el = int(chi_el)
            tree.insert_node(par_el, chi_el)
        elif 'delete' in request:
            tmp, el = map(str, request.split())
            el = int(el)
            tree.del_node(el)
        elif 'print' in request:
            tmp, el = map(str, request.split())
            el = int(el)
            select = int(input('What will you print?(1: child, 2:siblings, 3:tree): '))
            if select==1:
                tree.print_chi(el)
            elif select==2:
                tree.print_sib(el)
            elif select==3:
                pass
            else:
                print('error:out of range(1~3 needed)')
        else:
            print(f'There is no function named{request}\n(size, insert, delete, print are functions we have)')