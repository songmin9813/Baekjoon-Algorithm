H,M = map(int,input().split())
H,M = (H,M-45) if M-45>=0 else (23,15+M) if H==0 else (H-1,15+M)
print(H, M)