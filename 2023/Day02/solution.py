def solution_1():
    with open('./Day02/input.txt', 'r') as f:
        data = f.read().splitlines()
    
    overall = 0
    for line in data:
        g = line.split(" ")
        game_idx = int(g[1][:-1])
        for bag in line.split("; "):
            if game_idx == 0:
                continue
            bag = bag.replace(",", "")
            game = bag.split(" ")
            blue_idx = game.index("blue") if "blue" in game else - 1
            red_idx = game.index("red") if "red" in game else - 1
            green_idx = game.index("green") if "green" in game else - 1
            
            if greater_than(game, blue_idx, 14) or greater_than(game, red_idx, 12) or greater_than(game, green_idx, 13):
                game_idx = 0
                
                
        overall += game_idx
        
    return overall

def greater_than(game, curr, max):
    if curr == -1:
        return False
    
    if int(game[curr- 1]) > max:
        return True
    
    return False


def solution_2():
    with open('./Day02/input.txt', 'r') as f:
        data = f.read().splitlines()
    
    res = 0
    for line in data:
        blue_max = 0
        red_max = 0
        green_max = 0
        for bag in line.split("; "):
            bag = bag.replace(",", "")
            game = bag.split(" ")
            blue = int(game[game.index("blue")-1]) if "blue" in game else 0
            red= int(game[game.index("red")-1])  if "red" in game else 0
            green= int(game[game.index("green")-1])  if "green" in game else 0
            
            blue_max = max(blue, blue_max)
            green_max = max(red, green_max)
            red_max = max(green, red_max)
                
                
        res += blue_max * red_max * green_max
        
    return res


if __name__ == "__main__":
    print(solution_1())
    print(solution_2())