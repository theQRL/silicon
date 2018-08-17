from Tokenizer.TokenDesc import TokenDesc
from Tokenizer.Tokens import get_token, Tokens, keywords


class Scanner:
    def __init__(self, filename):
        self.sourceName = filename
        with open(filename, 'r') as f:
            self.source = f.read()
        self.sourceLen = len(self.source)
        self.char = ""
        self.pos = -1
        self.m_currentToken = None
        self.m_nextToken = None
        self.reset()

    def reset(self):
        self.pos = 0
        self.char = self.source[0]
        self.skipWhitespace()
        self.scanToken()
        self.next()

    def currentToken(self):
        pass

    def next(self):
        self.m_currentToken = self.m_nextToken
        self.scanToken()
        return self.m_currentToken.token

    def nextToken(self):
        """
        Provides next token, without advancing position
        :return:
        """
        self.m_currentToken = self.m_nextToken

    def sourcePos(self):
        return self.pos

    def isWhitespace(self, c: str):
        return c in [' ', '\n', '\t', '\r']

    def skipWhitespace(self) -> bool:
        startPos = self.pos
        while self.isWhitespace(self.char):
            self.advance()

        return self.pos == startPos

    def advance(self):
        self.pos += 1

        if self.isSourcePastEndOfInput():
            self.char = ''
            return

        self.char = self.source[self.pos]

    def scanIdentifierOrKeyword(self):
        while self.isIdentifierPart(self.char):
            self.addLiteralCharAndAdvance()

        self.m_nextToken.complete()
        if self.m_nextToken.literal in keywords:
            return get_token(keywords[self.m_nextToken.literal])
        else:
            return get_token(Tokens.Identifier)

    def addLiteralChar(self, char):
        self.m_nextToken.addLiteralChar(char)

    def addLiteralCharAndAdvance(self):
        self.addLiteralChar(self.char)
        self.advance()

    def isLineTerminator(self, c: str) -> bool:
        return c == '\n'

    def isSourcePastEndOfInput(self):
        if self.pos == self.sourceLen:
            return True

        return False

    def scanDecimalDigits(self):
        while self.char.isdigit():
            self.addLiteralCharAndAdvance()

    def scanEscape(self) -> bool:
        c = self.char
        self.advance()

        if self.isLineTerminator(c):
            return True

        if c in ['\'', '"', '\\']:
            pass
        elif c in ['b', 'f', 'n', 'r', 't', 'v']:
            c = '\\' + c
        elif c == 'u':
            pass
            # TODO: unicode
        elif c == 'x':
            # TODO: hex byte
            pass

        self.addLiteralChar(c)
        return True

    def scanString(self):
        self.advance()
        while self.char != '"' and not self.isLineTerminator(self.char) and not self.isSourcePastEndOfInput():
            c = self.char
            self.advance()
            if c == '\\':
                if self.isSourcePastEndOfInput() or not self.scanEscape():
                    return Tokens.Invalid
                else:
                    self.addLiteralChar(c)

        if self.char != '"':
            return Tokens.Invalid
        self.m_nextToken.complete()
        self.advance()
        return Tokens.StringLiteral

    def scanNumber(self, charSeen: str=None):
        if charSeen == '.':
            self.addLiteralChar('.')
            self.scanDecimalDigits()
        else:
            self.scanDecimalDigits()
            if self.char == '.':
                if self.isSourcePastEndOfInput() or not self.source[self.pos+1].isdigit():
                    self.m_nextToken.complete()
                    return Tokens.Number
                self.addLiteralCharAndAdvance()
                self.scanDecimalDigits()
            # TODO: Add logic for hexadecimal, octal numbers

        self.m_nextToken.complete()
        return Tokens.Number

    def isIdentifierStart(self, c: str):
        if c.isalpha() or c == '_':
            return True
        return False

    def isIdentifierPart(self, c: str):
        if c.isalpha() or c == '_' or c.isdigit():
            return True
        return False

    def selectToken(self, c: Tokens):
        self.advance()
        return get_token(c)

    def scanToken(self):
        self.m_nextToken = TokenDesc()
        while True:
            self.m_nextToken.start = self.sourcePos()
            if self.char in [' ', '\t', '\n']:
                token = self.selectToken(Tokens.Whitespace)
            elif self.char == '+':
                token = self.selectToken(Tokens.Add)
            elif self.char == '-':
                token = self.selectToken(Tokens.Sub)
            elif self.char == '*':
                token = self.selectToken(Tokens.Mul)
            elif self.char == '/':
                token = self.selectToken(Tokens.Div)
            elif self.char == '**':
                token = self.selectToken(Tokens.Exp)
            elif self.char == '.':
                self.advance()
                if self.char.isdigit():
                    token = self.scanNumber('.')
                else:
                    token = Tokens.Period
            elif self.char == '>':
                # > >= >> >>=
                self.advance()
                if self.char == '=':
                    token = self.selectToken(Tokens.GreaterThanOrEqual)
                else:
                    token = self.selectToken(Tokens.GreaterThan)
            elif self.char == '<':
                # < <= << <<=
                self.advance()
                if self.char == '=':
                    token = self.selectToken(Tokens.LessThanOrEqual)
                else:
                    token = self.selectToken(Tokens.LessThan)
            elif self.char == '=':
                self.advance()
                if self.char == '=':
                    token = self.selectToken(Tokens.Equal)
                else:
                    token = self.selectToken(Tokens.Assign)
            elif self.char == '!':
                self.advance()
                if self.char == '=':
                    token = self.selectToken(Tokens.NotEqual)
                else:
                    token = self.selectToken(Tokens.Not)
            elif self.char == '(':
                token = self.selectToken(Tokens.LParen)
            elif self.char == ')':
                token = self.selectToken(Tokens.RParen)
            elif self.char == '{':
                token = self.selectToken(Tokens.LBrace)
            elif self.char == '}':
                token = self.selectToken(Tokens.RBrace)
            elif self.char == '"':
                token = self.scanString()
            else:
                if self.isIdentifierStart(self.char):
                    token = self.scanIdentifierOrKeyword()
                elif self.char.isdigit():
                    token = self.scanNumber()
                elif self.skipWhitespace():
                    token = Tokens.Whitespace
                elif self.isSourcePastEndOfInput():
                    token = Tokens.EOS
                else:
                    token = Tokens.Invalid

            if token != get_token(Tokens.Whitespace):
                break

        self.m_nextToken.end = self.sourcePos()
        self.m_nextToken.token = token
