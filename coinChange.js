var coinChange = function(coins, amount) {
    // Create dp array with length of amount + 1 (impossible value)
    const dp= new Array(amount + 1).fill(amount + 1);
    dp[0] = 0; // 0 coins needed to make 0 amount

    //Build up solutions for each amount from 1 to amount
    for (let currentAmount = 1; currentAmount <= amount; currentAmount++) {
        // For each coin, check if it can be used to make the current amount
        for (const coin of coins) {
            // If the coin is smaller or equal to the current amount
            if (coin <= currentAmount) {
                // Update the dp array with the minimum number of coins needed
                dp[currentAmount] = Math.min(dp[currentAmount], dp[currentAmount - coin] + 1);
            }
        }
    }
    // If the amount is impossible to make, return -1
    return dp[amount] > amount ? -1 : dp[amount];
};
// Time complexity: O(n*m)
// Space complexity: O(n)
// n = amount, m = coins.length
//Test Cases
console.log(coinChange([1, 2, 5], 11)); //expected output 3
console.log(coinChange([2], 3)); //expected output -1
console.log(coinChange([1], 0)); //expected output0