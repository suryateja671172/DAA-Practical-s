n = int(input("Enter number of coins: "))
coins = []
for i in range(n):
    coin = int(input("Enter coin value: "))
    coins.append(coin)

amount = int(input("Enter amount: "))

dp = [0] + [n] * amount

for i in range(1, amount + 1):
    for coin in coins:
        if coin <= i:
            dp[i] = min(dp[i], dp[i - coin] + 1)

print ("Minimum number of coins:", dp[amount])