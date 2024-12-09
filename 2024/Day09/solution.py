def solution():
    with open('./Day09/input.txt', 'r') as f:
        data = [int(x) for x in f.read()]
    
    j = len(data) - 1
    curr_front = 0
    curr_back = len(data) // 2
    compressed = []
    for i, num in enumerate(data):
        if i % 2 == 0:
            for _ in range(num):
                compressed.append(curr_front)
            curr_front += 1
            data[i] = 0    
        else:
            idx = 0
            while idx < num and j >= 0:  
                if data[j] != 0:
                    data[j] -= 1
                    idx += 1
                    compressed.append(curr_back)
                else:
                    j -= 2
                    curr_back -= 1
    
    ans = 0
    for idx, x in enumerate(compressed):
        ans += idx * int(x)
    
    return ans


def solution2():
    with open('./Day09/input.txt', 'r') as f:
        data = [int(x) for x in f.read()]
    
    curr_front = 0
    compressed = []
    used = [False for x in range(len(data))]
    for i, num in enumerate(data):
        if i % 2 == 0:
            for _ in range(num):
                if used[i]:
                    compressed.append(".")
                else:
                    compressed.append(curr_front)
            curr_front += 1
            used[i] = True    
        else:
            j = len(data) - 1
            back = len(data) // 2
            while j > i and num > 0:
                if used[j] is not True and data[j] <= num:
                    for _ in range(data[j]):
                        compressed.append(back)
                    num -= data[j]
                    used[j] = True

                back-=1
                j-=2
            
            for x in range(num):
                compressed.append(".")
    
    
    ans = 0
    for idx, x in enumerate(compressed):
        if x != '.':
            ans += idx * int(x)
    
    return ans


if __name__ == "__main__":
    print(solution())
    print(solution2())