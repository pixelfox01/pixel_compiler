from posixpath import lexists
from lexer import Lexer


def main():
    code = '+= # this is a new comment \n \"This is a string\" /*'
    lexer = Lexer(code)

    while lexer.peek() != '\0':
        print(lexer.get_token().kind)


main()
