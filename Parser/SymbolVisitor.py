from gen.siliconParser import siliconParser
from gen.siliconParserVisitor import siliconParserVisitor
from Parser.Function import Function
from Parser.SiliconValue import SiliconValue


class SymbolVisitor(siliconParserVisitor):

    def __init__(self, functions: dict):
        self._functions = functions

    @property
    def functions(self):
        return self._functions

    def visitFunctionDecl(self, ctx: siliconParser.FunctionDeclContext):
        if ctx.idList() != None:
            params = ctx.idList().Identifier()
        else:
            params = list()

        block = ctx.block()
        id = ctx.Identifier().getText() + str(len(params))
        self._functions[id] = Function(params, block)

        return SiliconValue.VOID
