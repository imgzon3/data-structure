class Node:
    def __init__(self, e: object):
        self.element = e # node가 저장하는 element
        self.front = None # 앞에 있는 node의 주소 저장
        self.back = None # 뒤에 있는 node의 주소 저장

class D_linked_list:
    def __init__(self):
        self.head = None # head에 위치하는 node의 주소 값 저장
        self.tail = None # tail에 위치하는 node의 주소 값 저장
    
    