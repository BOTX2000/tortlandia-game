import sys

def add():
    print("lol")

def _sort(arg_def):
    defs=["add"]
    if arg_def in defs:
        try:
            print(eval(f"{arg_def}({sys.argv[2]})"))
        except:
            print(eval(f"{arg_def}()"))
    else:
        try:
            print(eval(f"{arg_def}({sys.argv[2]})"))
        except:
            print(eval(f"{arg_def}()"))
        

_sort(sys.argv[1])
