import time

def func_one(n):
    return [str(num) for num in range(n)]

print(func_one(10))

print()

def func_two(n):
    return list(map(str, range(10)))

print(func_two(10))

print()

# STEP 1: Get start time
start_time = time.time()

# Step 2: Run your code you want to time
func_one(1000000)

# Step 3: Calculate total time elapsed
elapsed_time = time.time() - start_time
print(elapsed_time)

print()

# STEP 1: Get start time
start_time = time.time()

# Step 2: Run your code you want to time
func_two(1000000)

# Step 3: Calculate total time elapsed
elapsed_time = time.time() - start_time
print(elapsed_time)

print()

# STEP 1: Get start time
start_time = time.time()

# Step 2: Run your code you want to time
time.sleep(0.67)

# Step 3: Calculate total time elapsed
elapsed_time = time.time() - start_time
print(elapsed_time)

print()

import timeit



