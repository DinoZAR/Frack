# Generated from C:/Users/Spencer/Desktop/frack/src\Frack.g4 by ANTLR 4.5.3
from antlr4 import *
from io import StringIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\2\b")
        buf.write("$\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\3\2\3\2\3\3\3\3\3\4\3\4\3\4\3\5\3\5\3\6\6\6\32\n\6\r")
        buf.write("\6\16\6\33\3\7\6\7\37\n\7\r\7\16\7 \3\7\3\7\2\2\b\3\3")
        buf.write("\5\4\7\5\t\6\13\7\r\b\3\2\4\6\2\63;C\\aac|\5\2\13\f\17")
        buf.write("\17\"\"%\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2")
        buf.write("\2\2\13\3\2\2\2\2\r\3\2\2\2\3\17\3\2\2\2\5\21\3\2\2\2")
        buf.write("\7\23\3\2\2\2\t\26\3\2\2\2\13\31\3\2\2\2\r\36\3\2\2\2")
        buf.write("\17\20\7*\2\2\20\4\3\2\2\2\21\22\7+\2\2\22\6\3\2\2\2\23")
        buf.write("\24\7c\2\2\24\25\7u\2\2\25\b\3\2\2\2\26\27\7.\2\2\27\n")
        buf.write("\3\2\2\2\30\32\t\2\2\2\31\30\3\2\2\2\32\33\3\2\2\2\33")
        buf.write("\31\3\2\2\2\33\34\3\2\2\2\34\f\3\2\2\2\35\37\t\3\2\2\36")
        buf.write("\35\3\2\2\2\37 \3\2\2\2 \36\3\2\2\2 !\3\2\2\2!\"\3\2\2")
        buf.write("\2\"#\b\7\2\2#\16\3\2\2\2\5\2\33 \3\b\2\2")
        return buf.getvalue()


class FrackLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]


    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    IDENT = 5
    WS = 6

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'('", "')'", "'as'", "','" ]

    symbolicNames = [ "<INVALID>",
            "IDENT", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "IDENT", "WS" ]

    grammarFileName = "Frack.g4"

    def __init__(self, input=None):
        super().__init__(input)
        self.checkVersion("4.5.3")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


