a, b= map(int, input().split())
for i in range(-max(a,b), -1):
    if a%(-i)==0 and b%(-i)==0:
        d = -i
def CHTO(a, b, d):
    if fl==True:
        fl = False
    else:
        fl = True
    if flag == True:
        x,y =1,-1
        flag = FaLse
    if a*x+b*y ==d:
        print(x, y, d, sep=' ')
        return 1
    if a*x+b*y ==-d:
        print(-x, -y, d, sep=' ')
        return 1
    if fl==True:
        y+=1        
    return CHTO(y, x, d)
CHTO(a, b, d)
    

    