def solution():
    with open('input.txt', 'r') as f:
        data = f.read().splitlines()
        
    res = 0
    cycle = 20
    register = 1
    crt = [["." for _ in range(40)] for _ in range(6)] 
    for x in data:
        oldCycle = cycle
        oldRegister = register
        if x[0] == 'n':
            addtoCrt(crt, register, cycle - 20)
            cycle += 1
        else:
            num = int(x.split()[-1])
            addtoCrt(crt, register, cycle - 20)
            addtoCrt(crt, register, cycle - 19)
            cycle += 2
            register += num
            
        if cycle % 40 == 0:
            res += (cycle - 20) * oldRegister
        elif cycle % 40 < oldCycle % 40:
            res += (cycle - cycle % 40 - 20) * oldRegister
            
    return res, crt 
        
def addtoCrt(crt, register, crtpos):
     if crtpos % 40 >= register - 1 and crtpos % 40 <= register + 1:
        crt[crtpos // 40][crtpos % 40] = '#'
       
if __name__ == "__main__":
    reg, crt = solution()
    print(reg)
    for x in crt:
        print(x)