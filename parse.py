import sys

variables = []


class Parser(object):
    def __init__(self, tokens):
        # create global variables which will take tokens from the lexer
        self.tokens = tokens
        self.token_index = 0

    def parse(self):
        while self.token_index < len(self.tokens):
            # holds the token type as the first value in the token (i.e. the INTEGER/IDENTIFIER/etc)
            token_type = self.tokens[self.token_index][0]
            # holds the value of the token as the second value in the token
            token_value = self.tokens[self.token_index][1]

            # if the token type is an INTEGER and its value is an INT
            if token_type == "INTEGER" and token_value == "int":
                # checks if next token identifier is an operator -- where it is a variable declaration and not function
                if self.tokens[self.token_index + 2][0] == "OPERATOR":
                    # check if the value of the CONSTANT is an integer
                    if self.tokens[self.token_index + 3][1].isnumeric():
                        # if it is then put the tokens through to parse in the function "parse_variable_declaration"
                        self.parse_variable_declaration(self.tokens[self.token_index:len(self.tokens)])
                    # if not, then write an error saying that it is not an integer
                    else:
                        sys.stderr.write('Value is not an integer: %s\n' % self.tokens[self.token_index + 3][1])
                        sys.exit(1)
            # if the token type is a METHOD and its value is a print
            if token_type == "METHOD" and token_value == "print":
                # check if the next value is a string or a variable
                if self.tokens[self.token_index + 1][0] == "IDENTIFIER":
                    self.print_variable_input(variables, self.token_index)

            self.token_index += 1

    def parse_variable_declaration(self, token_stream):
        tokens_checked = 0
        variable = []
        for token in range(0, len(token_stream)):
            token_type = token_stream[tokens_checked][0]
            token_value = token_stream[tokens_checked][1]

            if token_type == "EOS":
                variables.append(variable)
                # self.print_variables()
                break

            # this will get variable type (i.e. int, char, float)
            if token == 0:
                print("Variable type is: " + token_value)
            # gets variable name and perform error if it is invalid
            elif token == 1 and token_type == "IDENTIFIER":
                print("Variable name: " + token_value)
                variable.append(token_value)
            elif token == 1 and token_type != "IDENTIFIER":
                sys.stderr.write("Invalid variable name: '%s'\n" % token_value)
                sys.exit(1)
            # gets operator and checks if the operator is valid
            elif token == 2 and token_type == "OPERATOR":
                print("Assignment Operator: " + token_value)
            elif token == 2 and token_type != "OPERATOR":
                sys.stderr.write("Operator missing or invalid")
                sys.exit(1)
            # gets the constant (error handling is done beforehand since this is for an int)
            elif token == 3 and token_type == "CONSTANT":
                print("Integer Value: " + token_value)
                variable.append(token_value)

            tokens_checked += 1

    def print_variable_input(self, token_stream, index):
        tokens_checked = 0

        for token in range(0, len(token_stream)):
            # check if the variable submitted matches the variable in the source code
            if self.tokens[index + 1][1] == token_stream[tokens_checked][0]:
                print(token_stream[tokens_checked][1])

                if self.tokens[index + 2][1] == ";":
                    break

            self.token_index += 1
            tokens_checked += 1

    # def print_variables(self):
    #     print(variables)

