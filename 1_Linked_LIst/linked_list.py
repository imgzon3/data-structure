class Node: # class Node
    def __init__(self, data: int):
        self.data = data # 저장하는 데이터 값
        self.next = None # 다음 node의 주소값 저장

class S_linked_list:
    def __init__(self): # 선언시 head와 tail값은 None
        self.head = None
        self.tail = None
    
    def empty(self)-> int: # 리스트가 비어있는지 확인하는 함수
        if self.head == None and self.tail == None:
            return 1 # 비어있다면 1 return
        else:
            return 0 # 비어있지 않다면 0 return
    
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
    
    def print(self)-> str: # 연결 리스트의 elements를 출력하는 함수
        our_node = self.head
        tmp = ''
        
        if self.empty(): # 리스트가 비어있다면 -1 return
            return '-1'
        else:
            while True:
                tmp += str(our_node.data) + ' '
                if our_node.next == None:
                    break
                else:
                    our_node = our_node.next
            return tmp
    
    def append(self, data: int): # 연결 리스트에 node를 추가하는 함수
        node = Node(data)
        
        if self.empty(): # 리스트가 비어있다면, head와 tail 지정해주기
            self.head = node
            self.tail = node
        else: # tail이 가리키는 node 변경 후 tail 변경
            self.tail.next = node
            self.tail = node
    
    def delete(self, idx: int)-> int: # idx에 해당하는 node를 삭제하고, 그 node의 data 출력
        location = 0 # 현재 위치
        cur_node = self.head
        pre_node = None
        
        if self.empty() or self.list_size() < idx: # 연결 리스트가 비어있거나, 벗어나는 값을 받은 경우
            return -1
        elif idx == 0: # 0번째 idx를 삭제하는 경우(head)
            tmp = self.head.data
            self.head = self.head.next
            return tmp
        else: # pre_node와 cur_node로 해당하는 idx의 node를 제거
            while True:
                if location == idx:
                    tmp = cur_node.data
                    pre_node.next = cur_node.next
                    break
                else:
                    pre_node = cur_node
                    cur_node = cur_node.next
                    location += 1
            return tmp

if __name__ == "__main__": # 테스트 해보기
    s_list = S_linked_list()
    print('made s_list')
    print(f's_list.empty(): {s_list.empty()}')
    print(f's_list.list_size(): {s_list.list_size()}')
    print(f's_list.print(): {s_list.print()}')
    print()
    
    s_list.append(1)
    print('append 1')
    print(f's_list.empty(): {s_list.empty()}')
    print(f's_list.list_size(): {s_list.list_size()}')
    print(f's_list.print(): {s_list.print()}')
    print()
    
    s_list.append(2)
    s_list.append(3)
    s_list.append(4)
    print('append 2, 3, 4')
    print(f's_list.empty(): {s_list.empty()}')
    print(f's_list.list_size(): {s_list.list_size()}')
    print(f's_list.print(): {s_list.print()}')
    print()
    
    print('delete 3')
    print(f's_list.delete(3):{s_list.delete(3)}')
    print(f's_list.empty(): {s_list.empty()}')
    print(f's_list.list_size(): {s_list.list_size()}')
    print(f's_list.print(): {s_list.print()}')
    print()