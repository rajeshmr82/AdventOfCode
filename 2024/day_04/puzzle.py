def read_input():
    with open((__file__.rstrip("puzzle.py")+"input.txt"), 'r') as input_file:
        return input_file.read()

def parse(input):
    return [list(line) for line in input.splitlines()]

def search_grid(grid, i, j, word):
    row = len(grid)
    col = len(grid[0])    
    if grid[i][j] != word[0]:
        return False
    
    word_len = len(word)

    dir_x = [-1, -1, -1, 0, 0, 1, 1, 1]
    dir_y = [-1, 0, 1, -1, 1, -1, 0, 1]

    for i in range(8):
        x = i + dir_x[i]
        y = j + dir_y[i]

        k = 1
        while k < word_len:
            if x >= row or x < 0 or y >= col or y < 0:
                break
            if grid[x][y] != word[k]:
                break
            x += dir_x[i]
            y += dir_y[i]
            k += 1

        if k == word_len:
            return True
        
    return False

def word_count(input):
    word = "XMAS"
    grid = parse(input)
    m = len(grid)
    n = len(grid[0])
    ans = []

    for i in range(m):
        for j in range(n):
            if search_grid(grid, i, j, word):
                ans.append((i, j))

    return ans

def solve_part_one(input):
    result = None
    return result


def solve_part_two(input):      
    
    result = None
    return result