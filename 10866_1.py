instruction_dic = {
    '0': 'push_front',
    '1': 'push_back',
    '2': 'pop_front',
    '3': 'pop_back',
    '4': '_size',
    '5': 'empty',
    '6': 'front',
    '7': 'back'
}

class Deck:
    def __init__(self):
        self.decklist = []
        self._size = 0
    
    def push_front(self,num):
        self.decklist.insert(0,num)
        self._size = self._size + 1
    def push_back(self,num):
        self.decklist.append(num)
        self._size = self._size + 1
    def pop_front(self):
        if self._size != 0:    
            buf = self.decklist.pop(0)
            self._size = self._size - 1
            return buf
        else:
            return -1
    def pop_back(self):        
        if self._size != 0:
            buf = self.decklist.pop(self._size - 1)
            self._size = self._size - 1
            return buf
        else:
            return -1
    def size(self):
        return self._size
    def empty(self):
        if self._size == 0:
            return 1
        else:
            return 0
    def front(self):
        if self._size != 0:
            return self.decklist[0]
        else:
            return -1
    def back(self):
        if self._size != 0:
            return self.decklist[self._size - 1]
        else:
            return -1
        
dk = Deck()
while(True):
    instrction_num = eval(input())
    if instrction_num>=1 and instrction_num<=1e4:
        break

"""
push_front X: 정수 X를 덱의 앞에 넣는다.
push_back X: 정수 X를 덱의 뒤에 넣는다.
pop_front: 덱의 가장 앞에 있는 수를 빼고, 그 수를 출력한다. 
    만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
pop_back: 덱의 가장 뒤에 있는 수를 빼고, 그 수를 출력한다. 
    만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
_size: 덱에 들어있는 정수의 개수를 출력한다.
empty: 덱이 비어있으면 1을, 아니면 0을 출력한다.
front: 덱의 가장 앞에 있는 정수를 출력한다. 
    만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
back: 덱의 가장 뒤에 있는 정수를 출력한다. 
    만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
"""
for i in range(instrction_num):
    instruction=input() #this instruction decide present iter should do
    instruction_list = instruction.split()
    
    if instruction_list[0] == instruction_dic['0']:
        dk.push_front(instruction_list[1])
    elif instruction_list[0] == instruction_dic['1']:
        dk.push_back(instruction_list[1])
    elif instruction_list[0] == instruction_dic['2']:
        print(dk.pop_front())
    elif instruction_list[0] == instruction_dic['3']:
        print(dk.pop_back())
    elif instruction_list[0] == instruction_dic['4']:
        print(dk.size())
    elif instruction_list[0] == instruction_dic['5']:
        print(dk.empty())
    elif instruction_list[0] == instruction_dic['6']:
        print(dk.front())
    elif instruction_list[0] == instruction_dic['7']:
        print(dk.back())
    #print(dk.decklist)
    #print(dk._size)
