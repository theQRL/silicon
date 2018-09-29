lexer grammar siliconLexer;

Println     : 'println';
Print       : 'print';
Input       : 'input';
Def         : 'def';
If          : 'if';
Else        : 'else';
Return      : 'return';
For         : 'for';
While       : 'while';
To          : 'to';
Do          : 'do';
End         : 'end';
In          : 'in';
Null        : 'null';

Or          : '||';
And         : '&&';
Equals      : '==';
NEquals     : '!=';
GTEquals    : '>=';
LTEquals    : '<=';
Pow         : '^';
Excl        : '!';
GT          : '>';
LT          : '<';
Add         : '+';
Subtract    : '-';
Multiply    : '*';
Divide      : '/';
Modulus     : '%';
OBrace      : '{';
CBrace      : '}';
OBracket    : '[';
CBracket    : ']';
OParen      : '(';
CParen      : ')';
SColon      : ';';
Assign      : '=';
Comma       : ',';
QMark       : '?';
Colon       : ':';

Bool
 : 'true'
 | 'false'
 ;

Number
 : Int ( '.' Digit* )?
 ;

Identifier
 : [a-zA-Z_] [a-zA-Z_0-9]*
 ;

String
 : ["] ( ~["\r\n\\] | '\\' ~[\r\n] )* ["]
 | ['] ( ~['\r\n\\] | '\\' ~[\r\n] )* [']
 ;

Comment
 : ( '//' ~[\r\n]* | '/*' .*? '*/' ) -> skip
 ;

Space
 : [ \t\r\n\u000C] -> skip
 ;

fragment Int
 : [1-9] Digit*
 | '0'
 ;

fragment Digit
 : [0-9]
 ;