from collections import deque
from pravidla import * 

stack = deque()

start = 'url'

stack.append('Z0') # spodok zasobnika
stack.append(start) # startovaci symbol

input_tokens = ['http://', 'g', 'o', 'o', 'g', 'l', 'e', '.', 'c', 'o', 'm', '/']

# todo: osetrit nespravny vstup

# get teminal symbol from the token use terminals_symbols dictionary -- either a terminal or "name"
def get_terminal(current_token):
    if current_token in terminals_symbols:
        return terminals_symbols[current_token]

    # our tokens are protocols + symbols + "name"
    # protocols + symbols are in terminals_symbols (and all tokens here are valid) => the other symbol must be "name"
    elif current_token in terminals_digits:
        return 'number'
    
    elif current_token in terminals_alpha:
        return 'letter'

    elif current_token == '$':
        return '$'

    else:
        return 'something has gone horribly wrong o_o'
    

def parse(input_tokens):
    input_tokens.append('$')
    current_token = input_tokens.pop(0)  # ktory token prave citame zo vstupu:
    print(f'INITIAL INFO\nstack - {str(stack)} / token - {current_token}')

    #! current_token = ktory token prave citame zo vstupu
    #! token = aky token je to naozaj (terminals vs number vs letter)

    while stack:
        top = stack.pop()
        token = get_terminal(current_token)
        print(f'------- while begin ------- \nstack - {str(stack)} / top - {top} / current_token - {current_token} / token - {token}')

        # check until symbol on top != current token (remove the symbol on top in the meanwhile)
        # posuvame sa len ked na vrchu zasobnika je taky isty symbol (token) ako prave citame zo vstupu 
        while (top == token):
            print(f'in token == top{top, token}')
            top = stack[-1]  
            stack.pop()  # only after we know the actual top character
            print(f'Match (top == token)\n Top: {top} --- Stack: {str(stack)} --- Token: {token}')

            # read the next token from the input string
            if input_tokens:
                current_token = input_tokens.pop(0)
                token = get_terminal(current_token)
                print(f'Current token (if input tokens exist): {token}')
            else:
                break

        # eps check - if eps found, skip (pop top from the stack)
        if top == 'eps':
            top = stack.pop()
            print(f'Skipping...\n Top: {top} --- Stack: {str(stack)} --- Token: {token}')
        
        # we've reached the bottom of the stack and ran out of input tokens :)
        if top == 'Z0' and not input_tokens:
            print('Accepted :)')
            break

        # get the rule from the rules dictionary
        rule_number = parsing_table[top][token]
        rule = rules[rule_number - 1]
        print(f'RULES\nTop - {top} / Token - {token} / Rule number - {rule_number} / Rule - {rule}')

        # add a specific alphanumeric character instead of the first one of terminals_alpha or terminals_digits
        if rule == terminals_alpha or rule == terminals_digits:
            stack.append(token)

        # don't add an epsilon to stack if it's an epsilon rule
        elif rule == 'eps':
            continue

        # split the rule into mulitple strings if it's not just one
        else:
            rule = rule.split(' ')
            rule.reverse()  # reverse the rules because it's a stack
            stack.extend(rule)

        print(f'Current stack: {str(stack)}')

        
    if not input_tokens and stack:
        print("Rejected")

    print(f'we\'re at the end of the function yay yippee')
    

parse(input_tokens)