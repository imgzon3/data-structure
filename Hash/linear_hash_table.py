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
    
    def put(self, key: int, value: str):
        while True:
            if not(self.table[key%13]):
                self.table[key%13] = value
            else:
                key += 1

if __name__ == '__main__':
    hashing = Hashtable()
    