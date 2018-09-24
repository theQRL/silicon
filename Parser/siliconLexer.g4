lexer grammar siliconLexer;

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

BinaryOp
  : '+' | '-' | '*' | '/' ;

AssignmentOp
  : '=' ;

WS
  : [ \t\r\n\u000C]+ -> skip ;
