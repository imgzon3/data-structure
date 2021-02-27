'''
heap 필요한 것
1. 저장할 배열
2. min-heap, max-heap 구별(+1, -1입력받고, 곱해서 구별하기)

heap functions
1. swap()
2. upheap()
3. downheap()
4. insert()
5. pop()
6. top()
7. size()
8. print()
9. is_empty()
10. find()
'''
class Heap:
    def __init__(self, dir: int): # 1 입력받으면 min-heap, -1 입력받으면 max-heap
        self.array = [-1] # 0번째 index값은 사용 안함
        self.dir = dir