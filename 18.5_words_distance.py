test = "the quick dog jumped over the lazy brown dog"

words = test.split(' ')

min_counter = float("inf")
counter = 0

word1 = "over"
word2 = "the"

which_word = 0

for word in words:
    if word == word1:
        if which_word == 1:
            counter = 0
        elif which_word == 2:
            counter += 1
            if counter < min_counter:
                min_counter = counter
                counter = 0
        which_word = 1
    elif word == word2:
        if which_word == 2:
            counter = 0
        elif which_word == 1:
            counter += 1
            if counter < min_counter:
                min_counter = counter
                counter = 0
        which_word = 2
    elif which_word != 0:
        counter += 1

print(min_counter)



# distances = {}
#
# n = len(words_list)
# for i in range(1, n): # spaces between words
#     for j in range(n): # words
#         curr = words_list[j]
#         if j+i<n:
#             next = words_list[j+i]
#             if next != curr:
#                 if (curr, next) not in distances:
#                     distances[(curr, next)] = distances[(next, curr)] = i
#
# pair = ('a', 'b')
# if pair in distances:
#     print(distances[pair])