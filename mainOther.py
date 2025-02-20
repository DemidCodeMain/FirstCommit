#for i in range(int(input())):
#    a,b,c = [int(i) for i in input().split()]
####        print("YES")
#    elif c == a + b:
#        print("YES")
#    else:
#       print("NO")
for i in range(int(input())):
    a,b,c = [int(i) for i in input().split()]
    if c == b + a:
        print('+')
    else:
        print('-')