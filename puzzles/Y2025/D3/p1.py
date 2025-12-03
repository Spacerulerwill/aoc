from typing import Any


def get_max_after_array(bank: list[int]) -> list[int]:
    # each index in max after corresponds to the maximum battery after the battery in the bank at that index
    # we don't need the last one because we must turn on exactly two batteries
    max_after = [0] * len(bank)
    current_max = bank[-1]
    for i in range(len(max_after) - 2, -1, -1):
        max_after[i] = current_max
        current_max = max(bank[i], current_max)
    return max_after


def puzzle(input: str) -> Any:
    banks = input.splitlines()
    total = 0
    for str_bank in banks:
        bank = [int(battery) for battery in str_bank]
        max_after = get_max_after_array(bank)
        current_max = 0
        for i in range(len(bank) - 1):
            battery = bank[i]
            value = battery * 10 + max_after[i]
            current_max = max(current_max, value)
        print(current_max)
        total += current_max
    return total


if __name__ == "__main__":
    print(get_max_after_array([9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 1, 1, 1, 1]))
    print(get_max_after_array([8, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9]))
    print(get_max_after_array([2, 3, 4, 2, 3, 4, 2, 3, 4, 2, 3, 4, 2, 7, 8]))
    print(get_max_after_array([8, 1, 8, 1, 8, 1, 9, 1, 1, 1, 1, 2, 1, 1, 1]))

    print(
        puzzle("""987654321111111
811111111111119
234234234234278
818181911112111""")
    )
