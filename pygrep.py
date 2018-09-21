import argparse, re

parser = argparse.ArgumentParser()
parser.add_argument('-v', '--verbose', help='log more verbosely', action='store_true')
parser.add_argument('file', help='file to search for matching pattern')
parser.add_argument('pattern', help='pattern to search input file for matching lines')

args = parser.parse_args()

if(args.verbose):
    print('Verbose Mode Enabled')
    print('Input File: ', args.file)
    print('Pattern: ', args.pattern)

file = open(args.file, 'r')

for line in file:
    if line.lower().find(args.pattern.lower()) > 0:
        print(line)

file.close()