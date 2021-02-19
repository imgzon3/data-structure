class Stack_array: # 배열을 기반으로 한 스택
    def __init__(self): # 파이썬에서는 list의 크기 제한이 없으므로, 자유롭게 사용한다.
        self.stack = [] # 배열
        self.t = -1 # 초기 top의 index -1로 초기화
    
    def size(self)-> int: # 스택의 원소 개수를 반환하는 함수
        return len(self.stack)
    
    def empty(self)-> bool: # 스택이 비었는지 확인하는 함수
        return len(self.stack) == 0
    
    def top(self)-> int: # 스택의 맨 위 원소를 확인하는 함수
        if self.empty(): # 스택이 비어있다면
            return -1
        else:
            return self.stack[self.t] # index t의 값 반환
    
    def push(self, n: int): # 스택의 새로운 값을 push하는 함수
        self.stack.append(n) # python은 리스트의 크기 제한이 없으므로, 바로 append
        self.t += 1 # top index + 1 하기
    
    def pop(self)-> int: # 스택의 top의 값을 삭제하고 반환하는 함수
        if self.empty(): # 스택이 비어있다면
            return -1
        else:
            self.t -= 1 # top index - 1 하기
            return self.stack.pop(-1) # pop함수 실행
    