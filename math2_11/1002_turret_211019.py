import sys

t=int(sys.stdin.readline())

for i in range(t):
    x_1,y_1,r_1,x_2,y_2,r_2=map(int,sys.stdin.readline().split())
    d=(x_2-x_1)**2+(y_2-y_1)**2    

    if x_1==x_2 and y_1==y_2 and r_1==r_2: #동심원
        print('-1')
    elif (r_1+r_2)**2 == d or (r_2-r_1)**2==d: #외접, 내접
        print('1')
    elif (r_2-r_1)**2<d<(r_1+r_2)**2: #|r2-r1| < d < r2+r1
        print('2')
    else: #외부, 내부
        print('0')