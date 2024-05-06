# precita vstup od usera alebo zo suboru alebo whatever, potom zavola tokanizer a potom syntakticku analyzu
from syntakticka_analyza import *
from lexikalna_analyza import *

def main():
    while True:
        try:
            print("Lexikalny a syntakticky analyzator\n")
            print("Zadajte vstup alebo stlacte ctrl+c pre ukoncenie programu\n")
            vstup = input("Zadajte vstup: ")
            print("TOKENIZATOR\n")
            tokens = tokenize(vstup, dfa)
            if not tokens:
                print("Vstup bol rejected\n")
                continue
            print(f"Tokenizovany vstup: {tokens}")
            print("SYNTAKTICKA ANALYZA\n")
            parse(tokens)
        except KeyboardInterrupt:
            print("\nProgram bol ukonceny")
            break


if __name__ == "__main__":
    main()