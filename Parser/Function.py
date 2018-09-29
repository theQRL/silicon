from Parser.AST.Visitor import Visitor
from Parser.Scope import Scope
from Parser.SiliconValue import SiliconValue
from Parser.ReturnValue import ReturnValue


class Function:
    def __init__(self, params, block):
        self._params = params
        self._block = block

    @property
    def params(self):
        return self._params

    @property
    def block(self):
        return self._block

    def invoke(self, params: list, functions, scope):
        if len(params) != len(self.params):
            raise Exception("Runtime exception")

        scope = Scope(scope)
        visitor = Visitor(scope, functions)

        for i in range(len(self.params)):
            value = visitor.visit(params[i])
            scope.assignParam(self.params[i].getText(), value)

        ret = SiliconValue.VOID

        try:
            visitor.visit(self.block)
        except Exception:
            ret = ReturnValue().value

        return ret
