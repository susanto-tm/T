from sys import *

tokens = []


def open_file(filename):
    data = open(filename, "r").read()
    return data


def lexer(file_contents):
    tok = ""  # token for when a keyword is matched
    state = 0  # state when the strings start "string"
    string = ""  # receives the characters between a string

    file_contents = list(file_contents)

    for char in file_contents:
        tok += char
        if tok == " ":
            if state == 0:  # when it is in the file
                tok = ""  # ignore if it starts with a space or has a space
            else:  # when it is in a string
                tok = " "
        elif tok == "print >" or tok == "print>" or tok == "print > ":
            tokens.append("print")
            tok = ""  # resets tok for next loop so it doesnt start at "print"
        elif tok == "\n":
            tok = ""
        elif tok == "\"":
            # begin searching for the words in a string and finding when the quotes start and end
            if state == 0:
                state = 1
            elif state == 1:
                # when string is found it ends searching and resets all parameters
                tokens.append("STRING:" + string + "\"")
                string = ""
                state = 0
                tok = ""
        elif state == 1:
            # begin copying down what is between the quotes
            string += tok
            tok = ""  # once string ends it resets tok
    return tokens
    # print(tokens)


def parse(token_data):
    i = 0
    while i < len(token_data):
        if token_data[i] + " " + token_data[i+1][0:6] == "print STRING":
            print(token_data[i+1][8:-1])
            i += 2


def run():
    data = open_file(argv[1])
    token_data = lexer(data)
    parse(token_data)


run()
