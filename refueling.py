"""
naive: power set (every combination)

hunch: greedy algorithm (just refuel when needed)
doesn't work:

startFuel: 3

1    2      3     4    5     6
2    10     1     2    99    x

solution: 1 stop (at 2)

you only ever need target liters

recursive solution:

minStops(target, startFuel, stations):
    if startFuel >= distance to target:
        return 0
    if startFuel + fuel at station >= distance to target:
        return 1
    if startFuel + fuel at station < distance to next station (or target if at last station):
        return -1

    currentFuel = startFuel - distance from prev station to this station
    // we do stop at this station
    a = 1 + minStops(distance to target, currentFuel + fuel at this station, stations[1:])

    // we don't stop at this station
    b = minStops(distance to target, currentFuel, stations[1:]))

    if a != -1 && b != -1:
        return min(a, b)
    if a != -1:
        return a
    return b;
"""

def minStopsRecursive(target, startFuel, stations):
    if not stations:
        if startFuel < target:
            return -1
        return 0
    """
    (100, 0, [[10,60],[20,30],[30,30],[60,40]])
    remainingDistance = 90
    nextFuel
    """
    remainingDistance = target - stations[0][0]
    if startFuel >= remainingDistance:
        return 0
    if startFuel + stations[0][1] >= remainingDistance:
        return 1
    if len(stations) < 2 or startFuel + stations[0][1] < stations[1][0] - stations[0][0]:
        return -1
    nextFuel = startFuel - (stations[1][0] - stations[0][0])
    if nextFuel >= 0:
        noStop = minStopsRecursive(target, nextFuel, stations[1:])
    else:
        noStop = -1
    stop = 1 + minStopsRecursive(target, nextFuel + stations[0][1], stations[1:])
    # 50, [20, 30]...
    print(stop, noStop)
    if stop != -1 and noStop != -1:
        return min(stop, noStop)
    if stop == -1:
        return noStop
    return stop

def minRefuelStops(target, startFuel, stations):
    if stations and startFuel < stations[0][0]:
        return -1
    return minStopsRecursive(target, startFuel - stations[0][0], stations)

print(minRefuelStops(100, 50, [[25,25],[50,50]]))




"""
Memo:
M[fuel, i] = min(1 + M[fuel + fuel at station, i-1], M[fuel, i-1])


array A, stations.length (+2?) long (including start and target?)
each slot is the number of stops you've made

A[0] = -1
A[i] =
"""
