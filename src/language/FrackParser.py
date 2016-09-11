# Generated from C:/Users/Spencer/Desktop/frack/src\Frack.g4 by ANTLR 4.5.3
# encoding: utf-8
from antlr4 import *
from io import StringIO

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3\b")
        buf.write("!\4\2\t\2\4\3\t\3\4\4\t\4\3\2\6\2\n\n\2\r\2\16\2\13\3")
        buf.write("\3\3\3\3\3\5\3\21\n\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\7\4\34\n\4\f\4\16\4\37\13\4\3\4\2\2\5\2\4\6\2\2 ")
        buf.write("\2\t\3\2\2\2\4\r\3\2\2\2\6\24\3\2\2\2\b\n\5\4\3\2\t\b")
        buf.write("\3\2\2\2\n\13\3\2\2\2\13\t\3\2\2\2\13\f\3\2\2\2\f\3\3")
        buf.write("\2\2\2\r\16\7\7\2\2\16\20\7\3\2\2\17\21\5\6\4\2\20\17")
        buf.write("\3\2\2\2\20\21\3\2\2\2\21\22\3\2\2\2\22\23\7\4\2\2\23")
        buf.write("\5\3\2\2\2\24\25\7\7\2\2\25\26\7\5\2\2\26\35\7\7\2\2\27")
        buf.write("\30\7\6\2\2\30\31\7\7\2\2\31\32\7\5\2\2\32\34\7\7\2\2")
        buf.write("\33\27\3\2\2\2\34\37\3\2\2\2\35\33\3\2\2\2\35\36\3\2\2")
        buf.write("\2\36\7\3\2\2\2\37\35\3\2\2\2\5\13\20\35")
        return buf.getvalue()


class FrackParser ( Parser ):

    grammarFileName = "Frack.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'as'", "','" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "IDENT", "WS" ]

    RULE_program = 0
    RULE_function = 1
    RULE_parameters = 2

    ruleNames =  [ "program", "function", "parameters" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    IDENT=5
    WS=6

    def __init__(self, input:TokenStream):
        super().__init__(input)
        self.checkVersion("4.5.3")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def function(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FrackParser.FunctionContext)
            else:
                return self.getTypedRuleContext(FrackParser.FunctionContext,i)


        def getRuleIndex(self):
            return FrackParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = FrackParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 7 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 6
                self.function()
                self.state = 9 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==FrackParser.IDENT):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FunctionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENT(self):
            return self.getToken(FrackParser.IDENT, 0)

        def parameters(self):
            return self.getTypedRuleContext(FrackParser.ParametersContext,0)


        def getRuleIndex(self):
            return FrackParser.RULE_function

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction" ):
                listener.enterFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction" ):
                listener.exitFunction(self)




    def function(self):

        localctx = FrackParser.FunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_function)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 11
            self.match(FrackParser.IDENT)
            self.state = 12
            self.match(FrackParser.T__0)
            self.state = 14
            _la = self._input.LA(1)
            if _la==FrackParser.IDENT:
                self.state = 13
                self.parameters()


            self.state = 16
            self.match(FrackParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ParametersContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENT(self, i:int=None):
            if i is None:
                return self.getTokens(FrackParser.IDENT)
            else:
                return self.getToken(FrackParser.IDENT, i)

        def getRuleIndex(self):
            return FrackParser.RULE_parameters

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameters" ):
                listener.enterParameters(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameters" ):
                listener.exitParameters(self)




    def parameters(self):

        localctx = FrackParser.ParametersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_parameters)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 18
            self.match(FrackParser.IDENT)
            self.state = 19
            self.match(FrackParser.T__2)
            self.state = 20
            self.match(FrackParser.IDENT)
            self.state = 27
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==FrackParser.T__3:
                self.state = 21
                self.match(FrackParser.T__3)
                self.state = 22
                self.match(FrackParser.IDENT)
                self.state = 23
                self.match(FrackParser.T__2)
                self.state = 24
                self.match(FrackParser.IDENT)
                self.state = 29
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





