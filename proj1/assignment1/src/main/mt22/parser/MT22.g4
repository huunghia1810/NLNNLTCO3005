//Nguyen Huu Nghia; MSSV: 2033068
grammar MT22;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

program: decl_list EOF ;
decl_list: decl decl_list | decl;
decl: var_decl | fun_decl;

//var_decl
var_decl: idlist COLON varssign SM;

idlist: ID(CM idlist)*;
varssign:
    (typeint ASSIGN valintlist
    | typefloat ASSIGN valfloatlist
    | typestring ASSIGN valstringlist
    | typeboolean ASSIGN valbooleanlist
    | typ ASSIGN call_stmt);

//fun_decl
fun_decl: ID COLON FUNCTION fntype param_decl block_stmt;
param_decl: LP paramlist  RP;
paramlist: param_prime | ;
param_prime: param(CM param_prime)*;
param: param_preffix ID COLON typ;


param_preffix: (INCOMING | OUTCOMING)? ;
block_stmt: LCB (stmt | var_decl)* RCB;
//stmt: var_decl | assignstmt | call_stmt | returnstmt;
stmt
    : if_stmt
    | do_while_stmt
    | for_stmt
    | return_stmt
    | block_stmt
    | break_stmt
    | continue_stmt
    | call_stmt
    | exp SM
    ;

//-----------------------
if_stmt
    : IF LP exp RP
        stmt
    (ELSE
        stmt)?
    ;
do_while_stmt
    : DO stmt+
    WHILE exp SM
    ;
for_stmt
    : FOR LP exp SM exp SM exp RP
        stmt
    ;
break_stmt: BREAK SM;
continue_stmt: CONTINUE SM;

call_stmt: ID param_call_stmt;
param_call_stmt: LP param_call_list RP;
param_call_list: param_call_prime | ;
param_call_prime: param_call(CM param_call_prime)*;
param_call: ID | INTLIT | FLOATLIT | STRINGLIT | BOOLLIT;

return_stmt
    : RETURN SM
    | RETURN exp SM
    ;
//-----------------------
exp: exp1 ASSIGN exp | exp1;
exp1: exp1 OR exp2 | exp2;
exp2: exp2 AND exp3 | exp3;
exp3: exp4 (EQUAL | NOT_EQUAL) exp4 | exp4;
exp4: exp5 (LT | LE | GT | GE) exp5 | exp5;
exp5: exp5 (ADD | SUB) exp6 | exp6;
exp6: exp6 (DIV | MUL | MOD) exp7 | exp7;
exp7: (SUB | NOT) exp7 | exp8;
exp8: exp9 LSB exp RSB | exp9;
exp9: LP exp RP | operand;
operand
    : INTLIT
    | FLOATLIT
    | STRINGLIT
    | BOOLLIT
    | ID
    | call
    ;
call: ID LP (exp (CM exp)*)? RP;
//-----------------------
valintlist: INTLIT(CM INTLIT)*;
valfloatlist: FLOATLIT(CM FLOATLIT)*;
valstringlist: STRINGLIT(CM STRINGLIT)*;
valbooleanlist: BOOLLIT(CM BOOLLIT)*;

//-----------------------
typ: INTEGER | FLOAT | STRTYPE | BOOLTYPE;
typeint: INTEGER;
typefloat: FLOAT;
typestring: STRTYPE;
typeboolean: BOOLTYPE;
fntype: typ | VOIDTYPE;

//-----------------------
BREAK: 'break';
CONTINUE: 'continue';
ELSE: 'else';
FOR: 'for';
IF: 'if';
RETURN: 'return';
DO: 'do';
WHILE: 'while';
TRUE: 'true';
FALSE: 'false';

//-----------------------
INTEGER: 'integer'; FLOAT: 'float';
STRTYPE: 'string'; BOOLTYPE: 'boolean';
VOIDTYPE: 'void'; FUNCTION: 'function';
INCOMING: 'in' ; OUTCOMING: 'out' ;

LP: '(' ;
RP: ')' ;
LCB: '{';
RCB: '}';
LSB: '[';
RSB: ']';
CM : ',';
COLON : ':';
SM: ';';

ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';
MOD: '%';
NOT: '!';
OR: '||';
AND: '&&';
NOT_EQUAL: '!=';
EQUAL: '==';
LT: '<';
GT: '>';
LE: '<=';
GE: '>=';
ASSIGN: '=';

INTLIT: [0-9_]+ {self.text = self.text.replace('_','')};
FLOATLIT: [0-9_]+ '.' [0-9_]+ {self.text = self.text.replace("_", "" )};
BOOLLIT: TRUE | FALSE;
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