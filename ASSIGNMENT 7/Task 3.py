def helper(n, memo):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if memo[n] != -1:
        return memo[n]
    memo[n] = helper(n - 1, memo) + helper(n - 2, memo)
    return memo[n]

def climbingStairs(n):
    memo = [-1] * (n + 1)
    return helper(n, memo)

input_file = open('input3_4.txt' , 'r')
output_file = open('output3_4.txt', 'w')
n = int(input_file.readline())
output_file.write(str(climbingStairs(n)))
input_file.close()
output_file.close()
