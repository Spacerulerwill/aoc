# Advent of Code solutions
```bash
git clone https://github.com/SpaceCases/aoc                 # Clone repository to local machine
cd aoc                                                      # Move into directory
uv sync
mv .env.example .env                                        # Rename .env.example to .env
```
Then use your preferred text editor of choice to add your session cookie to `.env`. Once that is setup, you can run the program:
```bash
uv run aoc.py run <year> <day> <part>                       # Run a solution
```