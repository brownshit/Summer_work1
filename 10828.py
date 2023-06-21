class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, x):
        self.stack.append(x)
    
    def pop(self):
        if self.stack:
            return self.stack.pop()
        else:
            return -1
    
    def size(self):
        return len(self.stack)
    
    def empty(self):
        return 0 if self.stack else 1
    
    def top(self):
        if self.stack:
            return self.stack[-1]
        else:
            return -1

# 입력 받기
n = int(input())
commands = [input().split() for _ in range(n)]

# 스택 인스턴스 생성
stack = Stack()

# 명령 처리 및 결과 출력
for command in commands:
    if command[0] == 'push':
        stack.push(int(command[1]))
    elif command[0] == 'pop':
        print(stack.pop())
    elif command[0] == 'size':
        print(stack.size())
    elif command[0] == 'empty':
        print(stack.empty())
    elif command[0] == 'top':
        print(stack.top())
