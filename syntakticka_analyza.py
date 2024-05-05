from collections import deque

from pravidla import * 

stack = deque()

start = 'url'

stack.append('Z0') # spodok zasobnika
stack.append(start) # startovaci symbol

# input string: http://google.com
input_tokens = ['http://', 'google', '.', 'com']

def parse(input_tokens):
    print("Current stack: " + str(stack))

    top = stack.pop()
    print("Current top: " + top)

    # ktory token prave citame zo vstupu: ['http://', 'google', '.', 'com'] <- 4 tokeny
    current_token = input_tokens.pop(0)
    print(current_token)

    while stack:
        print("Current token at the beginning of while loop")
        print(current_token)
        # get teminal symbol from the token use terminals_symbols dictionary 
        if current_token in terminals_symbols or current_token in terminals_alpha or current_token in terminals_digits:
            if current_token in terminals_symbols:
                symbol = terminals_symbols[current_token] # musime ho prelozit na token ktory mame v pravidlach http:// -> http 
            else:
                symbol = current_token
            print(symbol) # symbol je teda current token
        else:
            pass # TBD ?? 

        #  elif current_token in non_terminals:
            #symbol = current_token
            #print(symbol)

        if top == symbol: # ak na vstupe je to iste ako na vrchu zasobnika, tak popujeme a posuvame sa dalej v citani vstupu 
            print("Match")
            # pop top from the stack
            top = stack.pop()
            print("Current top: " + top)
            print("Current stack: " + str(stack))

            # posuvame sa len ked na vrchu zasobnika je taky isty symbol ako prave citame zo vstupu 
            if input_tokens: # ak je nieco na vstupe 
                current_token = input_tokens.pop(0) # citaj dalsi token zo vstupu 
                print(current_token)
                symbol = current_token
            else:
                break
            # connect top + current token with the parsing table to get the rule number 
        print(top, symbol)

        if top == 'eps': # ked na vrchu iba eps tak popujeme a ideme dalej
            print("Skipping...")
            # pop top from the stack
            top = stack.pop()
            print("Current top: " + top)
            print("Current stack: " + str(stack))

            if top == 'Z0':
          # ~ TBD lebo toto je este zle :D dolar tam nema ostat uz je vela hodin sleepy tired brain
                print(input_tokens)
                # if we popped and z0 is on top and input_tokens is dollar, we are done
                if input_tokens == ['$']:
                    print("Accepted")
                    break
                else:
                    print("Something went terribly wrong?")

        if current_token in terminals_symbols or current_token in terminals_alpha or current_token in terminals_digits: # viem ze toto je znovu ale este sa zamyslim nad tym 
            if current_token in terminals_symbols:
                symbol = terminals_symbols[current_token]
            else:
                symbol = current_token
            print(symbol)
        if symbol in terminals_alpha:
            token = "letter" # si to "prekodujeme" aby sme nemuseli kazde jedno cislo alebo pismenko zapisovat
        elif symbol in terminals_digits:
            token = "number"
        else:
            token = symbol
        print(top, token)
        rule_number = parsing_table[top][token] # az tu actually citame pravidlo z tabulky 
        print(rule_number)
        # get the rule from the rules dictionary
        rule = rules[rule_number-1] # kvoli tomu ze tabulka je cislovana od nuly a pravidla od jednotky
        if rule == terminals_alpha or rule == terminals_digits: # ak je to len pravidlo 42 a 43 tak to appendujeme do zasobnika
            print("ahaha")
            stack.append(symbol)
            print("Current stack: " + str(stack))
        else:
        # rule 42 su vsetky pismenka, nechceme tento rule appendovat do zasobniku, chceme appendnut iba symbol (ak je token letter)
            rule = rule[0].split()
            print(rule)

            print(rule[0])
            # push rule to stack from last to first
            # ak je to ine pravidlo tak zapisujeme ho do zasobnika od konca napr ["http hostport httpaddr_1"] -> ["httpaddr_1", "hostport", "http"] 
            for rule in rule[::-1]:
                stack.append(rule)
            print("Current stack: " + str(stack))
        top = stack.pop()
        print(top)

    # if we reach the end of the input string and the stack is empty, we are done

    # ked to docita potom idu este dolare a malo by to byt tak ze sa to uz len dopopuje
    # $ hostname - > rule 22 -> eps -> pop 

        if not input_tokens:
            input_tokens.append('$')
    
    # if we reached end of input but stack is not empty - reject the input
    if not input_tokens and stack:
        print("Rejected")
    
    # if we reach bottom of the stack (Z0) and input is empty, we are done

        # push the rule to the stack
        #for symbol in reversed(rules[rule]):
        #    stack.append(symbol)


parse(input_tokens)