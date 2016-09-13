grammar Frack;

program : functionDefinition+;

// Functions
functionDefinition : IDENT '(' parameters? ')' dataType? '{' statement* '}';
parameters : parameter (',' parameter)*;
parameter : IDENT dataType?;
dataType : 'as' IDENT ('.' IDENT)*;

// Statements
statement : assignment # AssignmentStatement
    | expression # ExpressionStatement;

// Assignments
assignment : IDENT dataType? '=' expression;

// Expressions
expression : expression '*' expression # Mult
    | expression '/' expression # Div
    | expression '+' expression # Add
    | expression '-' expression # Sub
    | '!' expression # Not
    | '(' expression ')' # Paren
    | value # ValueExpr
    | STRING # StringExpr
    | NUM # NumExpr;

value : IDENT '.' value
    | IDENT '(' (expression (',' expression)*)? ')' '.' value
    | IDENT '(' (expression (',' expression)*)? ')'
    | IDENT;

STRING : '"' CHAR_SEQUENCE? '"';
fragment CHAR_SEQUENCE : CHAR+;
fragment CHAR : ~["\\\r\n"]
    | ESCAPE_SEQUENCE
    | '\\\n'
    | '\\\r\n';

fragment ESCAPE_SEQUENCE : '\\x' HEX+;
fragment HEX : [0-9a-fA-F];

NUM : [0-9]+('.'[0-9]+)?;
IDENT : [a-zA-Z_][a-zA-Z1-9_]*;
WS : [ \t\r\n]+ -> skip;