from antlr4.ParserRuleContext import ParserRuleContext
from gen.siliconLexer import siliconLexer
from gen.siliconParser import siliconParser
from gen.siliconParserVisitor import siliconParserVisitor
from parser.Scope import Scope
from parser.ReturnValue import ReturnValue
from parser.SiliconValue import SiliconValue


class Visitor(siliconParserVisitor):
    returnValue = ReturnValue()

    def __init__(self, scope: Scope, functions: dict):
        super().__init__()
        self.scope = scope
        self.functions = functions

    # Visit a parse tree produced by siliconParser#sourceUnit.
    def visitSourceUnit(self, ctx: siliconParser.SourceUnitContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by siliconParser#block.
    def visitBlock(self, ctx: siliconParser.BlockContext):
        self.scope = Scope(self.scope)
        for sx in ctx.statement():
            self.visit(sx)
        ex = ctx.expression()
        if ex:
            self.returnValue.value = self.visit(ex)
            self.scope = self.scope.parent
            raise Exception(self.returnValue)
        self.scope = self.scope.parent
        return SiliconValue.VOID

    # Visit a parse tree produced by siliconParser#statement.
    def visitStatement(self, ctx: siliconParser.StatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by siliconParser#assignmentStatement.
    def visitAssignmentStatement(self, ctx: siliconParser.AssignmentStatementContext):
        newVal = self.visit(ctx.expression())
        if ctx.indexes():
            val = self.scope.resolve(ctx.Identifier().getText())
            exps = ctx.indexes().expression()
            self.setAtIndex(ctx, exps, val, newVal)
        else:
            id = ctx.Identifier().getText()
            self.scope.assign(id, newVal)

        return SiliconValue.VOID

    # Visit a parse tree produced by siliconParser#identifierFunctionCall.
    def visitIdentifierFunctionCall(self, ctx: siliconParser.IdentifierFunctionCallContext):
        params = list()
        if ctx.exprList():
            params = ctx.exprList().expression()

        fid = ctx.Identifier().getText() + str(len(params))
        f = self.functions[fid]
        if f:
            return f.invoke(params, self.functions, self.scope)
        raise Exception("Eval Exception")

    # Visit a parse tree produced by siliconParser#printlnFunctionCall.
    def visitPrintlnFunctionCall(self, ctx: siliconParser.PrintlnFunctionCallContext):
        print(self.visit(ctx.expression()))
        return SiliconValue.VOID

    # Visit a parse tree produced by siliconParser#printFunctionCall.
    def visitPrintFunctionCall(self, ctx: siliconParser.PrintFunctionCallContext):
        print(self.visit(ctx.expression()), end='')
        return SiliconValue.VOID

    # Visit a parse tree produced by siliconParser#ifStatement.
    def visitIfStatement(self, ctx: siliconParser.IfStatementContext):
        if self.visit(ctx.ifStat().expression()).asBoolean():
            return self.visit(ctx.ifStat().block())

        for i in range(len(ctx.elseIfStat())):
            if self.visit(ctx.elseIfStat(i).expression()).asBoolean():
                return self.visit(ctx.elseIfStat(i).block())

        if ctx.elseStat():
            return self.visit(ctx.elseStat().block())

        return SiliconValue.VOID

    # Visit a parse tree produced by siliconParser#ifStat.
    def visitIfStat(self, ctx: siliconParser.IfStatContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by siliconParser#elseIfStat.
    def visitElseIfStat(self, ctx: siliconParser.ElseIfStatContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by siliconParser#elseStat.
    def visitElseStat(self, ctx: siliconParser.ElseStatContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by siliconParser#functionDecl.
    def visitFunctionDecl(self, ctx: siliconParser.FunctionDeclContext):
        return SiliconValue.VOID

    # Visit a parse tree produced by siliconParser#forStatement.
    def visitForStatement(self, ctx: siliconParser.ForStatementContext):
        pass

    # Visit a parse tree produced by siliconParser#whileStatement.
    def visitWhileStatement(self, ctx: siliconParser.WhileStatementContext):
        while self.visit(ctx.expression()).asBoolean():
            returnValue = self.visit(ctx.block())
            if returnValue != SiliconValue.VOID:
                return returnValue

        return SiliconValue.VOID

    # Visit a parse tree produced by siliconParser#idList.
    def visitIdList(self, ctx: siliconParser.IdListContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by siliconParser#exprList.
    def visitExprList(self, ctx: siliconParser.ExprListContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by siliconParser#boolExpression.
    def visitBoolExpression(self, ctx: siliconParser.BoolExpressionContext):
        return SiliconValue(bool(ctx.getText()))

    # Visit a parse tree produced by siliconParser#numberExpression.
    def visitNumberExpression(self, ctx: siliconParser.NumberExpressionContext):
        val = ctx.getText()
        if '.' in val:
            return SiliconValue(float(val))
        return SiliconValue(int(val))

    # Visit a parse tree produced by siliconParser#identifierExpression.
    def visitIdentifierExpression(self, ctx: siliconParser.IdentifierExpressionContext):
        id = ctx.Identifier().getText()
        val = self.scope.resolve(id)

        if ctx.indexes():
            exps = ctx.indexes().expression()
            val = self.resolveIndexes(val, exps)

        return val

    # Visit a parse tree produced by siliconParser#notExpression.
    def visitNotExpression(self, ctx: siliconParser.NotExpressionContext):
        v = self.visit(ctx.expression())
        if not v.isBoolean():
            raise Exception(ctx)
        return SiliconValue(not v.asBoolean())

    # Visit a parse tree produced by siliconParser#orExpression.
    def visitOrExpression(self, ctx: siliconParser.OrExpressionContext):
        lhs = self.visit(ctx.expression(0))
        rhs = self.visit(ctx.expression(1))
        if not lhs.isBoolean() or not rhs.isBoolean():
            raise Exception("Invalid Type")

        raise SiliconValue(lhs.asBoolean() or rhs.asBoolean())

    # Visit a parse tree produced by siliconParser#unaryMinusExpression.
    def visitUnaryMinusExpression(self, ctx: siliconParser.UnaryMinusExpressionContext):
        v = self.visit(ctx.expression())
        if not v.isNumber():
            raise Exception("EvalException")
        return SiliconValue(-1 * v.asDouble())

    # Visit a parse tree produced by siliconParser#powerExpression.
    def visitPowerExpression(self, ctx: siliconParser.PowerExpressionContext):
        lhs = self.visit(ctx.expression(0))
        rhs = self.visit(ctx.expression(1))
        if lhs.isNumber() and rhs.isNumber():
            return SiliconValue(pow(lhs.asDouble(), rhs.asDouble()))

        raise Exception("EvalException")

    # Visit a parse tree produced by siliconParser#eqExpression.
    def visitEqExpression(self, ctx: siliconParser.EqExpressionContext):
        if ctx.op.type == siliconLexer.Equals:
            return self.eq(ctx)
        if ctx.op.type == siliconLexer.NEquals:
            return self.neq(ctx)

        raise Exception("unknown operator")

    # Visit a parse tree produced by siliconParser#andExpression.
    def visitAndExpression(self, ctx: siliconParser.AndExpressionContext):
        lhs = self.visit(ctx.expression(0))
        rhs = self.visit(ctx.expression(1))
        if not lhs.isBoolean() or not rhs.isBoolean():
            raise Exception("Invalid Type")

        raise SiliconValue(lhs.asBoolean() and rhs.asBoolean())

    # Visit a parse tree produced by siliconParser#inExpression.
    def visitInExpression(self, ctx: siliconParser.InExpressionContext):
        lhs = self.visit(ctx.expression(0))
        rhs = self.visit(ctx.expression(0))

        if rhs.isList():
            for val in rhs.asList():
                if val == lhs:
                    return SiliconValue(True)
            return SiliconValue(False)
        raise Exception("Invalid In Expression")

    # Visit a parse tree produced by siliconParser#stringExpression.
    def visitStringExpression(self, ctx: siliconParser.StringExpressionContext):
        text = ctx.getText()
        text = text[1:len(text) - 1].replace('\\\\(.)', '$1')
        val = SiliconValue(text)
        if ctx.indexes():
            exps = ctx.indexes().expression()
            val = self.resolveIndexes(val, exps)
        return val

    # Visit a parse tree produced by siliconParser#expressionExpression.
    def visitExpressionExpression(self, ctx: siliconParser.ExpressionExpressionContext):
        val = self.visit(ctx.expression())
        if ctx.indexes():
            exps = ctx.indexes().expression()
            val = self.resolveIndexes(val, exps)
        return val

    # Visit a parse tree produced by siliconParser#addExpression.
    def visitAddExpression(self, ctx: siliconParser.AddExpressionContext):
        if ctx.op.type == siliconLexer.Add:
            return self.add(ctx)
        if ctx.op.type == siliconLexer.Subtract:
            return self.subtract(ctx)
        raise Exception("unknown operator type")

    # Visit a parse tree produced by siliconParser#compExpression.
    def visitCompExpression(self, ctx: siliconParser.CompExpressionContext):
        if ctx.op.type == siliconLexer.LT:
            return self.lt(ctx)
        if ctx.op.type == siliconLexer.LTEquals:
            return self.ltEq(ctx)
        if ctx.op.type == siliconLexer.GT:
            return self.gt(ctx)
        if ctx.op.type == siliconLexer.GTEquals:
            return self.gtEq(ctx)
        return Exception("unkown operator type")

    # Visit a parse tree produced by siliconParser#nullExpression.
    def visitNullExpression(self, ctx: siliconParser.NullExpressionContext):
        return SiliconValue.NULL

    # Visit a parse tree produced by siliconParser#functionCallExpression.
    def visitFunctionCallExpression(self, ctx: siliconParser.FunctionCallExpressionContext):
        val = self.visit(ctx.functionCall())
        if ctx.indexes():
            exps = ctx.indexes().expression()
            val = self.resolveIndexes(val, exps)
        return val

    # Visit a parse tree produced by siliconParser#multExpression.
    def visitMultExpression(self, ctx: siliconParser.MultExpressionContext):
        if ctx.op.type == siliconLexer.Multiply:
            return self.multiply(ctx)
        if ctx.op.type == siliconLexer.Divide:
            return self.divide(ctx)
        if ctx.op.type == siliconLexer.Modulus:
            return self.modulus(ctx)
        raise Exception("unknown operator")

    # Visit a parse tree produced by siliconParser#listExpression.
    def visitListExpression(self, ctx: siliconParser.ListExpressionContext):
        val = self.visit(ctx.list2())
        if ctx.indexes():
            exps = ctx.indexes().expression()
            val = self.resolveIndexes(val, exps)
        return val

    # Visit a parse tree produced by siliconParser#ternaryExpression.
    def visitTernaryExpression(self, ctx: siliconParser.TernaryExpressionContext):
        condition = self.visit(ctx.expression(0))
        if condition.asBoolean():
            return SiliconValue(self.visit(ctx.expression(1)))
        else:
            return SiliconValue(self.visit(ctx.expression(2)))

    # Visit a parse tree produced by siliconParser#inputExpression.
    def visitInputExpression(self, ctx: siliconParser.InputExpressionContext):
        # REMOVE THIS - We will not be having any input
        pass

    # Visit a parse tree produced by siliconParser#list2.
    def visitList2(self, ctx: siliconParser.List2Context):
        l = list()
        if ctx.exprList():
            for ex in ctx.exprList().expression():
                l.append(self.visit(ex))

        return SiliconValue(l)

    # Visit a parse tree produced by siliconParser#indexes.
    def visitIndexes(self, ctx: siliconParser.IndexesContext):
        return self.visitChildren(ctx)

    '''
    ============================
    # OTHER OP
    ============================
    '''

    def multiply(self, ctx: siliconParser.MultExpressionContext):
        lhs = self.visit(ctx.expression(0))
        rhs = self.visit(ctx.expression(1))
        if lhs == None or rhs == None:
            print("lhs " + lhs + " rhs " + rhs)
            raise Exception("Evalexception")

        if lhs.isNumber() and rhs.isNumber():
            return SiliconValue(lhs.asDouble() * rhs.asDouble())

        if lhs.isString() and rhs.isNumber():
            return SiliconValue(lhs.asString() * int(rhs.asDouble()))  # TODO : Fix needs as a big number can cause crash

        if lhs.isList() and rhs.isNumber():
            total = []
            for i in range(int(rhs.asDouble())):
                total.append(lhs.asList())

            return SiliconValue(total)

        raise Exception(ctx)

    def divide(self, ctx: siliconParser.MultExpressionContext):
        lhs = self.visit(ctx.expression(0))
        rhs = self.visit(ctx.expression(1))

        if lhs.isNumber() and rhs.isNumber():
            return SiliconValue(lhs.asDouble() / rhs.asDouble())

        raise Exception("Eval Exception")

    def modulus(self, ctx: siliconParser.MultExpressionContext):
        lhs = self.visit(ctx.expression(0))
        rhs = self.visit(ctx.expression(1))

        if lhs.isNumber() and rhs.isNumber():
            return SiliconValue(lhs.asDouble() % rhs.asDouble())

        raise Exception("Eval Exception")

    def add(self, ctx: siliconParser.AddExpressionContext):
        lhs = self.visit(ctx.expression(0))
        rhs = self.visit(ctx.expression(1))

        if lhs == None or rhs == None:
            raise Exception("Eval Exception")

        if lhs.isNumber() and rhs.isNumber():
            return SiliconValue(lhs.asDouble() + rhs.asDouble())

        if lhs.isList():
            l = lhs.asList()
            l.append(rhs)
            return SiliconValue(l)

        if lhs.isString():
            return SiliconValue(lhs.asString() + "" + rhs.asString())

        if rhs.isString():
            return SiliconValue(lhs.asString() + "" + rhs.asString())

        return SiliconValue(lhs.asString() + rhs.asString())

    def subtract(self, ctx: siliconParser.AddExpressionContext):
        lhs = self.visit(ctx.expression(0))
        rhs = self.visit(ctx.expression(1))

        if lhs.isNumber() and rhs.isNumber():
            return SiliconValue(lhs.asDouble() - rhs.asDouble())

        if lhs.isList():
            l = lhs.asList()
            l.remove(rhs)
            return SiliconValue(l)

        raise Exception("Eval Exception")

    def gtEq(self, ctx: siliconParser.CompExpressionContext):
        lhs = self.visit(ctx.expression(0))
        rhs = self.visit(ctx.expression(1))

        if lhs.isNumber() and rhs.isNumber():
            return SiliconValue(lhs.asDouble() >= rhs.asDouble())

        if lhs.isString() or rhs.isString():
            return SiliconValue(lhs.asString() >= rhs.asString())

        raise Exception("Eval Exception")

    def ltEq(self, ctx: siliconParser.CompExpressionContext):
        lhs = self.visit(ctx.expression(0))
        rhs = self.visit(ctx.expression(1))

        if lhs.isNumber() and rhs.isNumber():
            return SiliconValue(lhs.asDouble() <= rhs.asDouble())

        if lhs.isString() or rhs.isString():
            return SiliconValue(lhs.asString() <= rhs.asString())

        raise Exception("Eval Exception")

    def gt(self, ctx: siliconParser.CompExpressionContext):
        lhs = self.visit(ctx.expression(0))
        rhs = self.visit(ctx.expression(1))

        if lhs.isNumber() and rhs.isNumber():
            return SiliconValue(lhs.asDouble() > rhs.asDouble())

        if lhs.isString() or rhs.isString():
            return SiliconValue(lhs.asString() > rhs.asString())

        raise Exception("Eval Exception")

    def lt(self, ctx: siliconParser.CompExpressionContext):
        lhs = self.visit(ctx.expression(0))
        rhs = self.visit(ctx.expression(1))

        if lhs.isNumber() and rhs.isNumber():
            return SiliconValue(lhs.asDouble() < rhs.asDouble())

        if lhs.isString() or rhs.isString():
            return SiliconValue(lhs.asString() < rhs.asString())

        raise Exception("Eval Exception")

    def eq(self, ctx: siliconParser.EqExpressionContext):
        lhs = self.visit(ctx.expression(0))
        rhs = self.visit(ctx.expression(1))

        if lhs == None:
            raise Exception("eq Exception")

        return SiliconValue(lhs == rhs)

    def neq(self, ctx: siliconParser.EqExpressionContext):
        lhs = self.visit(ctx.expression(0))
        rhs = self.visit(ctx.expression(1))

        if lhs == None:
            raise Exception("eq Exception")

        return SiliconValue(not lhs == rhs)

    def resolveIndexes(self, val, indexes):
        for ec in indexes:
            idx = self.visit(ec)
            if not idx.isNumber() or (not val.isList() and not val.isString()):
                raise Exception("resolveIndexes Exception")

            i = idx.asDouble().intValue()
            if val.isString():
                val = SiliconValue(val.asString()[i, i + 1])
            else:
                val = val.asList()[i]

        return val

    def setAtIndex(self, ctx: ParserRuleContext, indexes: list, val: SiliconValue, newVal: SiliconValue):
        if not val.isList():
            raise Exception('setAtIndex Exception'+ctx.getText())

        for i in range(len(indexes) - 1):
            idx = self.visit(indexes[i])
            if not idx.isNumber:
                raise Exception('setAtIndex Exception: Not a number'+ctx.getText())
            val = val.asList()[int(idx.asDouble())]

        idx = self.visit(indexes[len(indexes) - 1])
        if not idx.isNumber():
            raise Exception('setAtIndex Exception: Not a number '+ctx.getText())

        val.asList()[int(idx.asDouble())] = newVal