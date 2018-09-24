grammar silicon;

sourceUnit
  : (statement)* EOF ;

statement
  : assignmentStatement ;

assignmentStatement
  : identifier '=' expression ;

expression
  : number (binaryOp expression)* | identifier (binaryOp expression)* ;

binaryOp
  : '+' | '-' | '*' | '/' ;

number
  : Number ;

Number
  : Digit+ ;

fragment
IdentifierStart
  : [a-zA-Z_] ;

fragment
IdentifierPart
  : [a-zA-Z0-9_] ;

fragment
Digit
  : [0-9] ;

Identifier
  : IdentifierStart IdentifierPart* ;

identifier
  : Identifier ;