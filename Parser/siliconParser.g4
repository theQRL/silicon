parser grammar siliconParser;

options { tokenVocab=siliconLexer; }

sourceUnit
  : (statement)* EOF;

statement
  : assignmentStatement ;

assignmentStatement
  : identifier AssignmentOp expression ;

expression
  : number (BinaryOp expression)* | identifier (BinaryOp expression)* ;

number
  : Number ;

identifier
  : Identifier ;
