//Nguyen Huu Nghia, MSSV: 2033068
grammar MT22;

@lexer::header {
    from lexererr import *
}
@members{}
options{
	language=Python3;        
}
program: decllist EOF;

decllist: decl decllist | decl;

decl: vardecl | funcdecl;

// ------------------ 5.1 var_decl ------------------
vardecl: varnoinit | varassign | array;

varnoinit: idlist COLON vartype SM;

varassign:
    l=idlist COLON vartype ASSIGN r=expprime e=SM
    {if len($l.text.split(',')) != len($r.text.split(',')):
        raise Exception('Error on line {} col {}: ;'.format($e.line, $e.pos))
    };
vartype: INTEGER | FLOAT | BOOLEAN | STRING | AUTO;

atomic_type : INTEGER | FLOAT | BOOLEAN | STRING;

idlist: ID CM idlist | ID ;

// ------------------ 5.3 func_decl ------------------
funcdecl: base_funcdecl (PARAM_KEYWORDS ID| ) blockstmt;
base_funcdecl: ID COLON FUNCTION returntype LP paramlist RP;
returntype: atomic_type | VOID | AUTO | arrayParam;

paramlist: paramprime | ; 
paramprime: param CM paramprime | param;
param: (paramHead | ) parambase;
paramHead: PARAM_KEYWORDS (PARAM_KEYWORDS|);
parambase: ID COLON paramtype; 
paramtype: atomic_type | AUTO | arrayParam;
blocklist: allowed_blockstmt blocklist | ;

// ------------------ 4.2 array_decl ------------------
array: arraydecl | arrayinit;
arraydecl: idlist COLON arrayParam SM;
arrayinit: idlist COLON arrayParam ASSIGN arraylit SM;

arraylit: expprime | arrayValList;
arrayValList: arrayVal CM arrayValList | arrayVal;
arrayVal: LCB exprlist RCB;
arrayParam: ARRAY LSB dimension RSB OF atomic_type;
dimension: INTLIT CM dimension | INTLIT;

// ------------------ 7 statement: stmt ------------------
stmt
    : assignstmt
    | ifstmt
    | returnstmt
    | callstmt
    | forstmt
    | whilestmt
    | dowhile_stmt
    | continuestmt
    | breakstmt
    | blockstmt
    ;

allowed_blockstmt: stmt | vardecl;

assignstmt: scalar_variable ASSIGN expr SM;

ifstmt: IF LP expr RP loopstmt (ELSE loopstmt | );

forstmt: FOR LP scalar_variable ASSIGN expr CM expr CM expr RP loopstmt;

whilestmt: WHILE LP expr RP loopstmt;

dowhile_stmt: DO blockstmt WHILE LP expr RP SM;

returnstmt: RETURN (expr | ) SM;

callstmt: ID LP exprlist RP SM;
continuestmt: CONTINUE SM;
breakstmt: BREAK SM;
blockstmt: LCB blocklist RCB;  
loopstmt: blockstmt | stmt;

scalar_variable: ID |  indexop; 

exprlist: expprime | ;
expprime: expr CM expprime | expr;
expr: expr1 SRO expr1 | expr1;
expr1: expr2 COMPARE expr2 | expr2;
expr2: expr2 AND_OR expr3 | expr3;
expr3: expr3 (ADD | SUB) expr4 | expr4;
expr4: expr4 MOD_MUL_DIV expr5 | expr5;
expr5: NOT expr5 | expr6; 
expr6: SUB expr6 | expr7;
expr7: BOOLLIT | INTLIT | STRINGLIT | FLOATLIT | ID | callexpr | subexpr | indexop; 
callexpr: ID LP exprlist RP;
subexpr: LP expr RP;
indexop: ID LSB expprime RSB;

PARAM_KEYWORDS: INHERIT | OUT;
BOOLLIT: TRUE | FALSE;
FLOATLIT: (INTLIT DECPART | INTLIT DECPART EXPPART | INTLIT EXPPART | DECPART EXPPART? | INTLIT DOT | DOT EXPPART) {self.text = self.text.replace('_', '')};
INTLIT: '0' | [1-9] ('_'?[0-9])* {self.text = self.text.replace('_', '')};
STRINGLIT: DOUBLEQ (StringChar*) DOUBLEQ
    {
        result = str(self.text)
        self.text = result[1:-1]
    };

fragment EXPPART: [eE] [-+]? [0-9]+;
fragment DOT: '.';
fragment DECPART: DOT [0-9]+;
fragment StringChar: ~[\b\f\r\n\t"\\] | ESC2;
fragment ESC2: '\\' [bfrnt"\\];
fragment DOUBLEQ : '"';
fragment IllegalString
    : '\\' ~[bfrnt"\\]
    | '\\'
    ;

// ------------------ 3.6 Seperators ------------------
LP:         '(';
RP:         ')';
LSB:        '[';
RSB:        ']';
//DOT:        '.';
CM:         ',';
SM:         ';';
COLON:      ':';
LCB:        '{';
RCB:        '}';
ASSIGN:     '=';

// ------------------ 3.5 Operators ------------------
MOD_MUL_DIV: MOD | MUL | DIV;
AND_OR: LG_AND | LG_OR;
COMPARE: EQ | INEQ | GT | GE | LT | LE;

ADD:            '+';
SUB:            '-';
MUL:            '*';
DIV:            '/';
MOD:            '%';
NOT:            '!';
LG_AND:         '&&';
LG_OR:           '||';
EQ:             '==';
INEQ:           '!='; //inequality
LT:             '<';
GT:             '>';
LE:             '<=';
GE:             '>=';
SRO:            '::'; //scope resolution operator

// ------------------ 3.4 Keywords ------------------
AUTO:           'auto';
BREAK:          'break';
BOOLEAN:        'boolean';
DO:             'do';
ELSE:           'else';
FALSE:          'false';
FLOAT:          'float';
FOR:            'for';
FUNCTION:       'function';
IF:             'if';
INTEGER:        'integer';
INT:            'int'; //
RETURN:         'return';
STRING:         'string';
TRUE:           'true';
WHILE:          'while';
VOID:           'void';
IN:             'in';
OUT:            'out';
CONTINUE:       'continue';
OF:             'of';
INHERIT:        'inherit';
ARRAY:          'array';

// ------------------ comments ------------------
COMMENT: '//' ~[\r\n]* -> skip;
C_COMMENT: '/*' .*? '*/' -> skip;

// ------------------ 3.3 ID ------------------
ID
    :   [a-zA-Z_] [a-zA-Z_0-9]*
    ;

// ------------------ 3.1 ------------------
WS : [ \t\r\n]+ -> skip ;

UNCLOSE_STRING: DOUBLEQ StringChar* ([\b\t\f\n\r"\\] | EOF)
    {
        unclose_str = str(self.text)
        possible = ['\b', '\t', '\f', '\n', '\r', '"', '\\']
        if unclose_str[-1] in possible:
            raise UncloseString(unclose_str[1:-1])
        else:
            raise UncloseString(unclose_str[1:])
    }
    ;
ILLEGAL_ESCAPE:DOUBLEQ StringChar* IllegalString
    {
        illegal_str = str(self.text)
        raise IllegalEscape(illegal_str[1:])
    }
    ;   
ERROR_CHAR: .
    {
        raise ErrorToken(self.text)
    }
    ;
