#!/bin/sh
# Get a list of directories in the current working directory, excluding . and .git
directories=$(find . -maxdepth 1 -type d ! -name "." ! -name ".git" ! -name "utils" | sed 's|^\./||; s/-/: /1; s/_/ /g' | sort)

# Check if there are any directories
if [ -z "$directories" ]; then
  echo "No directories found in the current working directory."
  exit 1
fi

# Use fzf to let the user select a folder
day_selection=$(printf "%s\n" "$directories" | fzf --height 10 --reverse --border --prompt="Select a day: ")

# Handle the user's choice
if [ -z "$day_selection" ]; then
  echo "No day selected. Exiting..."
  exit 1
else
  directory=$(echo "$day_selection" | sed 's/: /-/g; s/ /_/g')
  script=$(echo "$directory" | sed 's/^[^-]*-//; s/_//g')
fi

input_files=$(find "./$directory" -maxdepth 1 -type f -name "*.txt" | sed 's:.*/::')

# Use fzf to let the user select an input file
file_selection=$(printf "%s\n" "$input_files" | fzf --height 10 --reverse --border --prompt="Select an input file: ")

# Use the file selection to run the python script
if [ -z "$file_selection" ]; then
  echo "No input file selected. Exiting..."
  exit 1
else 
  echo "Running script for day $day_selection with input from $file_selection:"
  python3 -m "$directory.$script" -f $file_selection
fi
