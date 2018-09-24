# Generated from silicon.g4 by ANTLR 4.5.3
from antlr4 import *
from io import StringIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\2\t")
        buf.write("\63\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t")
        buf.write("\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\3\2\3\2\3\3\3\3\3")
        buf.write("\4\3\4\3\5\3\5\3\6\3\6\3\7\6\7#\n\7\r\7\16\7$\3\b\3\b")
        buf.write("\3\t\3\t\3\n\3\n\3\13\3\13\7\13/\n\13\f\13\16\13\62\13")
        buf.write("\13\2\2\f\3\3\5\4\7\5\t\6\13\7\r\b\17\2\21\2\23\2\25\t")
        buf.write("\3\2\5\5\2C\\aac|\6\2\62;C\\aac|\3\2\62;\61\2\3\3\2\2")
        buf.write("\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2")
        buf.write("\r\3\2\2\2\2\25\3\2\2\2\3\27\3\2\2\2\5\31\3\2\2\2\7\33")
        buf.write("\3\2\2\2\t\35\3\2\2\2\13\37\3\2\2\2\r\"\3\2\2\2\17&\3")
        buf.write("\2\2\2\21(\3\2\2\2\23*\3\2\2\2\25,\3\2\2\2\27\30\7?\2")
        buf.write("\2\30\4\3\2\2\2\31\32\7-\2\2\32\6\3\2\2\2\33\34\7/\2\2")
        buf.write("\34\b\3\2\2\2\35\36\7,\2\2\36\n\3\2\2\2\37 \7\61\2\2 ")
        buf.write("\f\3\2\2\2!#\5\23\n\2\"!\3\2\2\2#$\3\2\2\2$\"\3\2\2\2")
        buf.write("$%\3\2\2\2%\16\3\2\2\2&\'\t\2\2\2\'\20\3\2\2\2()\t\3\2")
        buf.write("\2)\22\3\2\2\2*+\t\4\2\2+\24\3\2\2\2,\60\5\17\b\2-/\5")
        buf.write("\21\t\2.-\3\2\2\2/\62\3\2\2\2\60.\3\2\2\2\60\61\3\2\2")
        buf.write("\2\61\26\3\2\2\2\62\60\3\2\2\2\5\2$\60\2")
        return buf.getvalue()


class siliconLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]


    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    Number = 6
    Identifier = 7

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'='", "'+'", "'-'", "'*'", "'/'" ]

    symbolicNames = [ "<INVALID>",
            "Number", "Identifier" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "Number", "IdentifierStart", 
                  "IdentifierPart", "Digit", "Identifier" ]

    grammarFileName = "silicon.g4"

    def __init__(self, input=None):
        super().__init__(input)
        self.checkVersion("4.5.3")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


