class Monkey(object):
    def __init__(self, worry = 1, operation = None, operator = '+', test = 3, trueM = 0, falseM = 0):
        self.items = []
        self.operation = operation
        self.operator = operator
        self.test = test
        self.trueM = trueM
        self.falseM = falseM
        self.inspects = 0
        self.worry = worry
        self.divisor = 0
        
    def make_move(self, monkeys):
        for item in self.items:
            self.inspects += 1
            item = item % self.divisor
            new = self.calc(item) // self.worry
            if new % self.test == 0:
                monkeys[self.trueM].items.append(new)
            else: 
                monkeys[self.falseM].items.append(new)
                
        self.items = []
           
    def calc(self, item):
        if self.operator == '+':
            if not self.operation:
                return item + item
            return item + self.operation
        else:
            if not self.operation:
                return item * item
            return item * self.operation

def solution(rounds=20, worryDivisor = 1):
    with open('input.txt', 'r') as f:
        data = f.read().splitlines()
    
    monkeys = [] # List of monkeys
    
    #init monkeys
    monkey = None
    for x in data:
        s = x.split()
        if len(s) == 0:
            continue
        
        if s[0] == "Monkey":
            monkey = Monkey(worryDivisor)
            monkeys.append(monkey)
        elif s[0] == "Starting":
            for i in s[2:]:
                monkey.items.append((int) (i.replace(',', '')))  
        elif s[0] == "Operation:":
            monkey.operator = s[4]
            if s[-1].isdigit():
                monkey.operation = (int) (s[-1])  
        elif s[0] == "Test:":
            monkey.test = (int) (s[-1])
        elif s[0] == "If":
            if s[1] == "true:":
                monkey.trueM = (int) (s[-1])
            else:
                monkey.falseM = (int) (s[-1])
    
    #commonDivisor
    cd = 1
    for m in monkeys:
        cd *= m.test
    
    #set divisor in monkeys
    for m in monkeys:
        m.divisor = cd
    
    #make_moves
    for i in range(rounds):
        for m in monkeys:
            m.make_move(monkeys)
    
    #get firstMax and secondMax
    firstMax = 0
    secondMax = 0
    for m in monkeys:
        if firstMax < m.inspects:
            secondMax = firstMax
            firstMax = m.inspects
        elif secondMax < m.inspects:
            secondMax = m.inspects
    
    return firstMax * secondMax
    
if __name__ == "__main__":
    print(solution(20, 3))
    print(solution(10000))