import sys

while True :
    line = sys.stdin.readline().rstrip('\n') 
    up, low, space, num = 0, 0, 0, 0

    if not line :
        break
    for l in line:
        if l.isupper():
            up += 1
        elif l.islower():
            low += 1
        elif l.isdigit():
            num += 1
        elif l.isspace():
            space  += 1
    
    sys.stdout.write('{} {} {} {} \n'.format(low, up, num, space))
