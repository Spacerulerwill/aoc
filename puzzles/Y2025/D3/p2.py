from typing import Any


def calculate_best_joltage(bank: list[int]) -> int:
    # dp[i][j] = the largest number you can form by picking exactly j digits from the first i digits of the bank.
    dp = [[0 for _ in range(13)] for _ in range(len(bank) + 1)]
    # fill in the first column (maximum you can make by picking 1 digit from the first i digits of the bank)
    for i in range(1, len(bank) + 1):
        dp[i][1] = max(bank[i - 1], dp[i - 1][1])
    for j in range(2, 13):
        for i in range(j, len(bank) + 1):
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1] * 10 + bank[i - 1])
    return dp[-1][-1]


# similar to max subsequence of length k
def puzzle(input: str) -> Any:
    banks = input.splitlines()
    return sum(
        calculate_best_joltage([int(battery) for battery in bank]) for bank in banks
    )


if __name__ == "__main__":
    print(calculate_best_joltage([2, 3, 4, 2, 3, 4, 2, 3, 4, 2, 3, 4, 2, 7, 8]))
