'''
heap 필요한 것
1. 저장할 배열
2. min-heap, max-heap 구별(+1, -1입력받고, 곱해서 구별하기)

heap functions
0. is_empty()
1. swap()
2. upheap()
3. downheap()
4. insert()
5. pop()
6. top()
7. size()
8. print()
9. find()
'''
class Heap:
    def __init__(self, dir: int): # 1 입력받으면 min-heap, -1 입력받으면 max-heap
        self.array = [-1] # 0번째 index값은 사용 안함
        self.dir = dir
    
    def is_empty(self)-> bool: # heap의 빈 여부 반환
        return len(self.array)==1
    
    def swap(self, idx1: int, idx2: int): # 입력받은 2개의 inx에 저장되어 있는 값을 서로 바꿈
        self.array[0] = self.array[idx1]
        self.array[idx1] = self.array[idx2]
        self.array[idx2] = self.array[idx1]
    
    