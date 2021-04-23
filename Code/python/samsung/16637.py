
def cal_num(pre, post, opt):
    if opt == '+':
        return pre + post
    elif opt == '*':
        return pre * post
    else : 
        return pre - post 

def cal_queue(queue):
    result = queue[0]
    for i in range(0, len(queue)-2, 2):
        post = queue[i+2]
        result = cal_num(result, post, queue[i+1])
    return result

def insert_bracket(i, q):
    if i == n - 1: 
        no_bracket = q + [f[i]]
        return cal_queue(no_bracket)
    if i == n - 3:
        no_bracket = q + [f[i], f[i+1]]
        tmp = cal_num(f[i], f[i+2], f[i+1])
        bracket = q + [tmp]
        return max(insert_bracket(i+2, no_bracket), cal_queue(bracket))

    no_bracket = q + [f[i], f[i+1]]
    tmp = cal_num(f[i], f[i+2], f[i+1])
    bracket = q + [tmp, f[i + 3]]
    
    return max(insert_bracket(i+2, no_bracket),insert_bracket(i+4, bracket))

n = int(input())
f = [ int(x) if x != '*' and x != '+' and x != '-' else x for x in list(input()) ]
result = insert_bracket(0, [])
print(result)
