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
        list_size = 1
        our_node = self.head # head에서 시작
        
        if self.Empty(): # 비어있다면 0 return
            return 0
        else:
            while True:
                if our_node.next == None: # 다음 node가 없다면
                    break
                else: # 다음 node가 있다면
                    list_size += 1
                    our_node = our_node.next
            return our_node
    
    def Print(self)-> int: # 연결 리스트의 elements를 출력하는 함수
        our_node = self.head
        
        if self.Empty(): # 리스트가 비어있다면 -1 return
            return -1
        else:
            while True:
                print(our_node.data)
                if our_node.next == None:
                    break
                else:
                    our_node = our_node.next