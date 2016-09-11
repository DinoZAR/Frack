from language.FrackLexer import FrackLexer
from language.FrackParser import FrackParser
from language.FrackListener import FrackListener
import antlr4
from tree_debugger import TreeDebugger

TEST_FILE = 'test.frack'


def main():

    lexer = FrackLexer(antlr4.FileStream(TEST_FILE))
    stream = antlr4.CommonTokenStream(lexer)
    parser = FrackParser(stream)
    tree = parser.program()

    debugger = TreeDebugger()
    walker = antlr4.ParseTreeWalker()

    walker.walk(debugger, tree)

    print('done!')

if __name__ == '__main__':
    main()