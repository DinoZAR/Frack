grammar Frack;

program : functionDefinition+;

// Functions
functionDefinition : IDENT '(' parameters? ')' dataType? '{' statement* '}';
parameters : parameter (',' parameter)*;
parameter : IDENT dataType?;
dataType : 'as' IDENT ('.' IDENT)*;

// Statements
statement : assignment
    | expression;

assignment : IDENT dataType? '=' expression;

// Expressions
expression : expression '*' expression
    | expression '/' expression
    | expression '+' expression
    | expression '-' expression
    | '!' expression
    | value
    | NUM;

value : IDENT '.' value
    | IDENT '(' (expression (',' expression)*)? ')' '.' value
    | IDENT '(' (expression (',' expression)*)? ')'
    | IDENT;

NUM : [0-9]+('.'[0-9]+)?;
IDENT : [a-zA-Z_][a-zA-Z1-9_]*;
WS : [ \t\r\n]+ -> skip;