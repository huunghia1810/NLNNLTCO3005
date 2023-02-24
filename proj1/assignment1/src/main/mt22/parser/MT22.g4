//Nguyen Huu Nghia, MSSV: 2033068
grammar MT22;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

program: (variable_decl | func_decl | func_main)* EOF ;

// ------------------ func_main ------------------
func_main
    :   MAIN COLON FUNCTION VoidType LP RP main_return
    ;

main_return
    :   LCB (stmt|variable_decl)* RCB
    ;

// ------------------ 7 - statement: stmt
stmt
    :   assign_stmt
    |   if_stmt
    |   for_stmt
    |   while_stmt
    |   do_while_stmt
    |   break_stmt
    |   continue_stmt
    |   return_stmt
    |   call_stmt
    |   block_stmt
    ;

// ------------------ 7.1 - assign_stmt
assign_stmt
    :   lhs ASSIGN expression SM
    ;

lhs
    :   ID
    |   index_expr
    ;

// ------------------ 7.2 if_stmt ------------------
if_stmt
    :   IF LP expression RP stmt (ELSE stmt)?
    ;

// ------------------ 7.3 for_stmt ------------------
for_stmt
    :   FOR LP ID ASSIGN expression CM expression CM expression RP stmt
    ;

// ------------------ 7.4 while_stmt ------------------
while_stmt
    :   WHILE LP expression RP stmt
    ;

// ------------------ 7.5 do_while_stmt ------------------
do_while_stmt
    :   DO block_stmt WHILE LP expression RP SM
    ;

// ------------------ 7.6 break_stmt
break_stmt
    :   BREAK SM
    ;

// ------------------ 7.7 continue_stmt
continue_stmt
    :   CONTINUE SM
    ;

// ------------------ 7.8 return_stmt ------------------
return_stmt
    :   RETURN expression? SM
    ;

// ------------------ 7.9 call_stmt ------------------
call_stmt
    :   func_call SM
    ;

// ------------------ 7.10 block_stmt ------------------
block_stmt
    :   LCB (stmt | variable_decl)* RCB
    ;

// ------------------ 5.1 variable_decl ------------------
variable_decl
    :   l = identifier_lst COLON valid_type ASSIGN r=expr_lst e=SM
    {if len($l.text.split(',')) != len($r.text.split(',')):
        raise Exception('Error on line {} col {}: ;'.format($e.line, $e.pos))
    }
    |   identifier_lst COLON atomic_type SM
    ;

identifier_lst
    :   ID (CM ID)*
    ;

valid_type
    :   atomic_type
    |   AutoType
    ;

// ------------------ 5.2 para_decl ------------------
para_lst_decl
    :   para_decl (CM para_decl)*
    ;

para_decl
    :   INHERIT? OUT? ID COLON atomic_type
    ;

// ------------------ 5.3 func_decl ------------------
func_decl
    :   func_prototype func_body
    ;

func_prototype
    :   ID COLON FUNCTION func_return_type LP para_lst_decl RP (INHERIT ID)?
    ;

func_return_type
    :   atomic_type
    |   VoidType
    |   AutoType
    ;

func_body
    :   LCB (stmt|variable_decl)* RCB
    ;

// ------------------ 6 - expression
// ------------------ 6.6 - func_call
func_call
    :   ID LP arg_lst* RP
    ;

arg_lst
    :   expression (CM expression)*
    ;

expression
    :   relation_expr (SRO relation_expr)?
    ;

relation_expr
    :   logical_expr (relation_op logical_expr)?
    ;

relation_op
    :   (EQ | INEQ | LT | GT | LE | GE)
    ;

logical_expr
    :   logical_expr logical_op adding_expr
    |   adding_expr
    ;

logical_op
    :   (ANDAND | OROR)
    ;

adding_expr
    :   adding_expr adding_op multiplying_expr
    |   multiplying_expr
    ;

adding_op
    :   (ADD | SUB)
    ;

multiplying_expr
    :   multiplying_expr multiplying_op unary_logical_expr
    |   unary_logical_expr
    ;

multiplying_op
    :   (MUL | DIV | MOD)
    ;

unary_logical_expr
    :   unary_logical_op (unary_logical_expr | sign_expr)
    |   sign_expr
    ;

unary_logical_op
    :   NOT
    ;

sign_expr
    :   sign_op (index_expr | sign_expr)
    |   index_expr
    ;

sign_op
    :   (SUB)
    ;

index_expr
    :   ID LSB expr_lst RSB
    |   ID
    |   BOOLLIT
    |   INTLIT
    |   FLOATLIT
    |   STRINGLIT
    |   arrayL //processing
    |   func_call
    //
    ;

arrayL: LCB expr_lst RCB;

expr_lst
    :   expression (CM expression)*
    ;

// ------------------ 4.2 array_decl ------------------
array_decl:   ArrayType LSB integer_lst RSB OF atomic_type;

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

// ------------------ 3.7 Literals: INTLIT | FLOATLIT | BOOLLIT | STRINGLIT ------------------
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
ANDAND:         '&&';
OROR:           '||';
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
IN:             'in'; //?
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

UNCLOSE_STRING: UncloseString {raise UncloseString(self.text[1:])};
ERROR_CHAR: . {raise ErrorToken(self.text)};
ILLEGAL_ESCAPE: . {raise IllegalEscape(self.text)};
