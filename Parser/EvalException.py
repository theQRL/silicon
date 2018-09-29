from antlr4.ParserRuleContext import ParserRuleContext


class EvalException:

    def __init__(self, ctx: ParserRuleContext):
        self.evalException("Illegal expression: " + ctx.getText(), ctx)

    def evalException(self, msg: str, ctx: ParserRuleContext):
        raise Exception(msg + " line: " + ctx.start.getLine())
