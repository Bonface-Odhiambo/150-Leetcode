numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def custom_filter(n):
    if n % 3 == 0:
        return False
    if n % 2 == 0:
        return n % 5 != 0
    return n >5

filtered_numbers = filter( lambda x: custom_filter(x), numbers)
result = list(filtered_numbers)
print(result)