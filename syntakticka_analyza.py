from collections import deque
from pravidla import * 

examples_wrong_syntax = {
    0: ['http://', 'g', 'o', 'o', 'g', 'l', 'e', '.'],
    1: ['mailto::', 'l', 'u', 'c', 'i', 'e', 'n'],
    2: ['telnet:/', 'v', 'a', 'n', 'h', 'o', 'h', 'e', 'n', 'h', 'e', 'i', 'm'],
    3: ['http://', '1', '2', '3', 's', 'j', '.', 's', 'k', '/', 'p', 'a', 't', 'h', '/', 'f', 'i', 'l', 'e', '?', 's', 'e', 'a', 'r', 'c', 'h', '+', 'h', 'e', 'l', 'l', 'o'],
    4: ['telnet://', 'l', 'u', 'c', 'i', 'e', 'n', ':', 'p', 'a', 's', 's', 'w', 'o', 'r', 'd', '@', 'v', 'a', 'n', 'h', 'o', 'h', 'e', 'n', 'h', 'e', 'i', 'm', ':', '1', '3', '1', '1', '1', '9', '8', '8'],
    5: ['ftp://', 'l', 'u', 'c', 'i', 'e', 'n', '@', 'v', 'a', 'n', 'h', 'o', 'h', 'e', 'n', 'h', 'e', 'i', 'm', '.', 'f', 'r', '/', 'i', 's', 'l', 'a', 'n', 'd', 's'],
    6: ['ftp://', 'l', 'u', 'c', 'i', 'e', 'n', ':', 'p', 'a', 's', 's', 'w', 'o', 'r', 'd', '@', 'h', 'o', 's', 't', 'p', 'o', 'r', 't', '/'] ,
    7: ['mailto::', 'l', 'u', 'c', 'i', 'a', '@', 'r', 'a', 'p', 'a', 'n', 'o', 'v', 'a', '.', 'c', 'o', 'm']
}


# input_tokens = examples_wrong_syntax[int(input('Please enter the input tokens id: '))]

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
    

def parse(input_tokens, recovery_mode=None):
    if recovery_mode:
        print("Zotavovanie z chyb je zapnute")
        print(recovery_mode)
    else:
        print("Zotavovanie z chyb je vypnute")
    stack = deque()
    start = 'url'
    stack.append('Z0') # spodok zasobnika
    stack.append(start) # startovaci symbol

    input_tokens.append('$')
    current_token = input_tokens.pop(0)  # ktory token prave citame zo vstupu:

    accepted_tokens = []
    accepted_tokens.append(current_token)

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
                accepted_tokens.append(current_token)
                current_token = input_tokens.pop(0)
                print(f'accepted tokens: {accepted_tokens} -----------')
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
        # if rule_number = parsing_table[top][token] doesn't exist, it means the input is invalid
        if top not in parsing_table or token not in parsing_table[top]:
            # ! ERROR RECOVERY MODE 3 - skip characters unti
            if recovery_mode == 'panic':
                print('we panic')
                    
                while token not in parsing_table[top] and input_tokens:
                    print(f'RECOVERY BEFORE - token - {token} / current - {current_token} / input tokens: {input_tokens}')
                    current_token = input_tokens.pop(0)
                    token = get_terminal(current_token)
                    print(f'RECOVERY AFTER - token - {token} / current - {current_token} / input tokens: {input_tokens}')
            
            if not recovery_mode or not input_tokens:
                print(f'input tokens {input_tokens}')
                print('Rejected')
                print(f'Rule was not found in the parsing table\nTop: {top} --- Token: {token} --- Stack: {str(stack)}')
                break
        
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
    else:
        # todo: ? remove $ from accepted_tokens
        print(f'Accepted tokens: {accepted_tokens}')

    print(f'we\'re at the end of the function yay yippee')
    