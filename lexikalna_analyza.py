# pip install automata-lib
from automata.fa.dfa import DFA

# Define DFA which accepts:
# 1. All letters a...Z 
# 2. All digits 0...9
# 3. http://
# 4. ftp://
# 5. telnet://
# 6. mailto:
# 7. /
# 8. ?
# 9. @
# 10. .
# 11. :
# 12. +

dfa = DFA(
    states={'q0', 'qH', 'qT', 'qT1', 'qE', 'qL', 'qN', 'qE2', 'qP', 'qT2', 'qF', 'qCOLON', 'qSLASH'},
    input_symbols={'a', 'b', 'h', 't', 'p', 'e', 'l', 'n', ':', '/'},
    transitions={
        'q0': {'a': 'q0', 'b': 'q0', 'h': 'qH', 't':'qT1', 'p':'q0', 'e':'q0', 'l':'q0', 'n':'q0', ':':'q0', '/':'q0'},
        'qH': {'a': 'q0', 'b': 'q0', 'h': 'qH', 't':'qT', 'p':'q0', 'e':'q0', 'l':'q0', 'n':'q0', ':':'q0', '/':'q0'},
        'qT': {'a': 'q0', 'b': 'q0', 'h': 'qH', 't':'qT1', 'p':'q0', 'e':'qE', 'l':'q0', 'n':'q0', ':':'q0', '/':'q0'},
        'qT1': {'a': 'q0', 'b': 'q0', 'h': 'qH', 't':'q0', 'p':'qP', 'e':'qE', 'l':'q0', 'n':'q0', ':':'q0', '/':'q0'},
        'qP': {'a': 'q0', 'b': 'q0', 'h': 'qH', 't':'qT', 'p':'q0', 'e':'q0', 'l':'q0', 'n':'q0', ':':'qCOLON', '/':'q0'},
        'qCOLON': {'a': 'q0', 'b': 'q0', 'h': 'qH', 't':'qT', 'p':'q0', 'e':'q0', 'l':'q0', 'n':'q0', ':':'q0', '/':'qSLASH'},
        'qSLASH': {'a': 'q0', 'b': 'q0', 'h': 'qH', 't':'qT', 'p':'q0', 'e':'q0', 'l':'q0', 'n':'q0', ':':'q0', '/':'qF'},
        'qF': {'a': 'q0', 'b': 'q0', 'h': 'qH', 't':'qT1', 'p':'q0', 'e':'qE', 'l':'q0', 'n':'q0', ':':'q0', '/':'q0'},

        'qE': {'a': 'q0', 'b': 'q0', 'h': 'qH', 't':'qT1', 'p':'q0', 'e':'qE', 'l':'qL', 'n':'q0', ':':'q0', '/':'q0'},
        'qL': {'a': 'q0', 'b': 'q0', 'h': 'qH', 't':'qT1', 'p':'q0', 'e':'qE', 'l':'q0', 'n':'qN', ':':'q0', '/':'q0'},
        'qN': {'a': 'q0', 'b': 'q0', 'h': 'qH', 't':'qT1', 'p':'q0', 'e':'qE2', 'l':'q0', 'n':'qN', ':':'q0', '/':'q0'},
        'qE2': {'a': 'q0', 'b': 'q0', 'h': 'qH', 't':'qT2', 'p':'q0', 'e':'qE2', 'l':'q0', 'n':'qN', ':':'q0', '/':'q0'},
        'qT2': {'a': 'q0', 'b': 'q0', 'h': 'qH', 't':'qT1', 'p':'q0', 'e':'qE', 'l':'q0', 'n':'q0', ':':'qCOLON', '/':'q0'},
        'qCOLON': {'a': 'q0', 'b': 'q0', 'h': 'qH', 't':'qT1', 'p':'q0', 'e':'qE', 'l':'q0', 'n':'q0', ':':'q0', '/':'qSLASH'},
        'qSLASH': {'a': 'q0', 'b': 'q0', 'h': 'qH', 't':'qT1', 'p':'q0', 'e':'qE', 'l':'q0', 'n':'q0', ':':'q0', '/':'qF'},
    },
    initial_state='q0',
    final_states={'q0', 'qF'}
)
# ahttpb = [a, http, b]
# htttp = [h, t, t, t, p]
# http = [http]
# hhttp = [h, http]
# haha = [h, a, h, a]
# httpp = [http, p]
try:
    while True:
        tokens = []
        user_input = input('Please enter your input: ')
        current_state = 'q0'
        current_token = ''
        for symbol in user_input:
            print("Currently reading: " + symbol)
            if symbol in dfa.input_symbols:
                next_state = dfa.transitions[current_state].get(symbol)
                print("Current state: " + current_state)
                print("Next state: " + next_state)
                
            if next_state is not None:

                if current_state == 'q0' and next_state in ['qH', 'qT', 'qT1'] or current_state == next_state:
                    if current_token:
                        for i in current_token:
                            tokens.append(i)

                    current_token = ''
                current_state = next_state
                #if current_state == 'qH':
                    # Ked sme v stave qH tak vycistime vsetko, co sme mali predtym
                    # Napriklad case ked pride hhttp, aby sme mali = [h, http]
                #    if current_token:
                #        for i in current_token:
                #            tokens.append(i)
                #        current_token = ''
                    # Ked sme vycistili co to bolo, zacneme citat "http"
                #    for i in current_token:
                #        tokens.append(i)
                #        current_token = ''

                # Cistime v oboch stavoch qT a qT1 ak by sme chceli citat telnet
                # tento kod potom upracem 
                #elif current_state == 'qT' or current_state == 'qT1':
                    # actually nemozeme lebo si pokazime ak citame http 
                #    if current_token:
                #        for i in current_token:
                #            tokens.append(i)
                #        current_token = ''
                    # Ked sme vycistili co to bolo, zacneme citat telnet
                #    for i in current_token:
                #        tokens.append(i)
                #    current_token = ''

                #if current_state == 'qP':
                    # sme v stave qP - precitali sme http 
                    # Ulozime token a vycistime 
                  #  current_token += symbol
                  #  print("We found http token")
                  #  tokens.append(current_token)
                 #   print(tokens)
                 #   print("---------")
                 #   current_token = ''
                if current_state == 'qF':
                    # Precitali sme telnet 
                    current_token += symbol
                    print("We found fancy token")
                    print(current_token)
                    tokens.append(current_token)
                    print(tokens)
                    print("---------")
                    current_token = ''
                else:
                    # Ak sme niekde inde, tak len pridame symbol do tokenu
                    current_token += symbol
                    print("Appending token...")
                    print(current_token)
        if current_token:
            # Ak sme skoncili citat a mame nejaky token, tak ho pridame do zoznamu
            for i in current_token:
                tokens.append(i)
        print(tokens)
        # Ak sme skoncili a mame finalny stav, akceptujeme vstup 
        # Toto este trochu nefunguje dobre lebo som sa stratila :D 
        if current_state in dfa.final_states:
            print("Accepted")
        else:
            print("Rejected")

        #if dfa.accepts_input(input('Please enter your input: ')):
            # 
        #    print('Accepted')
            # ak to reachne nejaky stav (http) chcem si to ulozit ako token a pokracovat dalej v citani 
            # basically urcite stavy (resp. finalne) predstavuju precitany token 
        #else:
        #    print('Rejected')
except KeyboardInterrupt:
    print('')