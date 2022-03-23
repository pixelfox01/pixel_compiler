import sys
from lexer import Lexer

class Parser:
    def __init__(self, lexer):
        self.lexer = lexer
        self.curToken = None
        self.peekToken = None
        self.next_token()
        self.next_token()

    def check_token(self, kind):
        return kind == self.curToken

    def check_peek(self, kind):
        return kind == self.peekToken

    def match(self, kind):
        if not self.check_token(kind):
            self.abort('Expected: ' + kind.name + ', got: ' + self.curToken.kind)
        self.next_token()

    def next_token(self):
        self.curToken = self.peekToken
        self.peekToken = self.lexer.get_token()

    def abort(self, message):
        sys.exit('Error: ' + message)
