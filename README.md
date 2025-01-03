# Advent of Code solutions
```bash
git clone https://github.com/SpaceCases/aoc                 # Clone repository to local machine
cd aoc                                                      # Move into directory
python -m venv env                                          # Create the virtual environment
source env/bin/activate                                     # Activate virtual environment
python -m pip install .                                     # Install dependencies
mv .env.example .env                                        # Rename .env.example to .env
```
Then use your preferred text editor of choice to add your session cookie to the `.env`. Once that is setup, you can run the bot:
```bash
python aoc.py run <year> <day> <part>                       # Run a solution
```