T = int(input())

for _ in range(T):
    # Read X and Y
    X, Y = map(int, input().split())
    
    total_hours = 4 * X + Y
    
    print(total_hours)
