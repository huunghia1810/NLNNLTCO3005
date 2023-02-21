//Nguyen Huu Nghia; MSSV: 2033068
grammar MT22;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

program: decllist EOF ;
decllist: decl decllist | decl;
decl: vardecl | fundecl;

//vardecl
vardecl: idlist COLON (typeint EQ valintlist | typefloat EQ valfloatlist) SEMI;
idlist: ID(COMMA idlist)*;

//fundecl
fundecl: ID COLON 'function' fntype paramdecl body;
paramdecl: LB paramlist  RB;
paramlist: paramprime | ;
paramprime: param COMMA paramprime | param;
param: ID COLON typ;


body: LP stmtlist RP;
stmtlist: stmt stmtlist | ;
//stmt: vardecl | assignstmt | callstmt | returnstmt;
stmt: vardecl;



//-----------------------
valintlist: INTLIT(COMMA INTLIT)*;
valfloatlist: FLOATLIT(COMMA FLOATLIT)*;

//-----------------------
typ: INTEGER | FLOAT;
typeint: INTEGER;
typefloat: FLOAT;
fntype: typ | 'void';
//-----------------------
INTEGER: 'integer'; FLOAT: 'float';
AND : 'and' ;
OR : 'or' ;
NOT : 'not' ;
EQ : '=' ;
LB: '(';
RB: ')';
LP: '{';
RP: '}';
COMMA : ',';
COLON : ':';
SEMI: ';';
INTLIT: [0-9_]+ {self.text = self.text.replace('_','')};
FLOATLIT: [0-9_]+ '.' [0-9_]+ {self.text = self.text.replace("_", "" )};
STRINGLIT: '"' ( ~('\\') | '\\' (~('\\'))* '\\' )* '"'
    {
        result = str(self.text)
        self.text = result[1:-1]
    };

//STRINGLIT: '"' Schar* '"';
//fragment Schar: ~ [\\\r\n] | EscapeSequence;
//fragment EscapeSequence : '\\b' | '\\f' | '\\r' | '\\n' | '\\t' | '\\\'' | '\\\\' | '\\"' ;

ID: [a-zA-Z]+;

//COMMENT : '#' ~[\r\n]* '\r'? '\n' -> skip ;
WS : [ \t\r\n\f]+ -> skip ; // skip spaces, tabs, newlines

ERROR_CHAR: . {raise ErrorToken(self.text)};
UNCLOSE_STRING: . {raise UncloseString(self.text)};
ILLEGAL_ESCAPE: . {raise IllegalEscape(self.text)};