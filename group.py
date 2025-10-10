"""
Problem: Chef-TV Subscriptions

A new TV streaming service called Chef-TV has started in Chefland. 
A group of N friends wants to buy Chef-TV subscriptions. 

Rules:
- 6 people can share one Chef-TV subscription.
- The cost of one subscription is X rupees.

Task:
Determine the minimum total cost that the group of N friends will incur 
so that everyone can use Chef-TV.

Input Format:
- The first line contains a single integer T — the number of test cases.
- Each test case contains two integers N and X:
  - N: number of friends in the group
  - X: cost of one subscription

Output Format:
- For each test case, output the minimum total cost for the group.

Constraints:
- 1 ≤ T ≤ 1000
- 1 ≤ N ≤ 100
- 1 ≤ X ≤ 1000

Sample Input:
3
6 100
10 120
5 50

Sample Output:
100
240
50

Explanation:
1. For 6 friends with cost 100:
   - 6 friends fit exactly in 1 subscription → 1 * 100 = 100
2. For 10 friends with cost 120:
   - 10 friends need ceil(10/6) = 2 subscriptions → 2 * 120 = 240
3. For 5 friends with cost 50:
   - 5 friends fit in 1 subscription → 1 * 50 = 50
"""
import math


# T = int(input())

# for _ in range(T):
#     N, X = map(int, input().split())
#     subscriptions_needed = math.ceil(N / 6)
#     total_cost = subscriptions_needed * X
#     print(total_cost)

T = int(input())

for _ in range(T):
    x = int(input())
    x+=3
    if(x>10):
        print("N0")
    else:
        print("Yes") 
