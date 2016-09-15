# Generated from /home/spencer/Documents/frack/src/Frack.g4 by ANTLR 4.5.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .FrackParser import FrackParser
else:
    from FrackParser import FrackParser

# This class defines a complete listener for a parse tree produced by FrackParser.
class FrackListener(ParseTreeListener):

    # Enter a parse tree produced by FrackParser#program.
    def enterProgram(self, ctx:FrackParser.ProgramContext):
        pass

    # Exit a parse tree produced by FrackParser#program.
    def exitProgram(self, ctx:FrackParser.ProgramContext):
        pass


    # Enter a parse tree produced by FrackParser#functionDefinition.
    def enterFunctionDefinition(self, ctx:FrackParser.FunctionDefinitionContext):
        pass

    # Exit a parse tree produced by FrackParser#functionDefinition.
    def exitFunctionDefinition(self, ctx:FrackParser.FunctionDefinitionContext):
        pass


    # Enter a parse tree produced by FrackParser#parameters.
    def enterParameters(self, ctx:FrackParser.ParametersContext):
        pass

    # Exit a parse tree produced by FrackParser#parameters.
    def exitParameters(self, ctx:FrackParser.ParametersContext):
        pass


    # Enter a parse tree produced by FrackParser#parameter.
    def enterParameter(self, ctx:FrackParser.ParameterContext):
        pass

    # Exit a parse tree produced by FrackParser#parameter.
    def exitParameter(self, ctx:FrackParser.ParameterContext):
        pass


    # Enter a parse tree produced by FrackParser#dataType.
    def enterDataType(self, ctx:FrackParser.DataTypeContext):
        pass

    # Exit a parse tree produced by FrackParser#dataType.
    def exitDataType(self, ctx:FrackParser.DataTypeContext):
        pass


    # Enter a parse tree produced by FrackParser#AssignmentStatement.
    def enterAssignmentStatement(self, ctx:FrackParser.AssignmentStatementContext):
        pass

    # Exit a parse tree produced by FrackParser#AssignmentStatement.
    def exitAssignmentStatement(self, ctx:FrackParser.AssignmentStatementContext):
        pass


    # Enter a parse tree produced by FrackParser#ExpressionStatement.
    def enterExpressionStatement(self, ctx:FrackParser.ExpressionStatementContext):
        pass

    # Exit a parse tree produced by FrackParser#ExpressionStatement.
    def exitExpressionStatement(self, ctx:FrackParser.ExpressionStatementContext):
        pass


    # Enter a parse tree produced by FrackParser#assignment.
    def enterAssignment(self, ctx:FrackParser.AssignmentContext):
        pass

    # Exit a parse tree produced by FrackParser#assignment.
    def exitAssignment(self, ctx:FrackParser.AssignmentContext):
        pass


    # Enter a parse tree produced by FrackParser#Add.
    def enterAdd(self, ctx:FrackParser.AddContext):
        pass

    # Exit a parse tree produced by FrackParser#Add.
    def exitAdd(self, ctx:FrackParser.AddContext):
        pass


    # Enter a parse tree produced by FrackParser#ValueExpr.
    def enterValueExpr(self, ctx:FrackParser.ValueExprContext):
        pass

    # Exit a parse tree produced by FrackParser#ValueExpr.
    def exitValueExpr(self, ctx:FrackParser.ValueExprContext):
        pass


    # Enter a parse tree produced by FrackParser#StringExpr.
    def enterStringExpr(self, ctx:FrackParser.StringExprContext):
        pass

    # Exit a parse tree produced by FrackParser#StringExpr.
    def exitStringExpr(self, ctx:FrackParser.StringExprContext):
        pass


    # Enter a parse tree produced by FrackParser#Sub.
    def enterSub(self, ctx:FrackParser.SubContext):
        pass

    # Exit a parse tree produced by FrackParser#Sub.
    def exitSub(self, ctx:FrackParser.SubContext):
        pass


    # Enter a parse tree produced by FrackParser#IfBlockExpr.
    def enterIfBlockExpr(self, ctx:FrackParser.IfBlockExprContext):
        pass

    # Exit a parse tree produced by FrackParser#IfBlockExpr.
    def exitIfBlockExpr(self, ctx:FrackParser.IfBlockExprContext):
        pass


    # Enter a parse tree produced by FrackParser#Exponent.
    def enterExponent(self, ctx:FrackParser.ExponentContext):
        pass

    # Exit a parse tree produced by FrackParser#Exponent.
    def exitExponent(self, ctx:FrackParser.ExponentContext):
        pass


    # Enter a parse tree produced by FrackParser#LessThanEqualTo.
    def enterLessThanEqualTo(self, ctx:FrackParser.LessThanEqualToContext):
        pass

    # Exit a parse tree produced by FrackParser#LessThanEqualTo.
    def exitLessThanEqualTo(self, ctx:FrackParser.LessThanEqualToContext):
        pass


    # Enter a parse tree produced by FrackParser#NotEquals.
    def enterNotEquals(self, ctx:FrackParser.NotEqualsContext):
        pass

    # Exit a parse tree produced by FrackParser#NotEquals.
    def exitNotEquals(self, ctx:FrackParser.NotEqualsContext):
        pass


    # Enter a parse tree produced by FrackParser#Div.
    def enterDiv(self, ctx:FrackParser.DivContext):
        pass

    # Exit a parse tree produced by FrackParser#Div.
    def exitDiv(self, ctx:FrackParser.DivContext):
        pass


    # Enter a parse tree produced by FrackParser#Not.
    def enterNot(self, ctx:FrackParser.NotContext):
        pass

    # Exit a parse tree produced by FrackParser#Not.
    def exitNot(self, ctx:FrackParser.NotContext):
        pass


    # Enter a parse tree produced by FrackParser#Equals.
    def enterEquals(self, ctx:FrackParser.EqualsContext):
        pass

    # Exit a parse tree produced by FrackParser#Equals.
    def exitEquals(self, ctx:FrackParser.EqualsContext):
        pass


    # Enter a parse tree produced by FrackParser#LessThan.
    def enterLessThan(self, ctx:FrackParser.LessThanContext):
        pass

    # Exit a parse tree produced by FrackParser#LessThan.
    def exitLessThan(self, ctx:FrackParser.LessThanContext):
        pass


    # Enter a parse tree produced by FrackParser#GreaterThanEqualTo.
    def enterGreaterThanEqualTo(self, ctx:FrackParser.GreaterThanEqualToContext):
        pass

    # Exit a parse tree produced by FrackParser#GreaterThanEqualTo.
    def exitGreaterThanEqualTo(self, ctx:FrackParser.GreaterThanEqualToContext):
        pass


    # Enter a parse tree produced by FrackParser#Mult.
    def enterMult(self, ctx:FrackParser.MultContext):
        pass

    # Exit a parse tree produced by FrackParser#Mult.
    def exitMult(self, ctx:FrackParser.MultContext):
        pass


    # Enter a parse tree produced by FrackParser#NumExpr.
    def enterNumExpr(self, ctx:FrackParser.NumExprContext):
        pass

    # Exit a parse tree produced by FrackParser#NumExpr.
    def exitNumExpr(self, ctx:FrackParser.NumExprContext):
        pass


    # Enter a parse tree produced by FrackParser#GreaterThan.
    def enterGreaterThan(self, ctx:FrackParser.GreaterThanContext):
        pass

    # Exit a parse tree produced by FrackParser#GreaterThan.
    def exitGreaterThan(self, ctx:FrackParser.GreaterThanContext):
        pass


    # Enter a parse tree produced by FrackParser#Paren.
    def enterParen(self, ctx:FrackParser.ParenContext):
        pass

    # Exit a parse tree produced by FrackParser#Paren.
    def exitParen(self, ctx:FrackParser.ParenContext):
        pass


    # Enter a parse tree produced by FrackParser#ifBlock.
    def enterIfBlock(self, ctx:FrackParser.IfBlockContext):
        pass

    # Exit a parse tree produced by FrackParser#ifBlock.
    def exitIfBlock(self, ctx:FrackParser.IfBlockContext):
        pass


    # Enter a parse tree produced by FrackParser#value.
    def enterValue(self, ctx:FrackParser.ValueContext):
        pass

    # Exit a parse tree produced by FrackParser#value.
    def exitValue(self, ctx:FrackParser.ValueContext):
        pass


