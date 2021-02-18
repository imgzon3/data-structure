class Test:
    def __init__(self, num:int):
        self.num = num
    
    def Empty(self)-> int:
        if self.num == 1:
            return 1
        else:
            return 0
    
    def Pass(self)-> int:
        if self.Empty():
            return 1
        else:
            return 0

if __name__ == "__main__":
    test = Test(1)
    print(test.Empty())
    print(test.Pass())