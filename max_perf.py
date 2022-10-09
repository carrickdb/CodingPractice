def maxPerformance(n, speed, efficiency, k):
	speed_sorted = list(enumerate(speed))
	print(speed_sorted)
	speed_sorted = sorted(speed_sorted, key=lambda x: x[1], reverse=True)
	efficiency_sorted = list(enumerate(efficiency))
	efficiency_sorted = sorted(efficiency_sorted, key=lambda x: x[1])
	max_sum = 0
	for _, top_speed in speed_sorted[:k]:
		max_sum += top_speed
	max_perf = 0
	top_kek = set([x[0] for x in speed_sorted[:k]])
	next_lowest = k-1
	for engineer, curr_efficiency in efficiency_sorted[:n-k+1]:
		curr_sum = max_sum
		in_top = engineer in top_kek
		if not in_top:
			curr_sum += speed[engineer]
			curr_sum -= speed_sorted[k-1][1]
			top_kek.remove(engineer)
		max_perf = max(max_perf, curr_sum * curr_efficiency)
		if next_lowest < n:
			top_kek.add(speed_sorted[next_lowest][0])
			if in_top:
				max_sum -= speed[engineer]
				max_sum += speed_sorted[next_lowest][1]
				next_lowest += 1
	return max_perf % (10**9 + 7)

"""
speed_sorted = [(0, 5)]
efficiency_sorted = [(0, 1)]
max_sum = 5
top_kek = (0)
engineer = 0
curr_efficiency = 1
curr_sum = 5
max_perf = 0
"""


n = 1
speed = [5]
efficiency = [1]
k = 1
print(maxPerformance(n, speed, efficiency, k))


"""
create tuples of speeds and indexes and sort the speeds
do the same thing with the efficiency array
get sum of the top k's speeds
for each engineer, in ascending order of efficiency:
	if this engineer isn't in the top k:
		subtract the lowest in k from the sum
		add the current engineer's speed
	multiply the sum by current engineer's efficiency
	delete this engineer from the speed array
O(nlogn)
"""
