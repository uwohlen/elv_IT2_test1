import random, time

def lsd_radix_sort(numbers):
    digits = 0
    for number in numbers:
        digits = max(digits, len(str(number)))
    
    for digit in range(digits):
        buckets = [[] for i in range(10)]
        for number in numbers:
            i = len(str(number)) - digit - 1
            power = 10**digit
            if i < 0:
                buckets[0].append(number)
                continue
            buckets[number // 10**digit % 10].append(number)

        i = 0
        for bucket in buckets:
            for number in bucket:
                numbers[i] = number
                i += 1
    
    return numbers

def msd_radix_sort(numbers):
    digits = 0
    for number in numbers:
        digits = max(digits, len(str(number)))
    
    return sort(numbers, digits)

def sort(numbers, digit):
    if len(numbers) == 0:
        return []
    if digit < 0:
        return numbers
    power = 10**digit
    buckets = [[] for i in range(10)]
    for number in numbers:
        buckets[(number // power) % 10].append(number)
    i = 0
    for bucket in buckets:
        start = i
        for number in bucket:
            numbers[i] = number
            i += 1
        sorted = sort(numbers[start:i], digit-1)
        i = start
        for number in sorted:
            numbers[i] = number
            i += 1
    return numbers

def benchmark(algo, num, max):
    numbers = [random.randint(0, max) for i in range(num)]
    start = time.perf_counter()
    algo(numbers)
    return time.perf_counter() - start

print(f"lsd_radix_sort: {benchmark(lsd_radix_sort, 1_000_000, 1_000_000)}s")
print(f"msd_radix_sort: {benchmark(msd_radix_sort, 1_000_000, 1_000_000)}s")
#print(lsd_radix_sort([170, 45, 75, 90, 2, 802, 2, 66]))