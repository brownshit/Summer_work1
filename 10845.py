class Queue:
    #left to right, moving elements
    def __init__(self):
        self.queue = []
    def push(self,num):
        self.queue.insert(0,num)
    def pop(self):
        if self.queue:return self.queue.pop()
        else:return -1
    def size(self):
        return len(self.queue)
    def empty(self):
        if self.queue:return 0
        else: return 1
    def front(self):
        if self.queue:return self.queue[-1]
        else: return -1
    def back(self):
        if self.queue:return self.queue[0]
        else: return -1

que = Queue()

n = int(input())
commands = [input().split() for _ in range(n)]

for command in commands:
    if command[0] == 'push':
        que.push(int(command[1]))
    elif command[0] == 'pop':
        print(que.pop())
    elif command[0] == 'size':
        print(que.size())
    elif command[0] == 'empty':
        print(que.empty())
    elif command[0] == 'front':
        print(que.front())
    elif command[0] == 'back':
        print(que.back())
    
