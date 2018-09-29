# Generated from siliconParser.g4 by ANTLR 4.5.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .siliconParser import siliconParser
else:
    from siliconParser import siliconParser

# This class defines a complete generic visitor for a parse tree produced by siliconParser.

class siliconParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by siliconParser#sourceUnit.
    def visitSourceUnit(self, ctx:siliconParser.SourceUnitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by siliconParser#block.
    def visitBlock(self, ctx:siliconParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by siliconParser#statement.
    def visitStatement(self, ctx:siliconParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by siliconParser#assignmentStatement.
    def visitAssignmentStatement(self, ctx:siliconParser.AssignmentStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by siliconParser#identifierFunctionCall.
    def visitIdentifierFunctionCall(self, ctx:siliconParser.IdentifierFunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by siliconParser#printlnFunctionCall.
    def visitPrintlnFunctionCall(self, ctx:siliconParser.PrintlnFunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by siliconParser#printFunctionCall.
    def visitPrintFunctionCall(self, ctx:siliconParser.PrintFunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by siliconParser#ifStatement.
    def visitIfStatement(self, ctx:siliconParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by siliconParser#ifStat.
    def visitIfStat(self, ctx:siliconParser.IfStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by siliconParser#elseIfStat.
    def visitElseIfStat(self, ctx:siliconParser.ElseIfStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by siliconParser#elseStat.
    def visitElseStat(self, ctx:siliconParser.ElseStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by siliconParser#functionDecl.
    def visitFunctionDecl(self, ctx:siliconParser.FunctionDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by siliconParser#forStatement.
    def visitForStatement(self, ctx:siliconParser.ForStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by siliconParser#whileStatement.
    def visitWhileStatement(self, ctx:siliconParser.WhileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by siliconParser#idList.
    def visitIdList(self, ctx:siliconParser.IdListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by siliconParser#exprList.
    def visitExprList(self, ctx:siliconParser.ExprListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by siliconParser#boolExpression.
    def visitBoolExpression(self, ctx:siliconParser.BoolExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by siliconParser#numberExpression.
    def visitNumberExpression(self, ctx:siliconParser.NumberExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by siliconParser#identifierExpression.
    def visitIdentifierExpression(self, ctx:siliconParser.IdentifierExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by siliconParser#notExpression.
    def visitNotExpression(self, ctx:siliconParser.NotExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by siliconParser#orExpression.
    def visitOrExpression(self, ctx:siliconParser.OrExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by siliconParser#unaryMinusExpression.
    def visitUnaryMinusExpression(self, ctx:siliconParser.UnaryMinusExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by siliconParser#powerExpression.
    def visitPowerExpression(self, ctx:siliconParser.PowerExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by siliconParser#eqExpression.
    def visitEqExpression(self, ctx:siliconParser.EqExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by siliconParser#andExpression.
    def visitAndExpression(self, ctx:siliconParser.AndExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by siliconParser#inExpression.
    def visitInExpression(self, ctx:siliconParser.InExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by siliconParser#stringExpression.
    def visitStringExpression(self, ctx:siliconParser.StringExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by siliconParser#expressionExpression.
    def visitExpressionExpression(self, ctx:siliconParser.ExpressionExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by siliconParser#addExpression.
    def visitAddExpression(self, ctx:siliconParser.AddExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by siliconParser#compExpression.
    def visitCompExpression(self, ctx:siliconParser.CompExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by siliconParser#nullExpression.
    def visitNullExpression(self, ctx:siliconParser.NullExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by siliconParser#functionCallExpression.
    def visitFunctionCallExpression(self, ctx:siliconParser.FunctionCallExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by siliconParser#multExpression.
    def visitMultExpression(self, ctx:siliconParser.MultExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by siliconParser#listExpression.
    def visitListExpression(self, ctx:siliconParser.ListExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by siliconParser#ternaryExpression.
    def visitTernaryExpression(self, ctx:siliconParser.TernaryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by siliconParser#inputExpression.
    def visitInputExpression(self, ctx:siliconParser.InputExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by siliconParser#list2.
    def visitList2(self, ctx:siliconParser.List2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by siliconParser#indexes.
    def visitIndexes(self, ctx:siliconParser.IndexesContext):
        return self.visitChildren(ctx)



del siliconParser