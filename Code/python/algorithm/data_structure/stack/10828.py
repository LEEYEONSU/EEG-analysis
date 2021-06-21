import sys 

n = int(sys.stdin.readline().rstrip())
stack = []

for _ in range(n):
    tmp = sys.stdin.readline().rstrip().split()

    ord = tmp[0]

    if ord == 'push':
        stack.append(tmp[1])
    
    elif ord == 'top':
        print(stack[-1]) if stack else print(-1)
    
    elif ord == 'size':
        print(len(stack))
    
    elif ord == 'empty':
        print(0) if stack else print(1)
    
    elif ord == 'pop':
        if not stack:
            print(-1)
        else :
            print(stack.pop())


