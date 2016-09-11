from language.FrackListener import FrackListener
from language.FrackParser import FrackParser

from parser.frack_elements import *


class Listener(FrackListener):

    def __init__(self):
        self.functions = []

        self._currFuncName = ''
        self._currParams = []

    def enterFunctionDefinition(self, ctx:FrackParser.FunctionDefinitionContext):
        self._currFuncName = ctx.IDENT().getText()
        print(self._currFuncName + '()')

    def enterParameter(self, ctx:FrackParser.ParameterContext):
        hasDataType = ctx.getChildCount() > 1
        name = ctx.children[0].getText()
        if hasDataType:
            dataType = ctx.children[1].children[1].getText()
        else:
            dataType = ""
        print('Parameter -> ' + name + ' as ' + dataType)
        self._currParams.append(Parameter(name, dataType))

    def exitFunctionDefinition(self, ctx:FrackParser.FunctionDefinitionContext):
        self.functions.append(Function(self._currFuncName, self._currParams))