# Generated from siliconLexer.g4 by ANTLR 4.5.3
from antlr4 import *
from io import StringIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\2\7")
        buf.write("\60\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t")
        buf.write("\7\4\b\t\b\4\t\t\t\3\2\6\2\25\n\2\r\2\16\2\26\3\3\3\3")
        buf.write("\3\4\3\4\3\5\3\5\3\6\3\6\7\6!\n\6\f\6\16\6$\13\6\3\7\3")
        buf.write("\7\3\b\3\b\3\t\6\t+\n\t\r\t\16\t,\3\t\3\t\2\2\n\3\3\5")
        buf.write("\2\7\2\t\2\13\4\r\5\17\6\21\7\3\2\7\5\2C\\aac|\6\2\62")
        buf.write(";C\\aac|\3\2\62;\5\2,-//\61\61\5\2\13\f\16\17\"\"/\2\3")
        buf.write("\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3")
        buf.write("\2\2\2\3\24\3\2\2\2\5\30\3\2\2\2\7\32\3\2\2\2\t\34\3\2")
        buf.write("\2\2\13\36\3\2\2\2\r%\3\2\2\2\17\'\3\2\2\2\21*\3\2\2\2")
        buf.write("\23\25\5\t\5\2\24\23\3\2\2\2\25\26\3\2\2\2\26\24\3\2\2")
        buf.write("\2\26\27\3\2\2\2\27\4\3\2\2\2\30\31\t\2\2\2\31\6\3\2\2")
        buf.write("\2\32\33\t\3\2\2\33\b\3\2\2\2\34\35\t\4\2\2\35\n\3\2\2")
        buf.write("\2\36\"\5\5\3\2\37!\5\7\4\2 \37\3\2\2\2!$\3\2\2\2\" \3")
        buf.write("\2\2\2\"#\3\2\2\2#\f\3\2\2\2$\"\3\2\2\2%&\t\5\2\2&\16")
        buf.write("\3\2\2\2\'(\7?\2\2(\20\3\2\2\2)+\t\6\2\2*)\3\2\2\2+,\3")
        buf.write("\2\2\2,*\3\2\2\2,-\3\2\2\2-.\3\2\2\2./\b\t\2\2/\22\3\2")
        buf.write("\2\2\6\2\26\",\3\b\2\2")
        return buf.getvalue()


class siliconLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]


    Number = 1
    Identifier = 2
    BinaryOp = 3
    AssignmentOp = 4
    WS = 5

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'='" ]

    symbolicNames = [ "<INVALID>",
            "Number", "Identifier", "BinaryOp", "AssignmentOp", "WS" ]

    ruleNames = [ "Number", "IdentifierStart", "IdentifierPart", "Digit", 
                  "Identifier", "BinaryOp", "AssignmentOp", "WS" ]

    grammarFileName = "siliconLexer.g4"

    def __init__(self, input=None):
        super().__init__(input)
        self.checkVersion("4.5.3")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


