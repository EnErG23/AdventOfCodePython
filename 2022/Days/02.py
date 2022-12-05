path = '../Inputs/2.txt'

Input = [l.strip() for l in open(path)]

score1 = 0
score2 = 0

for i in Input:
    o, m = i.replace("A", "1").replace("B", "2").replace("C", "3").replace("X", "1").replace("Y", "2").replace("Z", "3").split()

    op = int(o)
    me = int(m)

    score1 += me + {(1, 1): 3, (1, 2): 6, (1, 3): 0,
                    (2, 1): 0, (2, 2): 3, (2, 3): 6,
                    (3, 1): 6, (3, 2): 0, (3, 3): 3}[(op, me)]

    score2 += {1: 0, 2: 3, 3: 6}[me] + {(1, 1): 3, (1, 2): 1, (1, 3): 2,
                                        (2, 1): 1, (2, 2): 2, (2, 3): 3,
                                        (3, 1): 2, (3, 2): 3, (3, 3): 1}[(op, me)]

print(score1)
print(score2)