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
        elif self.curChar == '!':
            if self.peek() != '=':
                self.abort('Unknown Token: ' + self.curChar)
            else:
                last_char = self.curChar
                self.next_char()
                token = Token(last_char + self.curChar, TokenType.NOTEQ)
        elif self.curChar == '>':
            if self.peek() == '=':
                last_char = self.curChar
                self.next_char()
                token = Token(last_char + self.curChar, TokenType.GTEQ)
            else:
                token = Token(self.curChar, TokenType.GT)
        elif self.curChar == '<':
            if self.peek() == '=':
                last_char = self.curChar
                self.next_char()
                token = Token(last_char + self.curChar, TokenType.LTEQ)
            else:
                token = Token(self.curChar, TokenType.LT)
        elif self.curChar == '\"':
            self.next_char()
            startPos = self.curPos

            while self.curChar != '\"':
                if self.curChar == '\r' or self.curChar == '\n' or self.curChar == '\t' or self.curChar == '\\' or self.curChar == '%':
                    self.abort("Illegal character in string.")
                self.next_char()

            tokText = self.source[startPos : self.curPos]
            token = Token(tokText, TokenType.STRING)
        elif self.curChar.isdigit():
            startPos = self.curPos
            while self.peek().isdigit():
                self.next_char()
            if self.peek() == '.':
                self.next_char()
                if not self.peek().isdigit():
                    self.abort('Illegal character in number!')
                while self.peek().isdigit():
                    self.next_char()

            token = Token(self.source[startPos:self.curPos + 1], TokenType.NUMBER)
            
        elif self.curChar.isalpha():
            startPos = self.curPos
            self.next_char()
            while self.peek().isalnum():
                self.next_char()
            tokenText = self.source[startPos : self.curPos + 1]
            keyword = Token.check_if_keyword(tokenText)

            if keyword == None:
                token = Token(tokenText, TokenType.IDENT)
            else:
                token = Token(tokenText, keyword)

            

        else:
            self.abort('Unknown Token: ' + self.curChar)
             
        
        self.next_char()

        return token
