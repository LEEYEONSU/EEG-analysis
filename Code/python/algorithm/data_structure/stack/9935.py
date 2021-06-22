import sys 

T = input().strip()
B = input().strip()

stack = []
last_B  = B[-1]

for t in T:
    stack.append(t)
    if t == last_B and "".join(stack[-len(B):]) == B:
        del stack[-len(B):]
    
if len(stack) == 0:
    print("FRULA")
else :
    print("".join(stack))



