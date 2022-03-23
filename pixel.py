from lexer import Lexer
import sys


def main():
    if len(sys.argv) != 2:
        sys.exit('Error: Compiler needs a source code file')
    with open(sys.argv[1], 'r') as inputFile:
        sourceCode = inputFile.read()

    lexer = Lexer(sourceCode)

main()
