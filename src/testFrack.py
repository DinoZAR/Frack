import antlr4

from language.FrackLexer import FrackLexer
from language.FrackParser import FrackParser
from parser.listener import Listener


TEST_FILE = 'test.frack'


def main():

    # Setup lexers and parsers
    lexer = FrackLexer(antlr4.FileStream(TEST_FILE))
    stream = antlr4.CommonTokenStream(lexer)
    parser = FrackParser(stream)
    tree = parser.program()

    # Actually parse the program
    listener = Listener()
    walker = antlr4.ParseTreeWalker()
    #walker.walk(listener, tree)
    print(tree.toStringTree())

    for f in listener.functions:
        print(f)

    print('done!')

if __name__ == '__main__':
    main()