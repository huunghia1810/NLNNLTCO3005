//Nguyen Huu Nghia, MSSV: 2033068
grammar MT22;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

program: (var_decl | func_decl | func_main)* EOF;

// ------------------ func_main ------------------
func_main: MAIN COLON FUNCTION VoidType LP RP main_return;

main_return: LCB (stmt|var_decl)* RCB;

// ------------------ 7 statement: stmt ------------------
stmt
    :   assign_stmt
    |   if_stmt
    |   while_stmt
    |   do_while_stmt
    |   for_stmt
    |   break_stmt
    |   continue_stmt
    |   call_stmt
    |   block_stmt
    |   return_stmt
    ;

assign_stmt: lhs ASSIGN expr SM;
lhs: ID | index_expr;

if_stmt: IF LP expr RP stmt (ELSE stmt)?;

while_stmt: WHILE LP expr RP stmt;

do_while_stmt: DO block_stmt WHILE LP expr RP SM;

for_stmt: FOR LP ID ASSIGN expr CM expr CM expr RP stmt;

break_stmt: BREAK SM;

continue_stmt: CONTINUE SM;

call_stmt: func_call SM;

block_stmt: LCB (stmt | var_decl)* RCB;

return_stmt: RETURN expr? SM;

// ------------------ 5.1 var_decl ------------------
var_decl
    : l=id_lst COLON valid_type ASSIGN r=expr_lst e=SM
    {if len($l.text.split(',')) != len($r.text.split(',')):
        raise Exception('Error on line {} col {}: ;'.format($e.line, $e.pos))
    }
    | id_lst COLON atomic_type SM
    | id_lst COLON array_decl SM //?
    ;

id_lst: ID (CM ID)*;

valid_type: atomic_type | AutoType;

// ------------------ 5.2 para_decl ------------------
para_lst_decl: para_decl (CM para_decl)*;

para_decl: INHERIT? OUT?
    (ID COLON atomic_type | ID COLON array_decl); //?

// ------------------ 5.3 func_decl ------------------
func_decl: func_prototype func_body;

func_prototype
    :   ID COLON FUNCTION func_return_type LP para_lst_decl* RP (INHERIT ID)? //? para_lst_decl*
    ;

func_return_type
    :   atomic_type
    |   VoidType
    |   AutoType
    ;

func_body: LCB (stmt|var_decl)* RCB;

// ------------------ 6.6 func_call ------------------
func_call: ID LP arg_lst? RP;

arg_lst: expr (CM expr)*;
expr: relation_expr (SRO relation_expr)?;
relation_expr: logic_expr (relation_op logic_expr)?;

relation_op: EQ | INEQ | LT | GT | LE | GE;

logic_expr
    :   logic_expr logic_op adding_expr
    |   adding_expr
    ;

logic_op: LG_AND | LG_OR;

adding_expr
    :   adding_expr adding_op multiplying_expr
    |   multiplying_expr
    ;

adding_op: ADD | SUB;

multiplying_expr
    :   multiplying_expr multiplying_op unary_logic_expr
    |   unary_logic_expr
    ;

multiplying_op: MUL | DIV | MOD;

unary_logic_expr
    :   unary_logic_op (unary_logic_expr | sign_expr)
    |   sign_expr
    ;

unary_logic_op: NOT;

sign_expr
    :   sign_op (index_expr | sign_expr)
    |   index_expr
    ;

sign_op: SUB;

index_expr
    :   ID LSB expr_lst RSB
    |   ID
    |   BOOLLIT
    |   INTLIT
    |   FLOATLIT
    |   STRINGLIT
    |   arrayLIT
    |   func_call
    //
    ;

expr_lst: expr (CM expr)*;

// ------------------ 4.2 array_decl ------------------
array_decl: ArrayType LSB integer_lst RSB OF atomic_type;

integer_lst: INTLIT (CM INTLIT)*;

atomic_type
    :   BooleanType
    |   IntegerType
    |   FloatType
    |   StringType
    ;

// ------------------ 4. Type: String | Integer | Float | Boolean | Array | Void | Auto ------------------
StringType: STRING;
IntegerType: INTEGER;
FloatType: FLOAT;
BooleanType: BOOLEAN;
ArrayType: ARRAY;
VoidType: VOID;
AutoType: AUTO;

// ------------------ 3.7 Literals: INTLIT | FLOATLIT | BOOLLIT | STRINGLIT | arrayLIT ------------------
arrayLIT: LCB expr_lst RCB;

INTLIT
    :   NonZeroDigit ('_'Digit | Digit)* {self.text = self.text.replace('_', '')}
    |   '0'
    ;

FLOATLIT
    :   INTLIT DecimalPart ExponentPart? {self.text = self.text.replace('_', '')}
    |   INTLIT ExponentPart
    |   DecimalPart ExponentPart
    ;
fragment        DecimalPart: '.' Digit* ;
fragment        ExponentPart: [eE] ('-' | '+')? Digit+ ;
fragment        Digit: [0-9];
fragment        NonZeroDigit: [1-9];

BOOLLIT : TRUE | FALSE;

STRINGLIT:  '"' Schar* '"' {self.text = self.text[1:-1]};
fragment Schar:
	~ ["\\]
	| EscapeSequence
    ;
fragment EscapeSequence:
    '\\b'
    |   '\\f'
    |   '\\r'
    |   '\\n'
    |   '\\t'
    |   '\\\''
    |   '\\\\'
    |   '\\"'
    ;

// ------------------ 3.6 Seperators ------------------
LP:         '(';
RP:         ')';
LSB:        '[';
RSB:        ']';
DOT:        '.';
CM:         ',';
SM:         ';';
COLON:      ':';
LCB:        '{';
RCB:        '}';
ASSIGN:     '=';

// ------------------ 3.5 Operators ------------------
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
MAIN:           'main';
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

// ------------------ 3.3 ID ------------------
ID
    :   [a-zA-Z_] [a-zA-Z_0-9]*
    ;

// ------------------ 3.2 Comment ------------------
BlockComment
    :   '/*' .*? '*/' //non-greedy
        -> skip
    ;
//BlockMissComment: '/*' ~['*/'] {raise UnterminatedComment(self.text)};
LineComment
    :   '//' ~[\r\n]*
        -> skip
    ;

// ------------------ 3.1 ------------------
WS: [ \t\r\f\n]+ -> skip;

fragment
    UncloseString
    :   '"' Schar*
    ;
fragment
    UnterminatedCommentString
    :   '/*' Schar*
    ;

UNCLOSE_STRING: UncloseString {raise UncloseString(self.text[1:])};
ERROR_CHAR: . {raise ErrorToken(self.text)};
ILLEGAL_ESCAPE: . {raise IllegalEscape(self.text)};
UNTERMINATED_COMMENT: UnterminatedCommentString {raise UnterminatedComment(self.text)};
