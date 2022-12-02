import re

def solution():
    f = open("input.txt")
    res, res2 = 0, 0
    dic = {'A': 1, 'B': 2, 'C': 3, 'X': 1, 'Y': 2, 'Z': 3}
    loseWindic = {'X': 0, 'Y': 3, 'Z': 6}
    regex = re.compile('[^a-zA-Z]')
    for x in f:
        x = regex.sub('', x)
        res += dic[x[1]]
        res2 += loseWindic[x[1]]
        
        if loseWindic[x[1]] == 3: #falls draw
            res2 += dic[x[0]]
        elif loseWindic[x[1]] == 6: #falls win
            res2 += (dic[x[0]] + 1) % 4 + (int) ((dic[x[0]] + 1) / 4)
        else: #falls lose
            res2 += (dic[x[0]] + 2) % 4 + (int) ((dic[x[0]] + 2) / 4)
        
        if dic[x[0]] == dic[x[-1]]: # falls draw
            res += 3
        elif (dic[x[-1]] + 2) % 3 == dic[x[0]] % 3: # falls win
            res += 6
        
    return res, res2

if __name__ == "__main__":
    print(solution())