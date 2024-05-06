# precita vstup od usera alebo zo suboru alebo whatever, potom zavola tokanizer a potom syntakticku analyzu
from syntakticka_analyza import *
from lexikalna_analyza import *

def main():
    while True:
        try:
            print("Lexikalny a syntakticky analyzator\n")
            print("Mod Zotavenia z chyb: \n")
            print("Napiste 1, ak chcete zotavit chybu v lexikalnej analyze pomocou ignorovania chybnych znakov\n")
            print("Napiste 2, ak chcete zotavit chybu v lexikalnej analyze pomocou pridania ocakavanych znakov\n")
            print("Napiste 3, ak chcete zotavit chybu v syntaktickej analyze pomocou Panic-Mode Recovery\n")
            print("Napiste 4, ak chcete zotavit chybu v syntaktickej analyze pomocou Phrase-Level Recovery\n")
            print("Stlacte enter ak nechcete zapnut zotavovanie chyb\n")
            recovery_mode = input("Vyberte mod zotavenia: ")
            if recovery_mode == "1":
                recovery_mode = "ignore"
            elif recovery_mode == "2":
                recovery_mode = "insert"
            elif recovery_mode == "3":
                recovery_mode = "panic"
            elif recovery_mode == "4":
                recovery_mode = "phrase"
            else:
                recovery_mode = None
            # TODO
            print("Zadajte vstup alebo stlacte ctrl+c pre ukoncenie programu\n")
            vstup = input("Zadajte vstup: ")
            print("TOKENIZATOR\n")
            tokens = tokenize(vstup, dfa, recovery_mode=recovery_mode)
            if not tokens:
                print("Vstup bol rejected\n")
                continue
            print(f"Tokenizovany vstup: {tokens}")
            #print("SYNTAKTICKA ANALYZA\n")
            #parse(tokens, recovery_mode=recovery_mode)
        except KeyboardInterrupt:
            print("\nProgram bol ukonceny")
            break


if __name__ == "__main__":
    main()