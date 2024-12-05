#!/bin/sh
# Get a list of directories in the current working directory, excluding . and .git
directories=$(find . -maxdepth 1 -type d ! -name "." ! -name ".git" ! -name "utils" | sed 's|^\./||; s/-/: /g; s/_/ /g')

# Check if there are any directories
if [ -z "$directories" ]; then
  echo "No directories found in the current working directory."
  exit 1
fi

# Use fzf to let the user select a folder
selection=$(printf "%s\n" "$directories" | fzf --height 10 --reverse --border --prompt="Select a day: ")

# Handle the user's choice
if [ -z "$selection" ]; then
  echo "No day selected. Exiting..."
  exit 1
else
  echo "Running script for day $selection"
  directory=$(echo "$selection" | sed 's/: /-/g; s/ /_/g')
  script=$(echo "$directory" | sed 's/^[^-]*-//; s/_//g')
  python3 -m "$directory.$script"
fi