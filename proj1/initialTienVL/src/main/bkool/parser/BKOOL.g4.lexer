grammar BKOOL;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

program  : mptype 'main' LB RB LP body? RP EOF ;

mptype: INTTYPE | VOIDTYPE ;

body: funcall SEMI;

exp: funcall | INTLIT ;

funcall: ID LB exp? RB ;

INTTYPE: 'int' ;

VOIDTYPE: 'void'  ;

//Lexer - question 1
//ID: [a-z] [a-z0-9]*;

//Lexer - question 2
//ID: [0-9]+ ('.' [0-9]+ EXPONENT? | EXPONENT);
//fragment EXPONENT: [Ee] [+-]? [0-9]+ ;

//Lexer - question 3
ID: '\'' ( ~('\'') | '\'' (~('\''))* '\'' )* '\'';

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines

ERROR_CHAR: . {raise ErrorToken(self.text)};
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;