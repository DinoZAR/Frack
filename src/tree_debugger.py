from language.FrackListener import FrackListener
from language.FrackParser import FrackParser

class TreeDebugger(FrackListener):

    def enterProgram(self, ctx:FrackParser.ProgramContext):
        print('Enter program!')

    def exitProgram(self, ctx:FrackParser.ProgramContext):
        print('Exit program!')

    def enterFunction(self, ctx:FrackParser.FunctionContext):
        print('Enter function!')

    def exitFunction(self, ctx:FrackParser.FunctionContext):
        print('Exit function!')

    def enterParameters(self, ctx:FrackParser.ParametersContext):
        print('Enter parameters!')

    def exitParameters(self, ctx:FrackParser.ParametersContext):
        print('Exit parameters!')
