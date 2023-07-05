# implement an argument parser to parse (for me) command-line arguments

import argparse

# Instantiate the arg parser object
parser = argparse.ArgumentParser(description="Meow like a cat")

# Specify the arguments, default values, types, and help text
parser.add_argument("-n", "--number", default=1, type=int, dest="num", help="number of times to meow", metavar="integer")
parser.add_argument("-v", "--voice", default="meow", type=str, help="voice to use", metavar="string")

# add the above arguments to the parser object
args = parser.parse_args()

for _ in range(args.num):
    print(args.voice)

