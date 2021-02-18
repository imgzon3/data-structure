class Node: # class Node
    def __init__(self, data: int):
        self.data = data # 저장하는 데이터 값
        self.next = None # 다음 node의 주소값 저장

class S_linked_list:
    def __init__(self): # 선언시 head와 tail값은 None
        self.head = None
        self.tail = None
    
    def Empty(self)-> int: # 리스트가 비어있는지 확인하는 함수
        if self.head == None and self.tail == None:
            return 1 # 비어있다면 1 return
        else:
            return 0 # 비어있지 않다면 0 return
    
    def List_size(self)-> int: # 리스트의 크기를 반환하는 함수
        self.list_size = 1
        self.our_node = None
        
        self.our_node = self.head # head에서 시작
        if self.Empty(): # 비어있다면 0 return
            return 0
        else:
            while True:
                if self.our_node.next == None: # 다음 node가 없다면
                    break
                else: # 다음 node가 있다면
                    self.list_size += 1
                    