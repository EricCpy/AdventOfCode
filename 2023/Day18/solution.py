import sys

N, S, W, O = (-1,0), (1,0), (0,-1), (0,1)
instruction_mapping = {'R': O, 'L': W, 'U': N, 'D': S}
def solution():
    with open('./Day18/input.txt', 'r') as f:
        data = f.read().splitlines()
    
    grid = [['.' for a in range(1000)] for b in range(1000)]
    curr = [200,200]
    grid[200][200] = '#'
    for instruction in data:
        s = instruction.split(' ')
        dir = instruction_mapping[s[0]]
        moves = int(s[1])
        
        for _ in range(moves):
            curr[0] += dir[0]
            curr[1] += dir[1]
            grid[curr[0]][curr[1]] = '#'
            
    ans = 0
    sys.setrecursionlimit(100000)
    result_matrix = flood_fill(grid, 201, 201, '#')
    
    for i in range(len(result_matrix)):
        for j in range(len(result_matrix[i])):
            if result_matrix[i][j] != '.':
                ans += 1
    
    
    return ans
       
def flood_fill(matrix, start_row, start_col, new):
    original= matrix[start_row][start_col]

    if original == new:
        return matrix
    
    def fill(row, col):
        if 0 <= row < len(matrix) and 0 <= col < len(matrix[0]):
            
            if matrix[row][col] == original:
                matrix[row][col] = new

                fill(row - 1, col)
                fill(row + 1, col)
                fill(row, col - 1)
                fill(row, col + 1)

    fill(start_row, start_col)
    
    return matrix       
       
     
        
    
if __name__ == "__main__":
    print(solution())
