sudoku = [
    [0,3,0, 0,0,0, 0,0,0],
    [0,0,0, 0,0,0, 0,1,8],
    [1,0,6, 0,0,0, 7,0,0],

    [0,7,0, 0,0,4, 9,0,0],
    [0,2,0, 6,0,0, 0,0,5],
    [0,0,1, 2,8,0, 0,0,0],

    [9,0,0, 0,0,0, 0,0,0],
    [0,0,7, 0,1,8, 6,4,0],
    [0,0,0, 0,9,5, 0,0,0],
] 

def check_sudoku(y,x,n):
    global sudoku
    if sudoku[y].count(n) == 1: return False

    for a in range(9):
        if sudoku[a][x] == n: return False

    y0,x0 = (y//3)*3, (x//3)*3
    for a in range(3):
        for b in range(3):
            if sudoku[y0+a][x0+b] == n: return False
   
    return True

def solve_sudoku():
    global sudoku
    for y in range(9):
        for x in range(9):
            # Find blank positions in the sudoku (value = 0)
            if sudoku[y][x] == 0:
                # Loop n from 1-9
                for n in range(1,10):
                    if check_sudoku(y,x,n):
                        sudoku[y][x] = n
                        new = solve_sudoku()

                        # This is where backtracking happens
                        # Reset the latest position back to 0 and try with new n value
                        if new == False:
                            sudoku[y][x] = 0
                        else:
                            return True
                return False
    return True
solve_sudoku()

for a in range(9):
    print(sudoku[a])