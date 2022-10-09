import heapq


def getOrder(tasks):
    i = 0
    for task in tasks:
        task.append(i)
        i += 1
    tasks = sorted(tasks, key=lambda x: tasks[0])
    answer = []
    time = 0
    available_tasks = []
    for task in tasks:
        if task[1] >= time:
            heapq.heappush(available_tasks, task)
            time = task[1]
        else:
            curr_task = 




tasks = [[7,10],[7,12],[7,5],[7,4],[7,2]]
print(getOrder(tasks))



# def maxIceCream(costs, coins):
#     costs = sorted(costs)
#     numBars = 0
#     for cost in costs:
#         if coins >= cost:
#             coins -= cost
#             numBars += 1
#         else:
#             break
#     return numBars
#
# costs = [1,6,3,1,2,5]
# coins = 20
# print(maxIceCream(costs, coins))


# def checkIfPangram(str):
#     buckets = [0 for i in range(26)]
#     for char in str:
#         buckets[ord(char) - ord('a')] = 1
#     for bucket in buckets:
#         if bucket == 0:
#             return False
#     return True
#
#
# str = "thequickbrownfoxjumpsoverthelazydog"
# str = 'leetcode'
# print(checkIfPangram(str))
