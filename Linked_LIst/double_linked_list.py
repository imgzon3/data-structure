class Node:
    def __init__(self, e: object):
        self.element = e # node가 저장하는 element
        self.front = None # 앞에 있는 node의 주소 저장
        self.back = None # 뒤에 있는 node의 주소 저장

class D_linked_list:
    def __init__(self):
        self.head = Node('head') # head역할을 하는 node 지정
        self.tail = Node('tail') # tail역할을 하는 node 지정
    
    def empty(self)-> bool: # list의 비었는지 여부를 반환하는 함수
        if self.head.back==None and self.tail.front==None:
            return 1
        else:
            return 0
    
    def size(self)-> int: # list의 크기를 반환하는 함수
        tmp = 1
        cur_node = self.head.back
        
        if self.empty(): # list가 비어있다면
            return 0
        else:
            while True:
                if cur_node.back.back==None:
                    break
                else:
                    cur_node = cur_node.back
                    tmp += 1
            return tmp
    
    def begin(self)-> object: # list의 앞의 element 반환
        if self.empty():
            return None
        else:
            return self.head.back.element
    
    def end(self)-> object: # list의 뒤의 element 반환
        if self.empty():
            return None
        else:
            return self.tail.front.element
    
    def insert(self, i: int, e: object): # list의 index i에 element e 삽입
        node = Node(e)
        pre_node = self.head
        next_node = self.head.back
        tmp = 0
        
        if i>self.size() or i<0: # 찾고자 하는 index가 size보다 크거나, 0보다 작은 경우
            print('out of index')
        elif self.empty() and i==0: # list가 비어있을 경우
            self.head.back = node
            self.tail.front = node
        else:
            while True:
                if tmp==i:
                    break
                else:
                    pre_node = pre_node.back
                    next_node = next_node.back
                    tmp += 1
            pre_node.back = node
            next_node.front = node
            node.front = pre_node
            node.back = next_node
    
    def erase(self, i: int)-> object: # list의 index i에 위치하는 element e 제거
        pre_node = self.head
        next_node = self.head.back
        tmp = 0
        
        if i>=self.size() or i<0: # index가 size보다 크거나 같거나, 0보다 작은 경우
            print('out of index')
            return None
        elif self.empty: # list가 비어있을 경우
            print('list is empty')
            return None
        else:
            while True:
                if tmp==i:
                    break
                else:
                    pre_node = pre_node.back
                    next_node = next_node.back
                    tmp += 1
                pre_node.back = next_node
                next_node.front = pre_node