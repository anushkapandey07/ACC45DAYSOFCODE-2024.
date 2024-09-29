def chef_tv_subscriptions(T, test_cases):
    results = []
    
    for i in range(T):
        N, X = test_cases[i]
        subscriptions_needed = (N + 5) // 6
        total_cost = subscriptions_needed * X
        results.append(total_cost)
    
    return results

T = int(input())  # Number of test cases
test_cases = [tuple(map(int, input().split())) for _ in range(T)]

results = chef_tv_subscriptions(T, test_cases)

for result in results:
    print(result)