from posixpath import lexists
from lexer import Lexer


def main():
    code = '+- #this is a comment   \n +==-'
    lexer = Lexer(code)

    while lexer.peek() != '\0':
        print(lexer.get_token().kind)


main()
