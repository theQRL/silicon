parser grammar siliconParser;

/*
TODO:
    1. Add access specifier such as public, private, protected
    2. Add Datatypes
    3. Add modifiers such as static
    4. Change Print and Println to something that could only be used for debugging
*/

options { tokenVocab=siliconLexer; }

sourceUnit
  : block EOF
  ;

block
  : ( statement | functionDecl )* ( Return expression )?
  ;

statement
  : assignmentStatement
  | functionCall
  | ifStatement
  | forStatement
  | whileStatement
  ;

assignmentStatement
  : Identifier indexes? '=' expression
  ;

functionCall
  : Identifier '(' exprList? ')' # identifierFunctionCall
  | Println '(' expression? ')'  # printlnFunctionCall
  | Print '(' expression? ')'    # printFunctionCall
  ;

ifStatement
  : ifStat elseIfStat* elseStat? ;

ifStat
  : If '(' expression ')' '{' block '}'
  ;

elseIfStat
  : Else If '(' expression ')' '{' block '}'
  ;

elseStat
  : Else '{' block '}'
  ;

functionDecl
  : Def Identifier '(' idList? ')' '{' block '}'
  ;


forStatement
  : For '(' assignmentStatement? ';' expression? ';' assignmentStatement? ')' '{' block '}'
  /*
    TODO:
        1. Add support for multiple initialization statement
  */
  ;

whileStatement
  : While expression '{' block '}'
  ;

idList
  : Identifier ( ',' Identifier )*
  ;

exprList
  : expression ( ',' expression )*
  ;

expression
  : '-' expression                                           #unaryMinusExpression
  | '!' expression                                           #notExpression
  | <assoc=right> expression '^' expression                  #powerExpression
  | expression op=( '*' | '/' | '%' ) expression             #multExpression
  | expression op=( '+' | '-' ) expression                   #addExpression
  | expression op=( '>=' | '<=' | '>' | '<' ) expression     #compExpression
  | expression op=( '==' | '!=' ) expression                 #eqExpression
  | expression '&&' expression                               #andExpression
  | expression '||' expression                               #orExpression
  | expression '?' expression ':' expression                 #ternaryExpression
  | expression In expression                                 #inExpression
  | Number                                                   #numberExpression
  | Bool                                                     #boolExpression
  | Null                                                     #nullExpression
  | functionCall indexes?                                    #functionCallExpression
  | list2 indexes?                                           #listExpression
  | Identifier indexes?                                      #identifierExpression
  | String indexes?                                          #stringExpression
  | '(' expression ')' indexes?                              #expressionExpression
  | Input '(' String ')'                                     #inputExpression
  ;

list2
  : '[' exprList? ']'
  ;

indexes
  : ( '[' expression ']' )+
  ;
