import sys

def get_input_filename():
  # Check for flag
  flag = ''
  if len(sys.argv) > 1:
    flag = sys.argv[1]

  # Get the directory and file
  directory, file = sys.argv[0].split('/')[-2:]

  # Get the main input or test input if -t/--test flag is used
  if flag.lower() in ['-t', '--test']:
    filename = 'test.txt'
  elif flag.lower() in ['-f', '--file'] and len(sys.argv) > 2:
    filename = sys.argv[2]
  else:
    filename = 'input.txt'

  filename = '/'.join([directory, filename])

  return filename

def get_part():
  part = 'both'
  for index in range(len(sys.argv)):
    arg = sys.argv[index]
    if arg.lower() in ['-p', '--part'] and len(sys.argv) > index + 1:
      part = sys.argv[index + 1]
  return part