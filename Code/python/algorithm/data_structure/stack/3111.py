import sys

A = sys.stdin.readline().rstrip()
T = sys.stdin.readline().rstrip()

A = list(A)
reversed_A = list(reversed(A))
len_A = len(A)

L = []
R = []

L_idx = 0
R_idx = len(T) - 1

flag = True

while L_idx <= R_idx:    

    if flag:
        L.append(T[L_idx])
        L_idx += 1

        if L[-len_A:] == A :
            L[-len_A:] = []
            flag = False 
    
    else :
        R.append(T[R_idx])
        R_idx -= 1

        if R[-len_A:] == reversed_A:
            R[-len_A:] = []
            flag = True 

while R:
    L.append(R.pop())

    if L[-len_A:] == A:
        L[-len_A:] = []

print("".join(L)) 


