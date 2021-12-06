class player:
    def __init__(self,name):
        self.player_name = name
        self.cards = list()
        return

    def add_card(self,card_list):
        for c in card_list:
            self.cards.append(c)
        return
    
    def get_top_card(self):
        return self.cards.pop(0)

##############
def check_winner():
    if len(players['1'].cards) == 0:
        return '2'
    elif len(players['2'].cards) == 0:
        return '1'
    return False


def play_round(round ):
    if print_out:
        print("\n-- Round {} --".format(round))
        print("Player 1's deck: {}".format(','.join([str(int) for int in players['1'].cards])))
        print("Player 2's deck: {}".format(','.join([str(int) for int in players['2'].cards])))
    c1 = players['1'].get_top_card()
    c2 = players['2'].get_top_card()
    if print_out:
        print("Player 1 plays: {}".format(c1))
        print("Player 2 plays: {}".format(c2))

    if c1 > c2:
       if print_out: print("Player 1 wins the round!")
       players['1'].add_card([c1, c2])
    elif c2 > c1:
        if print_out: print("Player 2 wins the round!")
        players['2'].add_card([c2, c1])
    else:
        pass
    return

def score(winner):
    total = 0
    for i, c in zip(reversed(range(1,total_cards+1)),players[winner].cards):
        total += i * c
    return total

def print_winner(winner):
    print("\n== Post-game results ==")
    print("Player 1's deck: {}".format(','.join([str(int) for int in players['1'].cards])))
    print("Player 2's deck: {}".format(','.join([str(int) for int in players['2'].cards])))
    print("Score = {}".format(str(score(winner))))
    return

def play_combat():
    round = 0
    winner = False
    while not winner:
        round += 1
        play_round(round)
        winner = check_winner()
    print_winner(winner)
    return

##############
players = dict()
for line in open("input.txt"):
    line = line.strip()
    if not line:
        continue
    elif ':' in line:
        name = line.split(':')[0].split()[1]
        players[name] = player(name)
    else:
        players[name].add_card([int(line)])

print_out = False
total_cards = 0
for k, v in players.items():
    total_cards += len(v.cards)
play_combat()
