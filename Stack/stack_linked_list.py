class Node: # class Node
    def __init__(self, data: int):
        self.data = data # 저장하는 데이터 값
        self.next = None # 다음 node의 주소값 저장

class S_linked_list:
    def __init__(self): # 선언시 head와 tail값은 None
        self.head = None
        self.tail = None
    
    def empty(self)-> bool: # 리스트가 비어있는지 확인하는 함수
        if self.head == None and self.tail == None:
            return 1 # 비어있다면 1 return
        else:
            return 0 # 비어있지 않다면 0 return
    
    def peek(self)-> int: # tail값을 반환
        if self.empty(): # 비어있다면 -1 return
            return -1
        else:
            return self.head.data
    
    def list_size(self)-> int: # 리스트의 크기를 반환하는 함수
        list_size = 1
        our_node = self.head # head에서 시작
        
        if self.empty(): # 비어있다면 0 return
            return 0
        else:
            while True:
                if our_node.next == None: # 다음 node가 없다면
                    break
                else: # 다음 node가 있다면
                    list_size += 1
                    our_node = our_node.next
            return list_size
    
    def append(self, data: int): # 연결 리스트에 node를 추가하는 함수
        node = Node(data)
        
        if self.empty(): # 리스트가 비어있다면, head와 tail 지정해주기
            self.head = node
            self.tail = node
        else: # head가 가리키는 node 변경 후 head 변경
            node.next = self.head
            self.head = node
    
    def delete(self)-> int: # head에 해당하는 node를 삭제하고, 그 node의 data 출력
        if self.empty(): # 연결 리스트가 비어있는 경우
            return -1
        elif self.list_size() == 1: # 스택에 데이터가 1개밖에 남아있지 않은 경우
            tmp = self.head.data
            self.head = self.head.next
            self.tail = None
            return tmp
        else: # head node 제거
            tmp = self.head.data
            self.head = self.head.next
            return tmp

class Stack_linked:
    def __init__(self):
        self.stack = S_linked_list() # singly linked list기반 저장
        self.t = -1 # top index -1로 default
    
    def size(self)->int: # 스택의 크기 return
        return self.stack.list_size()
    
    def empty(self)-> bool: # 스택이 비었는지 여부 return
        return self.empty()
    
    