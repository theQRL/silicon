import antlr4

from gen.siliconLexer import siliconLexer
from gen.siliconParser import siliconParser

from parser.Scope import Scope
from parser.ast.Visitor import Visitor
from parser.SymbolVisitor import SymbolVisitor


code = antlr4.FileStream("sample.sil")
lexer = siliconLexer(code)
stream = antlr4.CommonTokenStream(lexer)
parser = siliconParser(stream)

tree = parser.sourceUnit()
scope = Scope()
functions = dict()
symbolVisitor = SymbolVisitor(functions)
symbolVisitor.visit(tree)
visitor = Visitor(scope, functions)
visitor.visit(tree)
