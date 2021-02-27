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
8-2. print_g()
9. find()
'''
class Heap:
    def __init__(self, dir: int): # 1 입력받으면 min-heap, -1 입력받으면 max-heap
        """heap을 생성하는 class입니다.

        Args:
            dir (int): 1이면 mean-heap, -1이면 max-heap
        """
        self.array = [-1] # 0번째 index값은 사용 안함
        self.dir = dir
    
    def is_empty(self)-> bool: # heap의 빈 여부 반환
        return len(self.array)==1
    
    def swap(self, idx1: int, idx2: int): # 입력받은 2개의 inx에 저장되어 있는 값을 서로 바꿈
        self.array[0] = self.array[idx1]
        self.array[idx1] = self.array[idx2]
        self.array[idx2] = self.array[0]
        # print(f'swap {idx1} and {idx2}')
    
    def upheap(self, idx: int): # upheap 진행하는 재귀함수
        if idx == 1: # idx가 root라면
            return
        else:
            parent = idx//2
            if self.array[parent]*self.dir > self.array[idx]*self.dir:
                self.swap(parent, idx)
                self.upheap(parent)
    
    def downheap(self, idx: int): # downheap 진행하는 재귀함수
        left = idx*2
        right = idx*2 + 1
        if right <= len(self.array)-1: # 두 자식이 존재할 경우
            if self.array[left]*self.dir <= self.array[right]*self.dir: # 왼쪽의 자식이 더 작다면(max-heap이면 크다면)
                if self.array[left]*self.dir < self.array[idx]*self.dir:
                    self.swap(idx, left)
                    self.downheap(left)
                else:
                    return
            elif self.array[left]*self.dir > self.array[right]*self.dir: # 오른쪽의 자식이 더 작다면(max-heap이면 크다면)
                if self.array[right]*self.dir < self.array[idx]*self.dir:
                    self.swap(idx, right)
                    self.downheap(right)
                else:
                    return
        elif left <= len(self.array)-1: # 왼쪽의 한 자식만 존재할 경우
            if self.array[left]*self.dir < self.array[idx]*self.dir:
                self.swap(left, idx)
            else:
                return
        else:
            return
    
    def insert(self, e: int): # element e를 대입함
        self.array.append(e)
        self.upheap(len(self.array)-1)
    
    def pop(self)-> int: # heap에 성질에 따라, 최솟값 혹은 최댓값을 반환함
        if self.is_empty:
            print('error: heap is empty')
            return None
        else:
            tmp = self.array[1]
            self.swap(1, len(self.array)-1)
            self.array.pop(-1)
            self.downheap(1)
            return tmp
    
    def top(self)-> int:
        if self.is_empty:
            print('error: heap is empty')
            return None
        else:
            return self.array[1]
    
    def size(self)-> int:
        return len(self.array)-1
    
    def print(self)-> str: # 0번 index를 제외한 저장된 배열을 str으로 변환하여 출력
        tmp = ''
        for idx, i in enumerate(self.array):
            if idx!=0:
                tmp += str(i) + ' '
        return tmp
    
    def print_g(self): # 해당 heap의 모양을 그래프로 출력
        # '─', '┘', '└', '┴', '┌', '┐', '│' 활용
        pass

if __name__ == "__main__":
    heap = Heap(1) # mean-heap 선언
    heap.insert(1)
    print(f'insert 1, heap:{heap.print()}')
    heap.insert(10)
    print(f'insert 10, heap:{heap.print()}')
    heap.insert(3)
    print(f'insert 3, heap:{heap.print()}')
    heap.insert(7)
    print(f'insert 7, heap:{heap.print()}')
    heap.insert(6)
    print(f'insert 6, heap:{heap.print()}')