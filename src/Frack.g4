grammar Frack;

program : function+;
function : IDENT '(' parameters? ')';
parameters : IDENT 'as' IDENT (',' IDENT 'as' IDENT)*;


IDENT : [a-zA-Z1-9_]+;
WS : [ \t\r\n]+ -> skip;