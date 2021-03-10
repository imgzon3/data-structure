'''
linear probing hashing
필요 함수
1. put
2. del
3. show
4. find
'''
class Hashtable:
    def __init__(self):
        self.table = [None for _ in range(13)]
    
    def full(self)-> bool:
        tmp = True
        for i in self.table:
            if not(i):
                tmp = False
                break
        return tmp
    
    def put(self, key: int, value: str):
        if not(self.full()):
            while True:
                if not(self.table[key%13]):
                    self.table[key%13] = value
                else:
                    key += 1
    
    def del(self, key: int)-> str:
        while True:
            if self.table[key%13]:
                print(f'There is no value in {key}')
                break
            else:
                if self.table[key%13] == False:
                    key += 1
                else:
                    tmp = self.table[key%13]
                    self.table[key%13] = False
                    return tmp


if __name__ == '__main__':
    hashing = Hashtable()
    