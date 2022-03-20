import sys
from token import Token, TokenType

class Lexer:
    def __init__(self, input):
        self.source = input + '\n'
        self.curChar = ''
        self.curPos = -1
        self.next_char()

    def next_char(self):
        self.curPos += 1
        if self.curPos >= len(self.source):
            self.curChar = '\0'
        else:
            self.curChar = self.source[self.curPos]

    def abort(self, message):
        sys.exit('Lexing error. ' + message)

    def peek(self):
        if self.curPos + 1 >= len(self.source):
            return '\0'
        else:
            return self.source[self.curPos + 1]

    def skip_whitespace(self):
        while self.curChar == ' ' or self.curChar == '\t' or self.curChar == '\n':
            self.next_char()

    def skip_comments(self):
        if self.curChar == '#':
            self.next_char()
            while self.curChar != '\n': 
                self.next_char()

    def get_token(self):

        self.skip_whitespace()
        self.skip_comments()
        
        token = None

        if self.curChar == '=':
            if self.peek() == '=':
                last_char = self.curChar
                self.next_char()
                token = Token(last_char + self.curChar, TokenType.EQEQ)
            else:
                token = Token(self.curChar, TokenType.EQ)
        elif self.curChar == '+':
            token = Token(self.curChar, TokenType.PLUS)
        elif self.curChar == '-':
            token = Token(self.curChar, TokenType.MINUS)
        elif self.curChar == '*':
            token = Token(self.curChar, TokenType.ASTERISK)
        elif self.curChar == '/':
            token = Token(self.curChar, TokenType.SLASH)
        elif self.curChar == '\n':
            token = Token(self.curChar, TokenType.NEWLINE)
        elif self.curChar == '\0':
            token = Token(self.curChar, TokenType.EOF)

        else:
            self.abort('Unknown Token: ' + self.curChar)
             
        
        self.next_char()

        return token
