
stack_1 = list(input())
stack_2 = []
n = int(input())

for _ in range(n):
    tmp = list(input())
    
    if tmp[0] == 'L' :
        if not stack_1: continue
        else : stack_2.append(stack_1.pop())

    elif tmp[0] == 'D' :
        if not stack_2: continue
        else : stack_1.append(stack_2.pop())
    
    elif tmp[0] == 'B':
        if stack_1: stack_1.pop()
        else : continue

    elif tmp[0] == 'P':
        stack_1.append(tmp[2])
print("".join(stack_1+stack_2[-1::-1]))