from language.FrackListener import FrackListener
from language.FrackParser import FrackParser


class Listener(FrackListener):

    def __init__(self):
        self.functions = []

        self._currFuncName = ''
        self._currParams = []
        self._currStatements = []

        self._currExpression = None

    def enterFunctionDefinition(self, ctx:FrackParser.FunctionDefinitionContext):
        self._currFuncName = ctx.IDENT().getText()
        print(self._currFuncName + '()')

    def exitFunctionDefinition(self, ctx:FrackParser.FunctionDefinitionContext):
        self.functions.append({'funcName': self._currFuncName,
                               'params': self._currParams,
                               'statements': self._currStatements})
        self._currParams = []
        self._currStatements = []
        self._currFuncName = ""

    def exitParameter(self, ctx:FrackParser.ParameterContext):
        hasDataType = ctx.getChildCount() > 1
        name = ctx.IDENT().getText()
        dataType = self.getDataType(ctx.dataType())
        print('Parameter -> ' + name + ' as ' + dataType)
        self._currParams.append({'paramName': name, 'dataType': dataType})

    def exitAssignment(self, ctx:FrackParser.AssignmentContext):
        self._currStatements.append({'type': 'assignment',
                                     'name': ctx.IDENT().getText(),
                                     'dataType': self.getDataType(ctx.dataType()),
                                     'expression': self._currExpression})

    def exitExpressionStatement(self, ctx:FrackParser.ExpressionStatementContext):
        self._currStatements.append({'type': 'expression',
                                     'expression': self._currExpression})



    def getDataType(self, dataTypeToken):
        if dataTypeToken is not None:
            return dataTypeToken.children[1].getText()
        else:
            return ""
