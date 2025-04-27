n = int(input())
x, y = 0, 1
def fib(a):
    if a<=2:
        return 1
    else:
        return fib(a-1)+fib(a-2)
print(fib(n))