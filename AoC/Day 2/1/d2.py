def game_calc(game):
    score = 0
    # if opp is A(rock)
    if (game[0] == 'A' and game[2] == 'Y'):#paper
        return 'W-8'
    if (game[0] == 'A' and game[2] == 'X'):#rock
        return 'D-4'
    if (game[0] == 'A' and game[2] == 'Z'):#scissors
        return 'L-3'
    # if opp is B(paper)
    if (game[0] == 'B' and game[2] == 'Y'):
        return 'D-5'
    if (game[0] == 'B' and game[2] == 'X'):
        return 'L-1'
    if (game[0] == 'B' and game[2] == 'Z'):
        return 'W-9'
        # if opp is C(scissors)
    if (game[0] == 'C' and game[2] == 'Y'):
        return 'L-2'
    if (game[0] == 'C' and game[2] == 'X'):
        return 'W-7'
    if (game[0] == 'C' and game[2] == 'Z'):
        return 'D-6'

def score_calc(array):
    tot_score = 0
    for game in array:
        tot_score += int(game[2])
    return tot_score

print(game_calc('B Y'))

with open('Day 2\/1\input.txt') as f:
    lines = f.readlines()
f.close

print(lines)

results = []
for game in lines:
    results.append(game_calc(game))
print(results)
print(score_calc(results))