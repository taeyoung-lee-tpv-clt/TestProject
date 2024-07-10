# python3
import math

from typing import List,Dict
INF = 9999
Type = int
Coins = List[Type]
Memo = Dict[Type, Type]

class RECsoulution:
    def minCoins(self, C: Coins, T:Type) -> Type:
        return self.go(C,T)
    def go(self, C:Coins, T:Type, memo: Memo = {}, ans : Type= INF)-> Type:
        if T == 0: return 0
        if T in memo : return memo[T]
        for coin in C:
            if 0 <= T - coin:
                cnt = 1 + self.go(C, T - coin, memo)
                ans = min(ans, cnt)
        memo[T] = ans
        return ans
class DPsolution:
    def minCoins(self, c: Coins, T:Type) -> Type:
        dp = [INF] * (T + 1)
        dp[0] = 0
        for i in range(T+1):
            for coin in C:
                if 0 <= i - coin:
                    dp[i] = min(dp[i], 1 + dp[i-coin])
        return dp[T]


if __name__ == '__main__':
    rec_solution = RECsoulution()
    dp_solution = DPsolution()
    C = [1,3,4]
    T = int(input())
    rec_ans = rec_solution.minCoins(C,T)
    dp_ans = dp_solution.minCoins(C,T)
    assert(rec_ans == dp_ans)
    print(rec_ans)