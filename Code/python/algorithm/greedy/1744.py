
n = int(input())
positive, negative = [], []
zero = False

for _ in range(n):
    tmp = int(input())
    if tmp > 0 : 
        positive.append(tmp)
    elif tmp == 0 : 
        zero = True
    else : 
        negative.append(tmp)

positive = sorted(positive, reverse = True)
negative = sorted(negative)

ans = 0 
while len(positive) > 0 or len(negative) > 0  : 
    if len(positive) > 1 : 
        for _ in range(len(positive) // 2):
            if positive[0] == 1 or positive[1] == 1:
                ans += (positive[0] + positive[1])
            else:
                ans += positive[0]*positive[1]
            del positive[0:2] 
    if len(positive) > 0 :
        ans += positive[0]
        del positive[0]
    
    if len(negative) > 1: 
        for _ in range(len(negative) // 2):
            ans += negative[0] * negative[1]
            del negative[0:2]
    if len(negative) > 0  : 
        if zero > 0 :
            zero = False
            del negative[0]
        else : 
            ans += negative[0]
            del negative[0]
print(ans)
        
    

    



    