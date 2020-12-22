import copy
import matplotlib.pyplot as plt

class player:
    def __init__(self,name):
        self.player_name = name
        self.cards = list()
        self.decks = list()
        return

    def add_game(self,prev,game,num):
        self.cards.append(list())
        self.decks.append(list())
        if game > 0:
            self.cards[game] = copy.deepcopy(self.cards[prev][:num])
        return
    
    def add_card(self,card_list,game):
        for c in card_list:
            self.cards[game].append(c)
        return

    def check_infinite_loop(self,game):
        if self.cards[game] in self.decks[game]:
            return self.decks[game].index(self.cards[game])
        else:
            return self.player_name
        
    def add_round(self,game):
        self.decks[game].append(copy.deepcopy(self.cards[game]))
        return
    
    def get_top_card(self,game):
        return self.cards[game].pop(0)

##############
def check_winner(game):
    if len(players['1'].cards[game]) == 0:
        return '2'
    elif len(players['2'].cards[game]) == 0:
        return '1'
    return False

def score(winner,game):
    total = 0
    for i, c in zip(reversed(range(1,len(players[winner].cards[game])+1)),players[winner].cards[game]):
        total += i * c
    return str(total)

def print_winner(winner,game):
    print("\n== Post-game results ==")
    print("Player 1's deck: {}".format(','.join([str(int) for int in players['1'].cards[game]])))
    print("Player 2's deck: {}".format(','.join([str(int) for int in players['2'].cards[game]])))
    if winner: print("Player {}'s Score = {}".format(winner,score(winner,game)))
    return


def recursive_combat(rnd,prev,c1,c2):
    if print_out: print("Playing a sub-game to determine the winner...")

    game = len(rnd)
    if print_out: print("\n=== Game {} ===".format(game+1))
    rnd.append(0)
    players['1'].add_game(prev,game,c1)
    players['2'].add_game(prev,game,c2)

    winner = play_combat(rnd, game)
    
    if print_out: print("...anyway, back to Game {}".format(prev+1))
    return winner

def play_round(rnd, game):
    if print_out:
        print("\n-- Round {} Game {} --".format(rnd[game],game+1))
        print("Player 1's deck: {}".format(','.join([str(int) for int in players['1'].cards[game]])))
        print("Player 2's deck: {}".format(','.join([str(int) for int in players['2'].cards[game]])))

    c1 = players['1'].get_top_card(game)
    c2 = players['2'].get_top_card(game)
    if print_out:
        print("Player 1 plays: {}".format(c1))
        print("Player 2 plays: {}".format(c2))

    if len(players['1'].cards[game]) >= c1 and len(players['2'].cards[game]) >= c2:
        winner = recursive_combat(rnd, game,c1, c2)
    else:
        if c1 > c2:
            winner = '1'
        elif c2 > c1:
            winner = '2'
        # no instructions for if they tie
    if winner == '1':
        if print_out: print("Player 1 wins the round!")
        players['1'].add_card([c1, c2],game)
    elif winner == '2':
        if print_out: print("Player 2 wins the round!")
        players['2'].add_card([c2, c1],game)
        
    return 

def play_combat(rnd,game):
    rnd[game] = 0
    winner = False
    while not winner:
        rnd[game] += 1
        if  players['1'].check_infinite_loop(game) == players['2'].check_infinite_loop(game):
            winner = '1'
            if print_out: print("**** Inifinite loop detected ****")
            if print_out: print("Player 1 wins the round!")
        else:
            players['1'].add_round(game)
            players['2'].add_round(game)
            play_round(rnd,game)
            winner = check_winner(game)

    if game == 0:
        print_winner(winner, game)
    return winner, rnd

#######################
players = dict()
for line in open("input.txt"):
    line = line.strip()
    if not line:
        continue
    elif ':' in line:
        name = line.split(':')[0].split()[1]
        players[name] = player(name)
        players[name].add_game(0,0,0)

    else:
        players[name].add_card([int(line)],0)

print_out = False
winner, rnd = play_combat([0],0)
with plt.xkcd():
    plt.bar(range(1,len(rnd)+1),rnd, align='center', alpha=0.5)
    plt.xticks(range(1,len(rnd)+1),range(1,len(rnd)+1))
    plt.ylabel('Rounds')
    plt.xlabel('Game')
    plt.title('Day 22')
    plt.tight_layout()
    plt.show()
#35154
