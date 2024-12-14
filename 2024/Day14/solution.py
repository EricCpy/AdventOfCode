def solution(max_width, max_height, second):
    with open('./Day14/input.txt', 'r') as f:
        data = f.read().splitlines()

    middle_x = max_height // 2
    middle_y = max_width // 2
    quadrants = [0, 0, 0, 0]
    for robot in data:
        s = robot.split(" ")
        positions = s[0][2:].split(",")
        movement  = s[1][2:].split(",")

        x = int(positions[1])
        y = int(positions[0])
        m_x = int(movement[1])
        m_y = int(movement[0])

        x_100 = (x + m_x * second) % max_height
        y_100 = (y + m_y * second) % max_width
        
        if x_100 < middle_x and y_100 < middle_y:
            quadrants[0]+=1
        elif x_100 < middle_x and y_100 > middle_y:
            quadrants[1]+=1
        elif x_100 > middle_x and y_100 < middle_y:
            quadrants[2]+=1
        elif x_100 > middle_x and y_100 > middle_y:
            quadrants[3]+=1
        
    ans = 1
    for q in quadrants:
        ans *= q

    return ans

def solution2(max_width, max_height):    
    min_safety = float('inf')
    best_second = 0
    for second in range(max_height * max_width):
        curr = solution(max_width, max_height, second)
        if curr <= min_safety:
            best_second = second
            min_safety = curr
     
    return best_second

if __name__ == "__main__":
    print(solution(101, 103, 100))
    print(solution2(101, 103))