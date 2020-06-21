import sys


def lox():
    arg_len = len(sys.argv)

    # 2 b/c first arg is script
    if arg_len > 2:
        print('Usage: plox [script]')
    elif arg_len == 2:
        run_file(sys.argv[1])
    else:
        run_prompt()

def run_file(file_name):
    run()

def run_prompt():
    while True:
        user_input = input('> ')
        run()

def run():
    print('running!')

lox()
