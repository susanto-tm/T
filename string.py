from sys import *

STRING, BEGIN, EOF = 'STRING', 'BEGIN', 'EOF'


def open_file(filename):
    data = open(filename, 'r').read()
    return data


class Token(object):
    def __init__(self, type, value):
        # token type: STRING, BEGIN, EOF
        self.type = type
        # value is the string between " "
        self.value = value

    def __str__(self):
        # format for tokens Token(STRING, "...") or Token(BEGIN, ")
        return "Token({type}, {value})".format(
            type=self.type,
            value=repr(self)
        )

    def __repr__(self):
        return self.__str__()


def run():
    data = open_file(argv[1])
    Token(data)
