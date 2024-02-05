class MyCircularQueue:

    def __init__(self, k: int):
        self.data = []
        self.max = k

    def enQueue(self, value: int) -> bool:
        if self.max <= len(self.data):
            return False
        self.data.append(value)
        return True

    def deQueue(self) -> bool:
        if len(self.data) <= 0:
            return False
        self.data.pop(0)
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.data[0]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.data[-1]

    def isEmpty(self) -> bool:
        return len(self.data) <= 0

    def isFull(self) -> bool:
        return  self.max <= len(self.data)

obj = MyCircularQueue(3)
obj.enQueue(1)
obj.enQueue(2)
obj.enQueue(3)
obj.enQueue(4)
obj.deQueue()
obj.enQueue(4)
obj.deQueue()
obj.deQueue()
obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
print(obj.Front())