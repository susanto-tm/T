import re


class Lexer(object):
    def __init__(self, data):
        self.data = data

    def tokenize(self):
        # list where all the tokens will go to
        tokens = []

        # variable to split the words in the source code
        data = self.data.split()

        # index to keep track of source code
        pos = 0

        # loop through each word in the source code
        while pos < len(data):
            text = data[pos]
            # recognize the type of data being sent as a variable
            if text == "int":
                tokens.append(['INTEGER', text])
            elif text == "print":
                tokens.append(['METHOD', text])
            # recognize whether after variable declaration it is variable name or not
            elif re.match('[a-z]', text) or re.match('[A-Z]', text):
                if text[len(text) - 1] == ";":
                    tokens.append(['IDENTIFIER', text[0:len(text) - 1]])
                else:
                    tokens.append(['IDENTIFIER', text])
            # matches if it is a number, then identify it as a constant
            elif re.match('[0-9]', text):
                if text[len(text) - 1] == ";":
                    tokens.append(['CONSTANT', text[0:len(text) - 1]])
                else:
                    tokens.append(['IDENTIFIER', text])
            # recognizes if the source code has an OPERATOR
            elif text in "*/=+-":
                tokens.append(['OPERATOR', text])
            # if a statement ends with a (;) then add END OF STATEMENT (EOS) to tokens
            if text[len(text) - 1] == ";":
                tokens.append(['EOS', ';'])

            pos += 1
        print(tokens)

        return tokens
