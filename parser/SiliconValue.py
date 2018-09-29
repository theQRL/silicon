class PreDefinedConstants:
    def __init__(self, value):
        self.constants = ["NULL", "VOID"]
        self.value = value

    def __eq__(self, value):
        if self.value == value:
            return True

        return False


class SiliconValue:
    NULL = None
    VOID = None

    def __init__(self, v=None):
        if v == None:
            raise Exception("Runtime Exception")

        self.value = v

        if not (self.isBoolean() or self.isList() or self.isNumber() or self.isString()):
            raise Exception("Runtime Exception invalid data type")

        self.NULL = PreDefinedConstants("NULL")
        self.VOID = PreDefinedConstants("VOID")

    def asBoolean(self):
        return bool(self.value)

    def asDouble(self):
        return float(self.value)

    def asLong(self):
        return int(self.value)

    def asList(self):
        return list(self.value)

    def asString(self):
        return str(self.value)

    def __eq__(self, o: object):
        if self.value == "VOID" or (isinstance(o, PreDefinedConstants) and o.value == "VOID"):
            raise Exception("Runtime exception")

        if self.value == o:
            return True

        if o == None or self.value != o:
            return False

        that = SiliconValue(o)
        if self.isNumber() and that.isNumber():
            diff = abs(self.asDouble() - that.asDouble())
            return diff < 0.00000000001  # Todo : needs testing
        else:
            return self.value == that.value

    def isBoolean(self):
        return isinstance(self.value, bool)

    def isNumber(self):
        return isinstance(self.value, int) or isinstance(self.value, float)

    def isList(self):
        return isinstance(self.value, list)

    def isNull(self):
        return self.value == self.NULL

    def isVoid(self):
        return self.value == self.VOID

    def isString(self):
        return isinstance(self.value, str)

    def __str__(self):
        if self.isNull():
            return "NULL"
        elif self.isVoid():
            return "VOID"
        else:
            return str(self.value)
