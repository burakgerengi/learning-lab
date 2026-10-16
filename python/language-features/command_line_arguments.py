import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-x", type = int, help = "first value for the sum.")
parser.add_argument("-y", type = int, help = "second value for the sum.")

# reads the arguments supplied.
# the result is stored in args, typically as an argparse.Namespace
# parse_args() should come after the parser is created and define its arguments with add_argument(),
# so it knows what to look for.
args = parser.parse_args()

print(args.x + args.y)