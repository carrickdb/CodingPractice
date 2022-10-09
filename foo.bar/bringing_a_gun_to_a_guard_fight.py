from math import sqrt
from fractions import Fraction

def answer(dimensions, captain_position, badguy_position, distance):
    # corner cases:
    #   actual corners
    #   you getting shot
    #   if already shot the guy, bullet can't go through him again
    bearings = {}
    X = dimensions[0]
    Y = dimensions[1]
    you_x = captain_position[0]
    you_y = captain_position[1]
    guard_x = badguy_position[0]
    guard_y = badguy_position[1]

    # add corner points
    quotient = (distance - you_x)/X
    start_x = -quotient * X         # test where start_x is negative
    quotient = (distance + you_y)/Y
    start_y = quotient*Y
    span = -start_x + you_x + distance
    height = start_y + distance - you_y
    num_x = span / X + 1
    num_y = height/Y + 1
    for i in xrange(num_y):
        curr_y = start_y - i*Y
        for j in xrange(num_x):
            curr_x = start_x + j*X
            dist = sqrt((you_x - curr_x)**2 + (you_y - curr_y)**2)
            if dist > distance:
                continue
            print curr_x, curr_y
            frac = Fraction(curr_x - you_x, curr_y - you_y)
            print frac
            bearing = (abs(frac.numerator) if (curr_x-you_x) > 0 else -abs(frac.numerator),
                       abs(frac.denominator) if (curr_y-you_y) > 0 else -abs(frac.denominator))
            if bearing not in bearings:
                bearings[bearing] = (dist, 0)

    # add your and guard's points


    # check for parallel vectors
    for bearing in bearings:
        if len(bearing) > 1:
            num_guards = 0
            min_dist = float("inf")
            who_min_dist = None
            for point in bearing:
                if point[1] == 1:
                    num_guards += 1
                if point[0] < min_dist:
                    min_dist = point[0]
                    who_min_dist = point[1]
                
    total = 0


    return total

print answer([3, 2], [1, 1], [2, 1], 4)