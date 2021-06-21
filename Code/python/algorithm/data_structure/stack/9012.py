import sys 

def check(tmp):
    stack = []
    for i in range(len(tmp)):
        if tmp[i] == '(':
            stack.append(tmp[i])
        else :
            if stack: stack.pop()
            else : return 'NO' 
    
    if not stack :
        return 'YES'
    else :
        return 'NO'
            
n = int(input())
for _ in range(n):
    tmp = list(input())
    print(check(list(tmp)))
