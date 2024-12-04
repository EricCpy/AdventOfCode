def solution():
    dirs = [
        (-1, 0), (1, 0), (0, -1), (0, 1),  # Up, Down, Left, Right
        (-1, -1), (-1, 1), (1, -1), (1, 1) # Diagonals
    ]
    
    with open('./Day04/input.txt', 'r') as f:
        data = f.read().splitlines()

    search_word = "XMAS"
    word_length = len(search_word)
    ans = 0

    for x in range(len(data)):
        for y in range(len(data[x])):
            for dx, dy in dirs:
                found_word = True
                for i in range(word_length):
                    nx = x + dx * i
                    ny = y + dy * i
                    if (
                        nx < 0 or nx >= len(data) or 
                        ny < 0 or ny >= len(data[nx]) or 
                        data[nx][ny] != search_word[i]
                    ):
                        found_word = False
                        break
                    
                if found_word:
                    ans += 1

    return ans


def solution2():
    def search_word(data, x, y, dx, dy, word):
        for i in range(len(word)):
            nx, ny = x + dx * i, y + dy * i
            if (
                nx < 0 or nx >= len(data) or
                ny < 0 or ny >= len(data[nx]) or
                data[nx][ny] != word[i]
            ):
                return False
            
        return True

    with open('./Day04/input.txt', 'r') as f:
        data = f.read().splitlines()

    ans = 0
    words = ["SAM", "MAS"]

    for x in range(len(data)):
        for y in range(len(data[x])):
            word1 = any(search_word(data, x, y, 1, 1, word) for word in words)
            word2 = any(search_word(data, x, y + 2, 1, -1, word) for word in words)
            if word1 and word2:
                ans += 1

    return ans

if __name__ == "__main__":
    print(solution())
    print(solution2())