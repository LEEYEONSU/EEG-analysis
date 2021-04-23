from itertools import permutations

n = int(input())
inning = [list(map(int, input().split())) for _ in range(n)]

def game(line_ups):
    hit_idx = 0
    score = 0
    for each_inning in inning :
        outcount = 0
        base1, base2, base3 = 0, 0, 0

        while outcount < 3 :
            if each_inning[line_ups[hit_idx]] == 0:
                outcount += 1
            elif each_inning[line_ups[hit_idx]] == 1:
                score += base3
                base1, base2, base3 = 1, base1, base2
            elif each_inning[line_ups[hit_idx]] == 2:
                score += (base2 + base3)
                base1, base2, base3 = 0, 1, base1
            elif each_inning[line_ups[hit_idx]] == 3 :
                score += (base1 + base2 + base3)
                base1, base2, base3 = 0, 0, 1
            elif each_inning[line_ups[hit_idx]] == 4 :
                score += (base1 + base2 + base3 + 1)
                base1, base2, base3 = 0, 0, 0

            hit_idx = (hit_idx + 1)%9

    return score


max_score = 0
for line_ups in permutations(range(1,9), 8):
    line_ups = list(line_ups[:3]) + [0] + list(line_ups[3:])
    max_score = max(max_score, game(line_ups))

print(max_score)
