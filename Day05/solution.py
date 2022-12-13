from collections import deque
import re, copy

def solution():
    f = open("input.txt").read().splitlines()
    stacks = [deque() for _ in range((len(f[0]) + 1) // 4)]
    startLine = 0
    
    for s, x in enumerate(f):
        if x[1].isdigit():
            startLine = s
            break
        for i, c in enumerate(x[1:len(x):4]):
           if c.isalpha():
               stacks[i].appendleft(c)
    
    rx = re.compile('[a-z]')         
    instructions = [[int(x) - 1 for x in (rx.sub('', y)).strip().split('  ')] for y in f[startLine+2:]]
    
    return result9000(copy.deepcopy(stacks), instructions), result9001(copy.deepcopy(stacks), instructions)
       
def result9000(stacks, instructions):
    for x in instructions:
        for _ in range(x[0]+1):
            stacks[x[2]].append(stacks[x[1]].pop())

    return ''.join([x[-1] for x in stacks])

def result9001(stacks, instructions):
    for x in instructions:
        tmp = []
        for _ in range(x[0] + 1):
            tmp.append(stacks[x[1]].pop())

        tmp.reverse()
        stacks[x[2]].extend(tmp)

    return ''.join([x[-1] for x in stacks])


if __name__ == "__main__":
    print(solution())