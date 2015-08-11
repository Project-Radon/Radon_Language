from sys import *

tokens = []

def open_file(filename):
    data = open(filename, "r").read()
    return data

def lex(filecontents):
        tok = ""
        state = 0
        string = ""
        filecontents = list(filecontents)
        for char in filecontents:
                tok += char
                if tok == " ":
                    if state == 0:
                        tok = ""
                    else:
                        tok = " "
                elif tok == "\n":
                    tok = ""
                elif tok == "write":
                        tokens.append("write")
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
                print(tokens)
        return tokens
def parse(toks):
    v = 0
    print(v)
    while(v < len(toks)):
        if toks[v] + " " + toks[v+1][0:6] == "write string":
            print("Found string")
            v += 2
    
def run():
    data = open_file(argv[1])
    toks = lex(data)
    parse(toks)

def main():
    run()
    
if __name__ == '__main__':
    main()