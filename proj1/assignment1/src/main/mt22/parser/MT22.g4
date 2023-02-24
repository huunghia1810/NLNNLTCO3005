//Nguyen Huu Nghia, MSSV: 2033068
grammar MT22;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

program: (variable_decl| func_decl | func_main)* EOF ;

//// --------------- Parser ----------------------------------------- ////

// func_main
func_main
    :   MAIN COLON FUNCTION VoidType LPAREN RPAREN main_return
    ;

main_return
    :   LBRACKET (stmt|variable_decl)* RBRACKET
    ;

// 3.5 - arrayL
arrayL
    :   LBRACKET expr_list RBRACKET
    ;

// 7 - statement: stmt
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

// 7.1 - assign_stmt
assign_stmt
    :   lhs ASIGN expression SEMICOLON
    ;

lhs
    :   Identifier
    |   index_expr
    ;

// 7.2 - if_stmt
if_stmt
    :   IF LPAREN expression RPAREN stmt (ELSE stmt)?
    ;

// 7.3 - for_stmt
for_stmt
    :   FOR LPAREN Identifier ASIGN expression COMMA expression COMMA expression RPAREN stmt
    ;

// 7.4 - while_stmt
while_stmt
    :   WHILE LPAREN expression RPAREN stmt
    ;

// 7.5 - do_while_stmt
do_while_stmt
    :   DO block_stmt WHILE LPAREN expression RPAREN SEMICOLON
    ;

// 7.6 - break_stmt
break_stmt
    :   BREAK SEMICOLON
    ;

// 7.7 - continue_stmt
continue_stmt
    :   CONTINUE SEMICOLON
    ;

// 7.8 - return_stmt
return_stmt
    :   RETURN expression? SEMICOLON
    ;

// 7.9 - call_stmt
call_stmt
    :   func_call SEMICOLON
    ;

// 7.10 - block_stmt
block_stmt
    :   LBRACKET (stmt | variable_decl)* RBRACKET
    ;

// 5.1 - variable_decl
variable_decl
    :   l=identifier_list COLON valid_type ASIGN r=expr_list e=SEMICOLON
    {if len($l.text.split(',')) != len($r.text.split(',')):
        raise Exception('Error on line {} col {}: ;'.format($e.line, $e.pos))
    }
    |   identifier_list COLON atomic_type SEMICOLON
    ;

identifier_list
    :   Identifier (COMMA Identifier)*
    ;

valid_type
    :   atomic_type
    |   AutoType
    ;

// 5.2 para_decl
para_list_decl
    :   para_decl (COMMA para_decl)*
    ;

para_decl
    :   INHERIT? OUT? Identifier COLON atomic_type
    ;

// 5.3 func_decl
func_decl
    :   func_prototype func_body
    ;

func_prototype
    :   Identifier COLON FUNCTION func_return_type LPAREN para_list_decl RPAREN (INHERIT Identifier)?
    ;

func_return_type
    :   atomic_type
    |   VoidType
    |   AutoType
    ;

func_body
    :   LBRACKET (stmt|variable_decl)* RBRACKET
    ;

// 6 - expression
// 6.6 - func_call
func_call
    :   Identifier LPAREN arg_list* RPAREN
    ;

arg_list
    :   expression (COMMA expression)*
    ;

expression
    :   relation_expr (DOUBLECOLON relation_expr)?
    ;

relation_expr
    :   logical_expr (relation_op logical_expr)?
    ;

relation_op
    :   (EQEQ | NOTEQ | LESS | CREATER | LESSEQ | CREATEREQ)
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
    :   (PLUS | MINUS)
    ;

multiplying_expr
    :   multiplying_expr multiplying_op unary_logical_expr
    |   unary_logical_expr
    ;

multiplying_op
    :   (STAR | DIV | MOD)
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
    :   (MINUS)
    ;

index_expr
    :   Identifier LSQUARE expr_list RSQUARE
    |   Identifier
    |   BooleanL
    |   IntegerL
    |   FloatL
    |   StringL
    |   arrayL  //?
    |   func_call
    //
    ;

expr_list
    :   expression (COMMA expression)*
    ;

// 4.2 - array_decl
array_decl
    :   ArrayType LSQUARE integer_list RSQUARE OF atomic_type
    ;

integer_list
    :   IntegerL (COMMA IntegerL)*
    ;

atomic_type
    :   BooleanType
    |   IntegerType
    |   FloatType
    |   StringType
    ;

//// --------------- Lexer ------------------------------------------ ////


// 4.1 - Atomic types : BooleanType | IntegerType | FloatType | StringType
// - BooleanType
BooleanType
    :   BOOLEAN //{self.text += " BooleanType"}
    ;

