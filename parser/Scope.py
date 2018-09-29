class Scope:

    def __init__(self, p=None):
        self._parent = p
        self._variables = dict()

    @property
    def parent(self):
        return self._parent

    @property
    def variables(self):
        return self._variables

    def assignParam(self, var, value):
        self.variables[var] = value

    def assign(self, var, value):
        if self.resolve(var) != None:  # noqa
            self.reAssign(var, value)
        else:
            self.variables[var] = value

    def isGlobalScope(self):
        return self.parent == None

    def reAssign(self, identifier: str, value):
        if identifier in self.variables:
            self.variables[identifier] = value
        elif self.parent:
            self.parent.reAssign(identifier, value)

    def resolve(self, var):
        value = self.variables.get(var)
        if value != None:
            return value

        elif not self.isGlobalScope():
            return self.parent.resolve(var)

        else:
            return None

    def __str__(self):
        result = ""
        for key, value in self.variables.items():
            result += key + "->" + value
        return result
