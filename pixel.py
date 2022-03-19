from posixpath import lexists
from lexer import Lexer


def main():
    input = 'LET foobar = 123'
    lexer = Lexer(input)

    while lexer.peek() != '\0':
        print(lexer.curChar)
        lexer.next_char()


main()
