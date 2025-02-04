import random

def random_array(arr):
    for i in range(len(arr)):
        arr[i] = random.randint(1, 20)
    return arr
