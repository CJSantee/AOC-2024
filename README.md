# Advent of Code 2024
## What is Advent of Code?
[Advent of Code](https://adventofcode.com/2024/about) is an Advent calendar of small programming puzzles for a variety of skill levels that can be solved in any programming language you like.

## Running Programs
### Running individual program:
Run the following command with the `-t` flag to provide the test.txt file as input, run without any flag to provide the input.txt file as input, and run with the -f flag to specify a different file to provide as input.
```bash
python3 -m <directory>.<python_module> [-t | -f <input_filename>]
```

### Running with the run script:
Add run permissions to bash script:
```bash
chmod u+x run.sh
```
Install [fzf](https://github.com/junegunn/fzf):
```bash
brew install fzf
```
Run script:
```bash
./run.sh
```

## Naming Conventions

Python follows the PEP 8 style guide for naming conventions. Here's a summary:
### General Guidelines:
**Be descriptive:** Choose names that clearly convey the purpose of the variable, function, class, etc.

**Use lowercase with underscores for most names:** This applies to variables, functions, modules, and packages (e.g., my_variable, calculate_average).

**Use CamelCase for classes:** Capitalize the first letter of each word (e.g., MyClass, ShoppingCart).

**Use ALL_CAPS for constants:** Use uppercase letters with underscores to separate words (e.g., MAX_VALUE, PI).
Avoid single-letter names: Except for simple loop counters or iterators (e.g., i, j).

### Specific Cases:
**Packages:** Short, all-lowercase names (e.g., requests, numpy).

**Modules:** Short, all-lowercase names, underscores allowed (e.g., my_module, utils).

**Classes:** CamelCase (e.g., MyClass, ShoppingCart).

**Functions and Methods:** Lowercase with underscores (e.g., calculate_average, get_user_data).

**Variables:** Lowercase with underscores (e.g., my_variable, user_name).

**Constants:** All uppercase with underscores (e.g., MAX_VALUE, PI).

**Private variables and methods:** Prefix with a single underscore (e.g., _my_private_variable, _calculate_something).

**Class-private variables and methods:** Prefix with two underscores (e.g., __my_private_variable, __calculate_something).