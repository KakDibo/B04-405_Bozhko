def f(x):   
    for i in range(2, x):
        if x%i == 0:
            print(i, end=' ')
            return f(x//i)
    print(x) 
n = int(input())
f(n)


    
        
    