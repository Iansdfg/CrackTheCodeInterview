class MultiStack:
    def __init__(self, stacksize):
        self.numstack = 3
        self.sizes = [0]*stacksize
        self.arrary = [0]*(stacksize*self.numstack)
        self.stacksize = stacksize

    def Push(self,item, stacknum):
        if self.IsFull(stacknum):
            raise Exception('Stack is full')
        self.sizes[stacknum]+=1
        self.arrary[self.index(stacknum)] = item

    def Pop(self,stacknum):
        if self.IsEmpty(stacknum):
            raise Exception('Stack is empty')
        value = self.arrary[self.index(stacknum)]
        self.arrary[self.index(stacknum)] = 0
        self.sizes[stacknum] -= 1
        return value

    def Peek(self,stacknum):
        if self.IsEmpty(stacknum):
            raise Exception('Stack is empty')
        value = self.arrary[self.index(stacknum)]
        return value

    def IsFull(self, stacknum):
        return self.sizes[stacknum] == self.stacksize

    def IsEmpty(self, stacknum):
        return self.sizes[stacknum] == 0

    def index(self, stacknum):
        offset = stacknum*self.stacksize
        return offset+self.sizes[stacknum]-1

def ThreeInOne():
    newstack = MultiStack(2)
    print(newstack.IsEmpty(1))
    newstack.Push(3, 1)
    print(newstack.Peek(1))
    print(newstack.IsEmpty(1))
    newstack.Push(2, 1)
    print(newstack.Peek(1))
    print(newstack.Pop(1))
    print(newstack.Peek(1))
    newstack.Push(3, 1)

ThreeInOne()
