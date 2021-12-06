class bingo_board:
    def __init__(self,i,board):
        self.board_number = i
        self.board = board
        self.marks = [[False for i in range(len(self.board[0]))] for j in range(len(board))]
        self.has_bingo = False
        self.solution = 0
        self.last_call = ''
        
    def print(self, b):
        if b == "board":
            for n in self.board:
                print(' '.join(n))
        elif b == "marks":
            for n in self.marks:
                print(n)

    def mark_call(self, call):
        for row, items in enumerate(self.board):
            if call in items:
                #print("Call {} found on {} at {},{}".format(call,self.board_number,row,self.board[row].index(call)))
                self.marks[row][self.board[row].index(call)] = True
                self.last_call = call
                self._check_bingo()
                return
                
    def _transpose_board(self):
        trans = [[False for i in range(len(self.marks[0]))] for j in range(len(self.marks))]
        for row, items in enumerate(self.marks):
            for col, val in enumerate(items):
                trans[col][row] = val
        return trans

    def _check_bingo(self):
        for row in self.marks:
            if all(row):
                self.has_bingo = True
                break
            
        if not self.has_bingo:   
            for col in self._transpose_board():
                if all(col):
                    self.has_bingo = True
                    break
                
        if self.has_bingo:
            self._calc_solution()
        return

    def _calc_solution(self):
        sum_unmarked = 0
        for br, mr in zip(self.board, self.marks):
            for bc, mc in zip(br,mr):
                if not mc:
                    sum_unmarked += int(bc)
        self.solution = sum_unmarked * int(self.last_call)
        return self.solution
    
###############################################3
    
def parse_input(file):
    boards = list()
    with open(file) as f:
        calls = f.readline().strip().split(',')
        while True:
            spacer = f.readline()
            if not spacer:
                break
            else:
                board = [f.readline().strip().split() for i in range(5)]
                boards.append(bingo_board(len(boards)+1,board))
    return calls, boards

def play_bingo(calls,boards, to_lose):
    boards_remaining = len(boards)
    
    for c in calls:
        for b in boards:
            if not b.has_bingo:
                b.mark_call(c)
                if b.has_bingo:
                    if to_lose:
                        last_bingo = b.board_number
                        last_solution = b.solution
                        boards_remaining -= 1
                        if not boards_remaining:
                            break
                    else:
                        print("Found bingo in board " + str(b.board_number))
                        print("    Solution is",b.solution)
                        return b.solution                        
    print("Last solution is board",last_bingo)
    print("    with solution",last_solution)
    return last_solution


print("-- Part 1")
assert play_bingo(*parse_input("sample.txt"), False) == 4512
assert play_bingo(*parse_input("input.txt"), False) == 16716
print("\n-- Part 2")
assert play_bingo(*parse_input("sample.txt"), True) == 1924
assert play_bingo(*parse_input("input.txt"), True) == 4880
