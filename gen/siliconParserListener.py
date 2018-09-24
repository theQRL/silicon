# Generated from siliconParser.g4 by ANTLR 4.5.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .siliconParser import siliconParser
else:
    from siliconParser import siliconParser

# This class defines a complete listener for a parse tree produced by siliconParser.
class siliconParserListener(ParseTreeListener):

    # Enter a parse tree produced by siliconParser#sourceUnit.
    def enterSourceUnit(self, ctx:siliconParser.SourceUnitContext):
        pass

    # Exit a parse tree produced by siliconParser#sourceUnit.
    def exitSourceUnit(self, ctx:siliconParser.SourceUnitContext):
        pass


    # Enter a parse tree produced by siliconParser#statement.
    def enterStatement(self, ctx:siliconParser.StatementContext):
        pass

    # Exit a parse tree produced by siliconParser#statement.
    def exitStatement(self, ctx:siliconParser.StatementContext):
        pass


    # Enter a parse tree produced by siliconParser#assignmentStatement.
    def enterAssignmentStatement(self, ctx:siliconParser.AssignmentStatementContext):
        pass

    # Exit a parse tree produced by siliconParser#assignmentStatement.
    def exitAssignmentStatement(self, ctx:siliconParser.AssignmentStatementContext):
        pass


    # Enter a parse tree produced by siliconParser#expression.
    def enterExpression(self, ctx:siliconParser.ExpressionContext):
        pass

    # Exit a parse tree produced by siliconParser#expression.
    def exitExpression(self, ctx:siliconParser.ExpressionContext):
        pass


    # Enter a parse tree produced by siliconParser#number.
    def enterNumber(self, ctx:siliconParser.NumberContext):
        pass

    # Exit a parse tree produced by siliconParser#number.
    def exitNumber(self, ctx:siliconParser.NumberContext):
        pass


    # Enter a parse tree produced by siliconParser#identifier.
    def enterIdentifier(self, ctx:siliconParser.IdentifierContext):
        pass

    # Exit a parse tree produced by siliconParser#identifier.
    def exitIdentifier(self, ctx:siliconParser.IdentifierContext):
        pass


