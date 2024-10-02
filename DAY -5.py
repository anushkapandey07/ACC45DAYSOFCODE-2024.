T = int(input())

for _ in range(T):
    # Read B1, B2, and B3
    B1, B2, B3 = map(int, input().split())
    
    empty_count = 3 - (B1 + B2 + B3)  
    
    if empty_count >= 2:
        print("Water filling time")
    else:
        print("Not now")