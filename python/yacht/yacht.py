# Score categories.
YACHT = 0
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 7
FOUR_OF_A_KIND = 8
LITTLE_STRAIGHT = 9
BIG_STRAIGHT = 10
CHOICE = 11

from collections import Counter


def score(dice, category):
    c = Counter(dice)
    mc = c.most_common()
    if 1 <= category <= 6:
        return c[category] * category
    elif category == 7:
        if len(c) == 2 and mc[0][1] == 3:
            return mc[0][0] * mc[0][1] + mc[1][0] * mc[1][1]
    elif category == 8:
        if len(c) <= 2 and mc[0][1] >= 4:
            return mc[0][0] * 4
    elif category == 9:
        if len(c) == 5 and (c[1] ^ c[6]) and c[1]:
            return 30
    elif category == 10:
        if len(c) == 5 and (c[1] ^ c[6]) and c[6]:
            return 30
    elif category == 11:
        return sum(dice)
    else:  # category 0
        if len(c) == 1:
            return 50
    return 0
