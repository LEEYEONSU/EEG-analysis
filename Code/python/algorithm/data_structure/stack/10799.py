
bar = list(input())

stack = []
ans = 0 
for i in range(len(bar)):
    if bar[i] == '(':
        stack.append(bar[i])
    else :
        if bar[i-1] == '(':
            stack.pop()
            ans += len(stack)
        else : 
            stack.pop()
            ans += 1
print(ans)
