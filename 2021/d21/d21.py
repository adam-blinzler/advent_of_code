class player:
    def __init__(self,name,start):
        self.name = name
        self.pos = start
        self.points = 0

    def add_points(self):
        self.points += self.pos
        if self.points >= 1000:
            return True
        else:
            return False

    def move_pos(self,num):
        self.pos = (self.pos + num - 1) % 10 + 1
        return
    
def get_start(start_file):
    players = list()
    with open(start_file) as f:
        players.append(player("Player 1",int(f.readline().strip().split(": ")[1])))
        players.append(player("Player 2",int(f.readline().strip().split(": ")[1])))

    return players


def play_game(players):
    dice = 0
    total_rolls = 0
    while True:
        for p in [0,1]:
            for _ in range(3):
                dice = dice + 1
                if dice > 100:
                    dice = dice % 100
                total_rolls += 1
                players[p].move_pos(dice)
                
            if players[p].add_points():
                if p == 0:
                    score = players[1].points * total_rolls
                    print("Losing player is",players[1].name)
                else:
                    score = players[0].points * total_rolls
                    print("Losing player is",players[0].name)
                print("    points * total rolls = ", score)
                return score

print("-- Part 1")
assert play_game(get_start("sample.txt")) == 739785
assert play_game(get_start("input.txt")) == 798147
