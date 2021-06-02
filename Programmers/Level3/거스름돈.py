def solution(n, money):
    answer = 0;
    
    dp = [1] + [0] * n;
    #print("초기상태의 dp는", dp);
    
    for coin in money:
        #print("coin은, ", coin);
        for price in range(coin, n + 1):
            #print("price는, ", price);
            if price >= coin:
                #rint("여기!")
                dp[price] += dp[price - coin];
                #print(dp)
    
    #print("====최종결과====");
    #print(dp)
    return dp[n] % 1000000007