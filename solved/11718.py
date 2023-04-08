import sys
while True:
    try:
        n=sys.stdin.readline().rstrip()
        if n=="":
            break
        print(n)
    except:
        break