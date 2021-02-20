class Queue_array:
    def __init__(self):
        self.queue = [] # queue 저장할 리스트
        self.f = 0 # queue의 front idx
        self.r = -1 # queue의 rear idx
    
    def size(self)-> int: # queue의 크기 반환하는 함수
        return len(self.queue)

    def empty(self)-> bool: # queue가 비어있는지 여부를 반환하는 함수
        return len(self.queue)==0
    
    def front(self)-> object: # front의 element를 반환하는 함수
        if self.empty(): # queue가 비었다면
            print('queue is empty')
        else:
            return self.queue[self.f]
    
    def rear(self)-> object: # rear의 element를 반환하는 함수
        if self.empty(): # queue가 비었다면
            print('queue is empty')
        else:
            return self.queue[self.r]
    
    def enqueue(self, data: object): # rear에 element 추가
        self.queue.append(data)
        self.r += 1
    
    def dequeue(self): # front의 element 제거
        if self.empty(): # queue가 비었다면
            print('queue is empty')
        else:
            self.queue.pop(0)
            self.r -= 1