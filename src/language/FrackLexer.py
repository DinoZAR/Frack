# Generated from /home/spencer/Documents/frack/src/Frack.g4 by ANTLR 4.5.3
from antlr4 import *
from io import StringIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\2\22")
        buf.write("Y\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\3\2\3\2\3\3\3\3\3")
        buf.write("\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\7\3\b\3\b\3\t\3\t\3\n")
        buf.write("\3\n\3\13\3\13\3\f\3\f\3\r\3\r\3\16\3\16\3\17\6\17@\n")
        buf.write("\17\r\17\16\17A\3\17\3\17\6\17F\n\17\r\17\16\17G\5\17")
        buf.write("J\n\17\3\20\3\20\7\20N\n\20\f\20\16\20Q\13\20\3\21\6\21")
        buf.write("T\n\21\r\21\16\21U\3\21\3\21\2\2\22\3\3\5\4\7\5\t\6\13")
        buf.write("\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37")
        buf.write("\21!\22\3\2\6\3\2\62;\5\2C\\aac|\6\2\63;C\\aac|\5\2\13")
        buf.write("\f\17\17\"\"]\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t")
        buf.write("\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3")
        buf.write("\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2")
        buf.write("\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2")
        buf.write("\3#\3\2\2\2\5%\3\2\2\2\7\'\3\2\2\2\t)\3\2\2\2\13+\3\2")
        buf.write("\2\2\r-\3\2\2\2\17\60\3\2\2\2\21\62\3\2\2\2\23\64\3\2")
        buf.write("\2\2\25\66\3\2\2\2\278\3\2\2\2\31:\3\2\2\2\33<\3\2\2\2")
        buf.write("\35?\3\2\2\2\37K\3\2\2\2!S\3\2\2\2#$\7*\2\2$\4\3\2\2\2")
        buf.write("%&\7+\2\2&\6\3\2\2\2\'(\7}\2\2(\b\3\2\2\2)*\7\177\2\2")
        buf.write("*\n\3\2\2\2+,\7.\2\2,\f\3\2\2\2-.\7c\2\2./\7u\2\2/\16")
        buf.write("\3\2\2\2\60\61\7\60\2\2\61\20\3\2\2\2\62\63\7?\2\2\63")
        buf.write("\22\3\2\2\2\64\65\7,\2\2\65\24\3\2\2\2\66\67\7\61\2\2")
        buf.write("\67\26\3\2\2\289\7-\2\29\30\3\2\2\2:;\7/\2\2;\32\3\2\2")
        buf.write("\2<=\7#\2\2=\34\3\2\2\2>@\t\2\2\2?>\3\2\2\2@A\3\2\2\2")
        buf.write("A?\3\2\2\2AB\3\2\2\2BI\3\2\2\2CE\7\60\2\2DF\t\2\2\2ED")
        buf.write("\3\2\2\2FG\3\2\2\2GE\3\2\2\2GH\3\2\2\2HJ\3\2\2\2IC\3\2")
        buf.write("\2\2IJ\3\2\2\2J\36\3\2\2\2KO\t\3\2\2LN\t\4\2\2ML\3\2\2")
        buf.write("\2NQ\3\2\2\2OM\3\2\2\2OP\3\2\2\2P \3\2\2\2QO\3\2\2\2R")
        buf.write("T\t\5\2\2SR\3\2\2\2TU\3\2\2\2US\3\2\2\2UV\3\2\2\2VW\3")
        buf.write("\2\2\2WX\b\21\2\2X\"\3\2\2\2\b\2AGIOU\3\b\2\2")
        return buf.getvalue()


class FrackLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]


    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    T__10 = 11
    T__11 = 12
    T__12 = 13
    NUM = 14
    IDENT = 15
    WS = 16

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'('", "')'", "'{'", "'}'", "','", "'as'", "'.'", "'='", "'*'", 
            "'/'", "'+'", "'-'", "'!'" ]

    symbolicNames = [ "<INVALID>",
            "NUM", "IDENT", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "T__12", "NUM", 
                  "IDENT", "WS" ]

    grammarFileName = "Frack.g4"

    def __init__(self, input=None):
        super().__init__(input)
        self.checkVersion("4.5.3")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


