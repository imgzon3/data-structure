class Stack_array: # 배열을 기반으로 한 스택
    def __init__(self): # 파이썬에서는 list의 크기 제한이 없으므로, 자유롭게 사용한다.
        self.stack = [] # 배열
        self.t = -1 # 초기 top의 index -1로 초기화
    