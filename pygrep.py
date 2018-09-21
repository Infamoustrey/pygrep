import argparse, re, sys

# handle arguments
parser = argparse.ArgumentParser(
    description='A grep clone written in python')

parser.add_argument('file', help='file to search for matching pattern')
parser.add_argument('pattern', nargs='?', default='', help='pattern to search input file for matching lines')
parser.add_argument('-e', '--expression', action='append', help='pattern to search input file for matching lines')
parser.add_argument('-v', '--verbose', help='log more verbosely', action='store_true')

args = parser.parse_args() 
 
def outputLinesIncludingPattern():
    
    # Open File and Print out matching lines
    file = open(args.file, 'r')

    for line in file:
        if line.lower().find(args.pattern.lower()) > 0:
            print('>',line)

    file.close()

    return 

# need to refactor to use regular expression
def outputLinesMatchingRegularExpressions():
    
    file = open(args.file, 'r')

    for line in file:
        if line.lower().find(args.pattern.lower()) > 0:
            print('>',line)

    file.close()    

    return

# Check to see if using regular expression
if args.pattern != '': 
    outputLinesIncludingPattern()
elif args.expression:
    outputLinesMatchingRegularExpressions()
elif args.pattern != '' and not args.expression:
    sys.exit('No Valid Pattern Found')

