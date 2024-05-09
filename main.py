from syntax_analysis import *
from lexical_analysis import *
import argparse
import logging as log

# input example:
# main.py -lex 1 -syn 0 -f syntax_tree_data - v
# main.py -h / main.py --help 

parser = argparse.ArgumentParser()
parser.add_argument('-lex', '--lexical_analysis_recovery', action='store', nargs=1, help='Choose Lexical Analysis Method\n 0: No recovery, 1: Skip incorrect symbols, 2: Insert expected symbols')
parser.add_argument('-syn', '--syntax_analysis_recovery', action='store', nargs=1, help='Choose Syntax Analysis Method\n 0: No recovery, 3: Panic Mode Recovery, 4: Phrase Level Recovery')
parser.add_argument('-f', '--file_name_tree', action='store', nargs=1, help='Enter the name of the file where to save the syntax tree graphviz visualization code (a new file will be created). If no name provided, graphviz visualization omitted.')
parser.add_argument('-v', '--verbose', action='store_true', help = 'Verbose Mode')

def main():
    try:
        args = parser.parse_args()

        lex_recovery = int(args.lexical_analysis_recovery[0]) if args.lexical_analysis_recovery else None
        syn_recovery = int(args.syntax_analysis_recovery[0]) if args.syntax_analysis_recovery else None
        file_name = args.file_name_tree[0] if args.file_name_tree else None
        
        # check if the entered flags are valid:
        # we got a lexical recovery flag but it's not 0 1 or 2 / syn rec flag which is not 0 3 4
        if lex_recovery and not (lex_recovery == 0 or lex_recovery == 1 or lex_recovery == 2):
            print('Wrong lexical analysis recovery flag value. Perish')
            exit()
        if syn_recovery and not (syn_recovery == 0 or syn_recovery == 3 or syn_recovery == 4):
            print('Wrong syntax analysis recovery flag value. Perish')
            exit()
        
        # Ak je zapnuty verbose, tak bude vypisovat log.info printy o postupe 
        if args.verbose:
            log.basicConfig(format="%(levelname)s: %(message)s", level=log.DEBUG)
        else:
        # Ak je verbose vypnuty, vypise len error/warning a printy, ze inputy boli akceptovane a vysledne tokeny
            log.basicConfig(format="%(levelname)s: %(message)s")

    except Exception as e:
        print(e)
        print("Invalid parsing arguments. Exiting...")
        exit()

    # todo: test if two recoveries work at the same time

    print("\n°˖✧ Lexical and syntax analyzer ✧˖°\n")
    while True:
        try:
            vstup = input("\nType INPUT or PRESS CTRL + C to exit the program: ")

            print("\nTOKENIZER\n")
            tokens = tokenize(vstup, dfa, recovery_mode='ignore' if lex_recovery == 1 else 'insert' if lex_recovery == 2 else None)
            if not tokens:
                log.error("Tokenizer input was rejected\n")
                continue
            print(f"Tokenized input: {tokens}")

            print("\nSYNTAX ANALYSIS\n")
            parse(tokens, file_name, recovery_mode='panic' if syn_recovery == 3 else 'phrase' if syn_recovery == 4 else None)

        except KeyboardInterrupt:
            print("\nExiting program...")
            break


if __name__ == "__main__":
    main()