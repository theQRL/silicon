# Generated from siliconParser.g4 by ANTLR 4.5.3
# encoding: utf-8
from antlr4 import *
from io import StringIO

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3\7")
        buf.write("\63\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\3")
        buf.write("\2\7\2\20\n\2\f\2\16\2\23\13\2\3\2\3\2\3\3\3\3\3\4\3\4")
        buf.write("\3\4\3\4\3\5\3\5\3\5\7\5 \n\5\f\5\16\5#\13\5\3\5\3\5\3")
        buf.write("\5\7\5(\n\5\f\5\16\5+\13\5\5\5-\n\5\3\6\3\6\3\7\3\7\3")
        buf.write("\7\2\2\b\2\4\6\b\n\f\2\2\60\2\21\3\2\2\2\4\26\3\2\2\2")
        buf.write("\6\30\3\2\2\2\b,\3\2\2\2\n.\3\2\2\2\f\60\3\2\2\2\16\20")
        buf.write("\5\4\3\2\17\16\3\2\2\2\20\23\3\2\2\2\21\17\3\2\2\2\21")
        buf.write("\22\3\2\2\2\22\24\3\2\2\2\23\21\3\2\2\2\24\25\7\2\2\3")
        buf.write("\25\3\3\2\2\2\26\27\5\6\4\2\27\5\3\2\2\2\30\31\5\f\7\2")
        buf.write("\31\32\7\6\2\2\32\33\5\b\5\2\33\7\3\2\2\2\34!\5\n\6\2")
        buf.write("\35\36\7\5\2\2\36 \5\b\5\2\37\35\3\2\2\2 #\3\2\2\2!\37")
        buf.write("\3\2\2\2!\"\3\2\2\2\"-\3\2\2\2#!\3\2\2\2$)\5\f\7\2%&\7")
        buf.write("\5\2\2&(\5\b\5\2\'%\3\2\2\2(+\3\2\2\2)\'\3\2\2\2)*\3\2")
        buf.write("\2\2*-\3\2\2\2+)\3\2\2\2,\34\3\2\2\2,$\3\2\2\2-\t\3\2")
        buf.write("\2\2./\7\3\2\2/\13\3\2\2\2\60\61\7\4\2\2\61\r\3\2\2\2")
        buf.write("\6\21!),")
        return buf.getvalue()


class siliconParser ( Parser ):

    grammarFileName = "siliconParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'='" ]

    symbolicNames = [ "<INVALID>", "Number", "Identifier", "BinaryOp", "AssignmentOp", 
                      "WS" ]

    RULE_sourceUnit = 0
    RULE_statement = 1
    RULE_assignmentStatement = 2
    RULE_expression = 3
    RULE_number = 4
    RULE_identifier = 5

    ruleNames =  [ "sourceUnit", "statement", "assignmentStatement", "expression", 
                   "number", "identifier" ]

    EOF = Token.EOF
    Number=1
    Identifier=2
    BinaryOp=3
    AssignmentOp=4
    WS=5

    def __init__(self, input:TokenStream):
        super().__init__(input)
        self.checkVersion("4.5.3")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class SourceUnitContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(siliconParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(siliconParser.StatementContext)
            else:
                return self.getTypedRuleContext(siliconParser.StatementContext,i)


        def getRuleIndex(self):
            return siliconParser.RULE_sourceUnit

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSourceUnit" ):
                listener.enterSourceUnit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSourceUnit" ):
                listener.exitSourceUnit(self)




    def sourceUnit(self):

        localctx = siliconParser.SourceUnitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_sourceUnit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 15
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==siliconParser.Identifier:
                self.state = 12
                self.statement()
                self.state = 17
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 18
            self.match(siliconParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignmentStatement(self):
            return self.getTypedRuleContext(siliconParser.AssignmentStatementContext,0)


        def getRuleIndex(self):
            return siliconParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = siliconParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 20
            self.assignmentStatement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AssignmentStatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(siliconParser.IdentifierContext,0)


        def AssignmentOp(self):
            return self.getToken(siliconParser.AssignmentOp, 0)

        def expression(self):
            return self.getTypedRuleContext(siliconParser.ExpressionContext,0)


        def getRuleIndex(self):
            return siliconParser.RULE_assignmentStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignmentStatement" ):
                listener.enterAssignmentStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignmentStatement" ):
                listener.exitAssignmentStatement(self)




    def assignmentStatement(self):

        localctx = siliconParser.AssignmentStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_assignmentStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 22
            self.identifier()
            self.state = 23
            self.match(siliconParser.AssignmentOp)
            self.state = 24
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def number(self):
            return self.getTypedRuleContext(siliconParser.NumberContext,0)


        def BinaryOp(self, i:int=None):
            if i is None:
                return self.getTokens(siliconParser.BinaryOp)
            else:
                return self.getToken(siliconParser.BinaryOp, i)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(siliconParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(siliconParser.ExpressionContext,i)


        def identifier(self):
            return self.getTypedRuleContext(siliconParser.IdentifierContext,0)


        def getRuleIndex(self):
            return siliconParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)




    def expression(self):

        localctx = siliconParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_expression)
        try:
            self.state = 42
            token = self._input.LA(1)
            if token in [siliconParser.Number]:
                self.enterOuterAlt(localctx, 1)
                self.state = 26
                self.number()
                self.state = 31
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 27
                        self.match(siliconParser.BinaryOp)
                        self.state = 28
                        self.expression() 
                    self.state = 33
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,1,self._ctx)


            elif token in [siliconParser.Identifier]:
                self.enterOuterAlt(localctx, 2)
                self.state = 34
                self.identifier()
                self.state = 39
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 35
                        self.match(siliconParser.BinaryOp)
                        self.state = 36
                        self.expression() 
                    self.state = 41
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,2,self._ctx)


            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class NumberContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Number(self):
            return self.getToken(siliconParser.Number, 0)

        def getRuleIndex(self):
            return siliconParser.RULE_number

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumber" ):
                listener.enterNumber(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumber" ):
                listener.exitNumber(self)




    def number(self):

        localctx = siliconParser.NumberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_number)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            self.match(siliconParser.Number)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class IdentifierContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(siliconParser.Identifier, 0)

        def getRuleIndex(self):
            return siliconParser.RULE_identifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdentifier" ):
                listener.enterIdentifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdentifier" ):
                listener.exitIdentifier(self)




    def identifier(self):

        localctx = siliconParser.IdentifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            self.match(siliconParser.Identifier)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





