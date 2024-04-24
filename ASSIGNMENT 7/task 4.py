def coinChange(coins, amount):
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    return dp[amount] if dp[amount] <= amount else -1


input_file = open('input4_1.txt', 'r')
amount = int(input_file.readline().split()[1])
coins = list(map(int, input_file.readline().split()))
print(coinChange(coins, amount))
output_file = open('output4_1.txt', 'w')
output_file.write(str(coinChange(coins, amount)))