from typing import Any


def puzzle(input: str) -> Any:
    numbers = [int(num) for num in input.splitlines()]
    n = len(numbers)
    numbers.sort()
    for idx, first_num in enumerate(numbers):
        compliment = 2020 - first_num
        left = idx + 1
        right = n - 1
        while left < right:
            sum = numbers[left] + numbers[right]
            if sum == compliment:
                return first_num * numbers[left] * numbers[right]
            elif sum > compliment:
                right -= 1
            else:
                left += 1
