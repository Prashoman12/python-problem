"""
Problem: Greater Average

You are given three integers A, B, and C.
Determine whether the average of A and B is strictly greater than C.

Average of A and B is defined as (A + B) / 2.

Input Format:
- The first line contains a single integer T, denoting the number of test cases.
- Each test case consists of three integers A, B, and C.

Output Format:
- For each test case, output "YES" if average of A and B is strictly greater than C, else "NO".
- You can print YES/NO in uppercase or lowercase.

Constraints:
- 1 ≤ T ≤ 1000
- 1 ≤ A, B, C ≤ 10

Sample Input:
5
5 9 6
5 8 6
5 7 6
4 9 8
3 7 2

Sample Output:
YES
YES
NO
NO
YES

Explanation:
1. Average of 5 and 9 is 7 → 7 > 6 → YES
2. Average of 5 and 8 is 6.5 → 6.5 > 6 → YES
3. Average of 5 and 7 is 6 → 6 is not > 6 → NO
4. Average of 4 and 9 is 6.5 → 6.5 is not > 8 → NO
5. Average of 3 and 7 is 5 → 5 > 2 → YES
"""

size = int(input(""))

for i in range(size):
    a,b,c = map(int, input("").split())
    if (a + b) / 2 > c:
        print("YES")
    else:
        print("NO")