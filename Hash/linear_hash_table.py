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
            if i==None:
                tmp = False
                break
        return tmp
    
    def put(self, key: int, value: str):
        if not(self.full()):
            while True:
                if self.table[key%13]==None:
                    self.table[key%13] = value
                    break
                else:
                    key += 1
    
    def delete(self, key: int)-> str:
        while True:
            if self.table[key%13]==None:
                print(f'There is no value in {key}')
                break
            else:
                if self.table[key%13] == False:
                    key += 1
                else:
                    tmp = self.table[key%13]
                    self.table[key%13] = False
                    return tmp
    
    def show(self):
        for i in self.table:
            if i!=None:
                if i!=False:
                    print(i)


if __name__ == '__main__':
    hashing = Hashtable()
    nums = [18, 41, 22, 44, 59, 32, 31, 73]
    nums_str = ['18!', '41!', '22!', '44!', '59!', '32!', '31!', '73!']
    for i in range(len(nums)):
        hashing.put(nums[i], nums_str[i])
    
    hashing.show()
    print(hashing.table)