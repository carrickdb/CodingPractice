import random


x = 10**6
# start = -(2**31) + 1
# end = (2**31) - 1

# with open("ints.txt", "w+") as f:
#     for i in range(x):
#         rand_gen = random.randint(start, end)
#         f.write(str(rand_gen)+'\n')

mem_size = 1
mem_size <<= 20

num_counters = mem_size//4   # 2^18

int_size = 1
int_size <<= 32

block_size = int_size//num_counters   # 2^14

counters = [0 for y in range(num_counters)]

# 1 2 4 8 16 32 --> 2^6 bits
# 2^8 bit vector


with open("ints.txt", "r") as f:
    done = False
    for i in range(x):
        curr = f.readline().strip()
        if curr == '':
            continue
        curr = int(curr)
        curr += (2**31) - 1
        counters[curr//block_size] += 1
    for i in range(x):
        if counters[i] != block_size:
            arr_size = block_size//32
            bit_vector = [0 for y in range(arr_size)]
            start = i*block_size
            end = (i+1)*block_size
            for j in range(x):
                curr = f.readline().strip()
                if curr == '':
                    continue
                curr = int(curr)
                curr += (2 ** 31) - 1
                if curr < end and curr >= start:
                    mask = 1
                    mask <<= curr % block_size
                    bit_vector[curr//block_size] |= mask
            for j in range(arr_size):
                if bit_vector[j] < 0xFFFFFFFF:
                    position = 0
                    mask = 1
                    for k in range(32):
                        if bit_vector[j] & mask == 0:
                            result = j * block_size + position
                            result -= (2**31)+1
                            print(result)
                            done = True
                            break
                        mask <<= 1
                        position += 1
                if done:
                    break
        if done:
            break
