class Node:
    def __init__(self, e: object):
        self.element = e # node가 저장하는 element
        self.front = None # 앞에 있는 node의 주소 저장
        self.back = None # 뒤에 있는 node의 주소 저장

class D_linked_list:
    def __init__(self):
        self.head = None # head에 위치하는 node의 주소 값 저장
        self.tail = None # tail에 위치하는 node의 주소 값 저장
    
    def empty(self)-> bool: # list의 비었는지 여부를 반환하는 함수
        if self.head==None and self.tail==None:
            return 1
        else:
            return 0
    
    def size(self)-> int: # list의 크기를 반환하는 함수
        tmp = 1
        cur_node = self.head
        
        if self.empty(): # list가 비어있다면
            return 0
        else:
            while True:
                if cur_node.back==None:
                    break
                else:
                    cur_node = cur_node.back
                    tmp += 1
            return tmp
    
    def begin(self)-> object: # list의 앞의 element 반환
        return self.head.element
    
    def end(self)-> object: # list의 뒤의 element 반환
        return self.tail.element
    
    