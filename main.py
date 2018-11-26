from sys import *
import lexer
import parse


def main():
    # Reading the source code
    with open(argv[1], 'r') as file:
        content = file.read()

    # pass in content into the Lexer class in lexer.py
    lex = lexer.Lexer(content)
    # call the tokenize method
    tokens = lex.tokenize()

    # Parser
    parse_tokens = parse.Parser(tokens)
    parse_tokens.parse()


main()
