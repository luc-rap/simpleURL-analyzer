from collections import deque
from pravidla import * 
import logging as log

# pip install treelib
# tree visualizer from graphviz output: https://dreampuf.github.io/
from treelib import Node, Tree


# get teminal symbol from the token using terminals_symbols dictionary -- either a terminal or "name"
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
    
    elif current_token in terminals_symbols.values():
        return current_token

    else:
        return 'something has gone horribly wrong o_o'
    

def parse(input_tokens, file_name, recovery_mode=None):
    if recovery_mode:
        log.info(f"Error recovery is turned on: {recovery_mode}")
    else:
        log.info("Error recovery is turned off")
    
    stack = deque()
    start = 'url'
    stack.append('Z0')  # spodok zasobnika
    stack.append(start)  # startovaci symbol

    syntax_tree = Tree()
    syntax_tree.add_node(Node(start, str(start) + str(parsing_table_tree_counters[start])))
    parsing_table_tree_counters[start] += 1

    input_tokens.append('$')
    current_token = input_tokens.pop(0)  # ktory token prave citame zo vstupu:

    accepted_tokens = []

    log.info(f'\nINITIAL INFO\nstack - {str(stack)} / token - {current_token}')

    # current_token = ktory token prave citame zo vstupu
    # token = aky token je to naozaj (terminals vs number vs letter)

    while stack:
        top = stack.pop()
        token = get_terminal(current_token)
        log.info('\n')
        log.info(f'Currently reading a new symbol\nstack - {str(stack)} / top - {top} / current_token - {current_token} / token - {token}')
        log.info(f'Accepted tokens: {accepted_tokens}\n Remaining tokens: {input_tokens}')
        # check until symbol on top != current token (remove the symbol on top in the meanwhile)
        # posuvame sa len ked na vrchu zasobnika je taky isty symbol (token) ako prave citame zo vstupu 
        while (top == token):
            top = stack[-1]  
            stack.pop()  # only after we know the actual top character
            log.info(f'Match (top == token)\n Top: {top} --- Stack: {str(stack)} --- Token: {token}')

            # read the next token from the input string
            if input_tokens:
                log.info("Reading next token from input")
                accepted_tokens.append(current_token)
                current_token = input_tokens.pop(0)
                token = get_terminal(current_token)
                log.info(f'Currently reading token: {token}')
            else:
                break

        # eps check - if eps found, skip (pop top from the stack)
        if top == 'eps':
            top = stack.pop()
            log.info(f'Skipping...\n Top: {top} --- Stack: {str(stack)} --- Token: {token}')

        # we've reached the bottom of the stack and ran out of input tokens :)
        if top == 'Z0' and not input_tokens:
            print('Input accepted')
            break

        # get the rule from the rules dictionary
        # if rule_number = parsing_table[top][token] doesn't exist, it means the input is invalid
        if top not in parsing_table or token not in parsing_table[top]:
            # ! ERROR RECOVERY MODE 3 - skip characters unti
            if recovery_mode == 'panic':
                log.info('In Panic Mode Recovery')
                    
                while (top not in parsing_table or token not in parsing_table[top]) and input_tokens:
                    log.info(f'BEFORE adjustments: token - {token} / current - {current_token} / input tokens: {input_tokens}')
                    log.info(f'Top: {top} --- Stack: {str(stack)}')
                    current_token = input_tokens.pop(0)
                    token = get_terminal(current_token)
                    log.info(f'AFTER adjustments: token - {token} / current - {current_token} / input tokens: {input_tokens}')
                    log.info(f'Top: {top} --- Stack: {str(stack)}')
            
            # ! ERROR RECOVERY MODE 4 - doplnenie chybajuceho znaku
            elif recovery_mode == 'phrase':
                log.info('In Phrase Mode Error Recovery')

                # ak nemame dalsi vstup (zostal nam v input_tokens iba '$')
                # a zostal nam terminal na vrchu zasobnika (napr. /) tak ten terminal doplnime
                if current_token == '$' and top in terminals_symbols.values():
                    
                    # find the actual character for the specific terminal token
                    terminals_keys = list(terminals_symbols.keys())
                    terminals_values = list(terminals_symbols.values())
                    pos = terminals_values.index(top)
                    
                    input_tokens.insert(0, terminals_keys[pos])
                    input_tokens.append('$')

                    current_token = input_tokens.pop(0) 

                    stack.append(top)
                    syntax_tree.add_node(Node(top, str(top) + str(parsing_table_tree_counters[top])), 
                                         parent=str(top) + str(parsing_table_tree_counters[top] - 1))
                    parsing_table_tree_counters[top] += 1
                    
                    log.info(f'AFTER adjustments: token - {token} / current - {current_token} / input tokens: {input_tokens}')
                    continue
            
            # if not recovery_mode or not input_tokens:
            if top not in parsing_table or token not in parsing_table[top]:
                log.error('Rejected')
                log.error(f'Rule was not found in the parsing table\nTop: {top} --- Token: {token} --- Stack: {str(stack)}')
                break
    
        rule_number = parsing_table[top][token]
        rule = rules[rule_number - 1]
        log.info(f'Parsing the RULES:\nTop - {top} / Token - {token} / Rule number - {rule_number} / Rule - {rule}')

        # add a specific alphanumeric character instead of the first one of terminals_alpha or terminals_digits
        if rule == terminals_alpha or rule == terminals_digits:
            stack.append(token)
            syntax_tree.add_node(Node(current_token), 
                                 parent=str(top) + str(parsing_table_tree_counters[top] - 1))

        # don't add an epsilon to stack if it's an epsilon rule
        elif rule == 'eps':
            syntax_tree.add_node(Node('eps'), 
                                 parent=str(top) + str(parsing_table_tree_counters[top] - 1))
            continue

        # split the rule into mulitple strings if it's not just one
        else:
            rule = rule.split(' ')
            rule.reverse()  # reverse the rules because it's a stack
            for r in rule:
                # syntax_tree.add_node((Node(r, r)), parent=top)
                syntax_tree.add_node(Node(r, str(r) + str(parsing_table_tree_counters[r])), 
                                 parent=str(top) + str(parsing_table_tree_counters[top] - 1))
                parsing_table_tree_counters[r] += 1
            stack.extend(rule)

        log.info(f'Current stack: {str(stack)}')

        
    if not input_tokens and stack:
        log.error("Input rejected")
    else:
        print(f'Accepted tokens: {accepted_tokens}')

    log.info("Finished")
    log.info(f'\n{syntax_tree.show(stdout=False)}')

    # todo: mention the ordering=out (in tree.py) in docu
    # todo: mention it's read from right to left
    if file_name:
        syntax_tree.to_graphviz(filename=file_name, shape=u'circle', graph=u'digraph')
        log.info(f'Saved syntax tree output to {file_name}')
