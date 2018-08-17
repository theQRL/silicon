from collections import namedtuple

from enum import Enum


T = namedtuple('T', 'token name precedence')


class Tokens(Enum):
    EOS = 0

    # Punctuators
    LParen = 1
    RParen = 2
    LBrack = 3
    RBrack = 4
    LBrace = 5
    RBrace = 6
    Colon = 7
    Semicolon = 8
    Period = 9
    Conditional = 10

    # Assignment Operators
    Assign = 11

    # Binary Operators
    AssignBitOr = 12
    AssignBitXor = 13
    AssignBitAnd = 14
    AssignShl = 15
    AssignSar = 16
    AssignShr = 17
    AssignAdd = 18
    AssignSub = 19
    AssignMul = 20
    AssignDiv = 21
    AssignMod = 22

    # Binary Operators
    Comma = 23
    Or = 24
    And = 25
    BitOr = 26
    BitXor = 27
    BitAnd = 28
    SHL = 29
    SAR = 30
    SHR = 31
    Add = 32
    Sub = 33
    Mul = 34
    Div = 35
    Mod = 36
    Exp = 37

    # Comparators
    Equal = 38
    NotEqual = 39
    LessThan = 40
    GreaterThan = 41
    LessThanOrEqual = 42
    GreaterThanOrEqual = 43

    # Unary Operators
    Not = 44
    BitNot = 45
    Inc = 46
    Dec = 47

    # Keywords
    While = 48
    Do = 49
    For = 50
    Break = 51
    Continue = 52
    If = 53
    Else = 54
    Return = 55
    Try = 56
    Catch = 57
    Throw = 58

    # Data type
    Int = 59
    Float = 60
    Bool = 61
    String = 62

    # Literals
    TrueLiteral = 63
    FalseLiteral = 64
    Number = 65
    StringLiteral = 66
    CommentLiteral = 67

    Identifier = 68

    Invalid = 69

    Whitespace = 70


keywords = {
    "while": Tokens.While,
    "do": Tokens.Do,
    "for": Tokens.For,
    "break": Tokens.Break,
    "continue": Tokens.Continue,
    "if": Tokens.If,
    "else": Tokens.Else,
    "return": Tokens.Return,
    "try": Tokens.Try,
    "catch": Tokens.Catch,
    "throw": Tokens.Throw,

    # Data type
    "int": Tokens.Int,
    "float": Tokens.Float,
    "bool": Tokens.Bool,
    "string": Tokens.String,
}

