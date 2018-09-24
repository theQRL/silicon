import antlr4
from gen.siliconLexer import siliconLexer
from gen.siliconParser import siliconParser


input = antlr4.FileStream("sample.sil")
lexer = siliconLexer(input)
stream = antlr4.CommonTokenStream(lexer)
parser = siliconParser(stream)


class siliconListener(antlr4.ParseTreeListener):

    def enterKey(self, ctx):
        pass

    def exitKey(self, ctx):
        pass

    def enterValue(self, ctx):
        pass

    def exitValue(self, ctx):
        pass


class KeyPrinter(siliconListener):
    def exitKey(self, ctx):
        print("Oh, a key!")


tree = parser.sourceUnit()
printer = KeyPrinter()
walker = antlr4.ParseTreeWalker()
walker.walk(printer, tree)
