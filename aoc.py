import os
import time
import argparse
import requests
from contextlib import suppress
from typing import Literal
from dotenv import load_dotenv
from datetime import datetime
import importlib

PUZZLE_LOCATION = "puzzles"

PUZZLE_STUB = """from typing import Any


def puzzle(input: str) -> Any: ...
"""

HEADERS = {
    "User-Agent": "https://github.com/Spacerulerwill/aoc by williamdredding@proton.me"
}


def init_puzzle(year: int, day: int, part: int, force: bool) -> None:
    folder_path = os.path.join(PUZZLE_LOCATION, f"Y{year}", f"D{day}")
    puzzle_name = os.path.join(folder_path, f"p{part}.py")
    os.makedirs(folder_path, exist_ok=True)
    # each year is a separate module
    with suppress(FileExistsError):
        with open(os.path.join(PUZZLE_LOCATION, f"Y{year}", "__init__.py"), "w+"):
            pass

    # Create or overwrite the puzzle file
    try:
        with open(puzzle_name, "x") as f:
            f.write(PUZZLE_STUB)
    except FileExistsError:
        if force:
            with open(puzzle_name, "w") as f:
                f.write(PUZZLE_STUB)
            print(f"Overwrote puzzle {year}/{day} part {part}")
        else:
            print(f"Puzzle {year}/{day} part {part} exists, use -f flag to overwrite")
            return

    print(f"Created puzzle {year}/{day} part {part}")


def run_puzzle(year: int, day: int, part: int, aoc_session_cookie: str) -> None:
    input_path = os.path.join(PUZZLE_LOCATION, f"Y{year}", f"D{day}", "input.txt")
    if not os.path.isfile(input_path):
        cookies = {"session": aoc_session_cookie}
        r = requests.get(
            f"https://adventofcode.com/{year}/day/{day}/input",
            cookies=cookies,
            headers=HEADERS,
        )
        r.raise_for_status()
        input = r.text
        with open(input_path, "w+") as f:
            f.write(input)
    with open(input_path) as f:
        input = f.read()
    module = importlib.import_module(f"puzzles.Y{year}.D{day}.p{part}")

    puzzle = getattr(module, "puzzle")
    print(f"Running Advent of Code {year}, day {day}, part {part}")
    start = time.perf_counter()
    result = puzzle(input)
    end = time.perf_counter()
    elapsed_time = end - start
    seconds = int(elapsed_time)
    milliseconds = int((elapsed_time - seconds) * 1000)

    print(f"Output:\n{result}")
    print(f"Executed in {seconds}:{milliseconds:03}")


def run_driver() -> None:
    # folder setup
    os.makedirs(PUZZLE_LOCATION, exist_ok=True)
    load_dotenv()
    aoc_session_cookie = os.environ["AOC_SESSION_COOKIE"]

    # Determine most recent AOC year
    now = datetime.now()
    current_year = now.year if now.month == 12 else now.year - 1

    # Create the root parser
    root_parser = argparse.ArgumentParser(
        prog="aoc.py", description="Run advent of code solutions"
    )
    subparsers = root_parser.add_subparsers(required=True, dest="command")
    # run command
    run_parser = subparsers.add_parser("run", help="Run an advent of code solution")
    # init command
    init_parser = subparsers.add_parser(
        "init", help="Generate boilerplate for a solution"
    )
    # both commands have the same arguments
    for parser in (run_parser, init_parser):
        parser.add_argument(
            "year", type=int, help=f"which year (2015 - {current_year})"
        )
        parser.add_argument("day", type=int, help="which day (1 - 25 inclusive)")
        parser.add_argument(
            "part",
            choices=["1", "2", "both"],
            help="which part",
        )
    # init has an optional -f --force flag to overwrite existing files
    init_parser.add_argument(
        "-f", "--force", action="store_true", help="overwrite existing puzzle code"
    )

    # Parse the arguments
    args = root_parser.parse_args()
    command: Literal["run", "init"] = args.command

    # Validate year range
    year: int = args.year
    if year < 2015 or year > current_year:
        print(f"Year must be between 2015 and {current_year}.")
        return

    # Validate day range
    day: int = args.day
    if day < 1 or day > 25:
        print("Day must be in range 1-25 inclusive.")
        return

    # Get parts
    selected_part: Literal["1", "2", "both"] = args.part
    if selected_part == "1":
        parts = [1]
    elif selected_part == "2":
        parts = [2]
    elif selected_part == "both":
        parts = [1, 2]
    else:
        raise ValueError("Invalid part selection, report as a bug")

    if command == "init":
        force: bool = args.force
        for part in parts:
            init_puzzle(year, day, part, force)
    elif command == "run":
        for part in parts:
            try:
                run_puzzle(year, day, part, aoc_session_cookie)
            except (ModuleNotFoundError, FileNotFoundError):
                print(
                    f"Puzzle {year}/{day} part {part} not found - to create, run python aoc.py init {year} {day} {part}"
                )


if __name__ == "__main__":
    run_driver()