tokens_info = {
    Tokens.EOS: T(Tokens.EOS, 'EOS', 0),

    Tokens.LParen: T(Tokens.LParen, '(', 0),
    Tokens.RParen: T(Tokens.RParen, ')', 0),
    Tokens.LBrack: T(Tokens.LBrack, '[', 0),
    Tokens.RBrack: T(Tokens.RBrack, ']', 0),
    Tokens.LBrace: T(Tokens.LBrace, '{', 0),
    Tokens.RBrace: T(Tokens.RBrace, '}', 0),
    Tokens.Colon: T(Tokens.Colon, ':', 0),
    Tokens.Semicolon: T(Tokens.Semicolon, ';', 0),
    Tokens.Period: T(Tokens.Period, '.', 0),
    Tokens.Conditional: T(Tokens.Conditional, '?', 3),

    Tokens.Assign: T(Tokens.Assign, '=', 2),

    Tokens.AssignBitOr: T(Tokens.AssignBitOr, '|=', 2),
    Tokens.AssignBitXor: T(Tokens.AssignBitXor, '^=', 2),
    Tokens.AssignBitAnd: T(Tokens.AssignBitAnd, '&=', 2),
    Tokens.AssignShl: T(Tokens.AssignShl, '<<=', 2),
    Tokens.AssignSar: T(Tokens.AssignSar, '>>=', 2),
    Tokens.AssignShr: T(Tokens.AssignShr, '>>>=', 2),
    Tokens.AssignAdd: T(Tokens.AssignAdd, '+=', 2),
    Tokens.AssignSub: T(Tokens.AssignSub, '-=', 2),
    Tokens.AssignMul: T(Tokens.AssignMul, '*=', 2),
    Tokens.AssignDiv: T(Tokens.AssignDiv, '/=', 2),
    Tokens.AssignMod: T(Tokens.AssignMod, '%=', 2),

    Tokens.Comma: T(Tokens.Comma, ',', 1),
    Tokens.Or: T(Tokens.Or, '||', 4),
    Tokens.And: T(Tokens.And, '&&', 5),
    Tokens.BitOr: T(Tokens.BitOr, '|', 8),
    Tokens.BitXor: T(Tokens.BitXor, '^', 9),
    Tokens.BitAnd: T(Tokens.BitAnd, '&', 10),
    Tokens.SHL: T(Tokens.SHL, '<<', 11),
    Tokens.SAR: T(Tokens.SAR, '>>', 11),
    Tokens.SHR: T(Tokens.SHR, '>>>', 11),
    Tokens.Add: T(Tokens.Add, '+', 12),
    Tokens.Sub: T(Tokens.Sub, '-', 12),
    Tokens.Mul: T(Tokens.Mul, '*', 13),
    Tokens.Div: T(Tokens.Div, '/', 13),
    Tokens.Mod: T(Tokens.Mod, '%', 13),
    Tokens.Exp: T(Tokens.Exp, '**', 14),

    Tokens.Equal: T(Tokens.Equal, '==', 6),
    Tokens.NotEqual: T(Tokens.NotEqual, '!=', 6),
    Tokens.LessThan: T(Tokens.LessThan, '<', 7),
    Tokens.GreaterThan: T(Tokens.GreaterThan, '>', 7),
    Tokens.LessThanOrEqual: T(Tokens.LessThanOrEqual, '<=', 7),
    Tokens.GreaterThanOrEqual: T(Tokens.GreaterThanOrEqual, '>=', 7),

    Tokens.Not: T(Tokens.Not, '!', 0),
    Tokens.BitNot: T(Tokens.BitNot, '~', 0),
    Tokens.Inc: T(Tokens.Inc, '++', 0),
    Tokens.Dec: T(Tokens.Dec, '--', 0),

    Tokens.While: T(Tokens.While, 'while', 0),
    Tokens.Do: T(Tokens.Do, 'do', 0),
    Tokens.For: T(Tokens.For, 'for', 0),
    Tokens.Break: T(Tokens.Break, 'break', 0),
    Tokens.Continue: T(Tokens.Continue, 'continue', 0),
    Tokens.If: T(Tokens.If, 'if', 0),
    Tokens.Else: T(Tokens.Else, 'else', 0),
    Tokens.Return: T(Tokens.Return, 'return', 0),
    Tokens.Try: T(Tokens.Try, 'try', 0),
    Tokens.Catch: T(Tokens.Catch, 'catch', 0),
    Tokens.Throw: T(Tokens.Throw, 'throw', 0),

    Tokens.Int: T(Tokens.Int, 'int', 0),
    Tokens.Float: T(Tokens.Float, 'float', 0),
    Tokens.Bool: T(Tokens.Bool, 'bool', 0),
    Tokens.String: T(Tokens.String, 'string', 0),

    Tokens.TrueLiteral: T(Tokens.TrueLiteral, 'true', 0),
    Tokens.FalseLiteral: T(Tokens.FalseLiteral, 'false', 0),
    Tokens.Number: T(Tokens.Number, None, 0),
    Tokens.StringLiteral: T(Tokens.StringLiteral, None, 0),
    Tokens.CommentLiteral: T(Tokens.CommentLiteral, None, 0),

    Tokens.Identifier: T(Tokens.Identifier, None, 0),

    Tokens.Invalid: T(Tokens.Invalid, 'Invalid', 0),

    Tokens.Whitespace: T(Tokens.Whitespace, None, 0),
}


def get_token(token: Tokens):
    return tokens_info[token]
