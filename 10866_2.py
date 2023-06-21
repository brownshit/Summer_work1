import sys
from collections import deque

# 빠른 입력을 위한 sys.stdin.readline() 사용
input = sys.stdin.readline

# 덱(Deque) 객체 생성
deque_obj = deque()

# 명령의 수 입력
n = int(input())

# 결과를 저장할 리스트
result = []

# 명령 처리
for _ in range(n):
    command = input().split()
    
    if command[0] == 'push_front':
        deque_obj.appendleft(int(command[1]))
    elif command[0] == 'push_back':
        deque_obj.append(int(command[1]))
    elif command[0] == 'pop_front':
        if deque_obj:
            result.append(deque_obj.popleft())
        else:
            result.append(-1)
    elif command[0] == 'pop_back':
        if deque_obj:
            result.append(deque_obj.pop())
        else:
            result.append(-1)
    elif command[0] == 'size':
        result.append(len(deque_obj))
    elif command[0] == 'empty':
        if deque_obj:
            result.append(0)
        else:
            result.append(1)
    elif command[0] == 'front':
        if deque_obj:
            result.append(deque_obj[0])
        else:
            result.append(-1)
    elif command[0] == 'back':
        if deque_obj:
            result.append(deque_obj[-1])
        else:
            result.append(-1)

# 결과 출력
sys.stdout.write('\n'.join(map(str, result)))
