from sys import *

tokens = []

def open_file(filename):
    if filename == None:
        print("There is no input file.")
    elif filename != None:
        data = open(filename, "r").read()
        return data

def lex(filecontents):
        tok = ""
        state = 0
        string = ""
        expr = ""
        nm = ""
        filecontents = list(filecontents)
        for char in filecontents:
                tok += char
                if tok == " ":
                    if state == 0:
                        tok = ""
                    else:
                        tok = " "
                elif tok == "\n" or tok == "<EOF>":
                    if expr != "" and isexpr == 1:
                        print(expr + "Int")
                        expr = ""
                    elif expr != "" and isexpr == 0:
                        print(expr + "Int")
                        expr = ""
                    tok = ""
                elif tok.lower() == "write":
                        tokens.append("write")
                        tok = ""
                elif tok == "0" or tok == "1" or tok == "2" or tok == "3" or tok == "4" or tok == "5" or tok == "6" or tok == "7" or tok == "8" or tok == "9":
                    expr += tok
                    tok = ""
                elif tok == "+":
                    isexpr = 1
                    expr += tok
                    tok = ""
                elif tok == "\"":
                        if state == 0:
                                state = 1
                        elif state == 1:
                                tokens.append("string:" + string + "\"")
                                string = ""
                                state = 0
                                tok = ""
                elif state == 1:
                        string += tok
                        tok = ""

                print(expr)
        return tokens
def parse(toks):
    v = 0
    print(v)
    while(v < len(toks)):
        if toks[v] + " " + toks[v+1][0:6] == "write string":
            print(toks[v+1][7:])
            v += 2
    
def run():
    if len(argv) > 1:
        data = open_file(argv[1])
        toks = lex(data)
        parse(toks)
    elif len(argv) < 2:
        print("There is no input file.")

def main():
    run()
    
if __name__ == '__main__':
    main()