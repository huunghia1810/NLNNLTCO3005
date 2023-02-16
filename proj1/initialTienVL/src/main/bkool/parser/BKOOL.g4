grammar BKOOL;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

program  : (vardecl)+ EOF ;

vardecl: VARNAME EQ expr SEMI;

expr: expr1 DQUES expr1 | expr1;
expr1: expr2 (ADD | SUB) expr1 | expr2;
expr2: expr2 (MUL | DIV | MOD) expr3 | expr3;
expr3: expr3 DOT expr4 | expr4;
expr4: expr5 DSTAR expr4 | expr5;
expr5: VARNAME | INTLIT | FLOATLIT | STRINGLIT | arrdecl | subexpr;

subexpr: LB expr RB;

arrdecl: (idxarr | assarr)+;

idxarr: 'array' LB exprlist RB;
exprlist: (expr(COMMA exprlist)*)? ;

assarr: 'array' LB asspairdecl RB;
asspairdecl: (asspair(COMMA asspairdecl)*)? ;
asspair: PAIRNAME ARROW expr;


DSTAR: '**';
DOT: '.';
ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';
MOD: '%';
DQUES: '??';
ARROW: '=>';
COMMA: ',';
LB: '(';
RB: ')';
SEMI: ';';
EQ: '=';
INTLIT: [0-9]+;
STRINGLIT: [a-zA-Z]+;
FLOATLIT: [0-9]+ '.' [0-9]+;
ID: [a-zA-Z]+;
VARNAME: [a-z]+;
PAIRNAME: [a-zA-Z0-9]+;

WS: [ \t\r\n] -> skip;

ERROR_CHAR: . {raise ErrorToken(self.text)};

UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;