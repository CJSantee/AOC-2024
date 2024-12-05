import sys

def get_input_filename():
  # Check for flag
  flag = ''
  if len(sys.argv) > 1:
    flag = sys.argv[1]

  # Get the directory and file
  directory, file = sys.argv[0].split('/')[-2:]

  # Get the main input or test input if -t/--test flag is used
  filename = 'test.txt' if (flag.lower() == '-t' or flag.lower() == '--test') else 'input.txt'

  filename = '/'.join([directory, filename])

  return filename
