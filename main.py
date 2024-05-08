# precita vstup od usera alebo zo suboru alebo whatever, potom zavola tokanizer a potom syntakticku analyzu
from syntakticka_analyza import *
from lexikalna_analyza import *
import argparse
import logging as log

# main.py -lex 1 -syn 0 -s 
# input vstup 

parser = argparse.ArgumentParser()
parser.add_argument('-lex', '--lexical_analysis_recovery', action='store', nargs=1, help='Choose Lexical Analysis Method\n 0: No recovery, 1: Skip incorrect symbols, 2: Insert expected symbols')
parser.add_argument('-syn', '--syntax_analysis_recovery', action='store', nargs=1, help='Choose Syntax Analysis Method\n 0: No recovery, 3: Panic Mode Recovery, 4: Phrase Level Recovery')
parser.add_argument('-v', '--verbose', action='store_true', help = 'Verbose Mode')

def main():
    try:
        args = parser.parse_args()
        print(args.lexical_analysis_recovery)

        lex_recovery = int(args.lexical_analysis_recovery[0])
        syn_recovery = int(args.syntax_analysis_recovery[0])

        # check if the entered flags are valid:
        # we got a lexical recovery flag but it's not 0 1 or 2
        if lex_recovery and not (lex_recovery == 0 or lex_recovery == 1 or lex_recovery == 2):
            print('Wrong lexical analysis recovery flag value. Perish')
            exit()
        if syn_recovery and not (syn_recovery == 0 or syn_recovery == 3 or syn_recovery == 4):
            print('Wrong syntax analysis recovery flag value. Perish')
            exit()
        

        if args.verbose:
            print("Verbose je zapnuty, to znamena, ze chceme vypisovat veci")
            log.basicConfig(format="%(levelname)s: %(message)s", level=log.DEBUG)
            log.info("Verbose output.")
        else:
            print("Verbose je vypnuty takze shut up")
            log.basicConfig(format="%(levelname)s: %(message)s")
            
        # todo: remove these logs 
        log.info("This should be verbose.")
        log.debug(f'This should be {syn_recovery} verbose.')
        log.warning('this is ACCEPTED')
        log.warning("This is a warning.")
        log.error("This is an error.")

    except Exception as e:
        print(e)
        print("Invalid parsing arguments. Exiting...")
        exit()

    print("\n°˖✧ Lexical and syntax analyzer ✧˖°\n")
    while True:
        try:
            vstup = input("Type INPUT or PRESS CTRL + C to exit the program: ")

            print("\nTOKENIZER\n")
            tokens = tokenize(vstup, dfa, recovery_mode='ignore' if lex_recovery == 1 else 'insert' if lex_recovery == 2 else None)
            if not tokens:
                print("Tokenizer input was rejected\n")
                continue
            print(f"Tokenized input: {tokens}")

            print("\nSYNTAX ANALYSIS\n")
            parse(tokens, recovery_mode='panic' if syn_recovery == 3 else 'phrase' if syn_recovery == 4 else None)

        except KeyboardInterrupt:
            print("\nExiting program...")
            break


if __name__ == "__main__":
    main()