def digit_root(x):
    iterations = 100  # Максимальное количество итераций
    while x > 9 and iterations > 0:
        x = sum(int(digit) for digit in str(x))
        iterations -= 1
    return x

def sort_by_digit_root(x):
    sorted_list = sorted(x, key=lambda y: digit_root(y))
    print(*sorted_list)

numbers = list(map(int, input().split()))
sort_by_digit_root(numbers)