//BooleanOpt
//    :   (NOT | ANDAND | OROR | EQEQ | NOTEQ) //{self.text += " BooleanOpt"}
//    ;

// - IntegerType
IntegerType
    :  INTEGER //{self.text += " IntegerType"}
    ;

//IntegerOpt
//    :   (PLUS | MINUS | STAR | DIV | MOD | EQEQ | NOTEQ | LESS | LESSEQ | CREATEREQ | CREATER) {self.text += " IntegerOpt"}
//    ;

// - FloatType
FloatType
    :   FLOAT //{self.text += " FloatType"}
    ;

// - StringType
StringType
    :   STRING //{self.text += " StringType"}
    ;

// 4.2 - Array Type
ArrayType
    :   ARRAY //{self.text += " ArrayType"}
    ;

// 4.3 - Void Type
VoidType
    :   VOID //{self.text += " VoidType"}
    ;

// 4.4 - Auto Type
AutoType
    :   AUTO //{self.text += " AutoType"}
    ;

// 3.7 - Literal: IntegerL | FloatL | BooleanL | StringL | arrayL
// - IntegerL
IntegerL
    :   [1-9] ('_'[0-9] | [0-9])* {self.text = self.text.replace('_', '')}//{self.text += " IntegerL"}
    |   '0'
    ;

// - FloatL
FloatL
    :   IntegerL DecimalP ExponentP? {self.text = self.text.replace('_', '')}
    |   IntegerL ExponentP
    |   DecimalP ExponentP
    ;

fragment
DecimalP: '.' [0-9]* ;

fragment
ExponentP: [eE] [+-]? [0-9]+ ;


// - BooleanL
BooleanL
    :   (TRUE | FALSE) //{self.text += " BooleanL"}
    ;

// - StringL
StringL
    :   '"' Schar* '"' {self.text = self.text[1:-1]}
    ;

fragment Schar:
	~ ["\\]
	| EscapeSequence
    ;

fragment
EscapeSequence
    :   '\\b'
    |   '\\f'
    |   '\\r'
    |   '\\n'
    |   '\\t'
    |   '\\\''
    |   '\\\\'
    |   '\\"'
    ;

// 3.6 - Seperator
LPAREN:     '(' ;
RPAREN:     ')' ;
LSQUARE:    '[' ;
RSQUARE:    ']' ;
DOT:        '.' ;
COMMA:      ',' ;
SEMICOLON:  ';' ;
COLON:      ':' ;
LBRACKET:   '{' ;
RBRACKET:   '}' ;
ASIGN:      '=' ;

// 3.5 - Operator
PLUS:       '+' ;
MINUS:      '-' ;
STAR:       '*' ;
DIV:        '/' ;
MOD:        '%' ;
NOT:        '!' ;
ANDAND:     '&&' ;
OROR:       '||' ;
EQEQ:       '==' ;
NOTEQ:      '!=' ;
LESS:       '<' ;
LESSEQ:     '<=' ;
CREATER:    '>' ;
CREATEREQ:  '>=' ;
DOUBLECOLON: '::' ;

// 3.4 - Keyword
AUTO:       'auto' ;
BREAK:      'break' ;
BOOLEAN:    'boolean' ;
DO:         'do' ;
ELSE:       'else' ;
FALSE:      'false' ;
FLOAT:      'float' ;
FOR:        'for' ;
FUNCTION:   'function' ;
IF:         'if' ;
INTEGER:    'integer' ;
RETURN:     'return' ;
STRING:     'string' ;
TRUE:       'true' ;
WHILE:      'while' ;
VOID:       'void' ;
OUT:        'out' ;
CONTINUE:   'continue' ;
OF:         'of' ;
INHERIT:    'inherit' ;
ARRAY:      'array' ;
MAIN:       'main' ;

// 3.3 - Identifier
//IdentifierList
//    :   Identifier (COMMA Identifier)* //{self.text += " IdenList"}
//    ;

Identifier
    :   [a-zA-Z_] [a-zA-Z_0-9]* //{self.text += " Identifier"}
    ;

// 3.1 - WhiteSpaces
WhiteSpaces
    :   [ \t\r\f\n]+
        -> skip
    ;

// 3.2 - BlockComment, LineComment
BlockComment
    :   '/*' .*? '*/'
        -> skip
    ;

LineComment
    :   '//' ~[\r\n]*
        -> skip
    ;

//// --------------- Exception -------------------------------------- ////
fragment
UncloseString
    :   '"' Schar*
    ;



UNCLOSE_STRING: UncloseString {raise UncloseString(self.text[1:])};
ERROR_CHAR: . { raise ErrorToken(self.text) };
//ILLEGAL_ESCAPE: . ;
