from collections import deque

from pravidla import * 

stack = deque()

start = 'url'

stack.append('Z0') # spodok zasobnika
stack.append(start) # startovaci symbol

# input string: http://google.com
input_tokens = ['http://', 'g', 'o', 'o', 'g', 'l', 'e', '.', 'com']

def parse(input_tokens):
    while stack:
        print("Current stack: " + str(stack))

        top = stack.pop()
        print("Current top: " + top)

        # ktory token prave citame zo vstupu:
        current_token = input_tokens.pop(0)
        print(current_token)
        # get teminal symbol from the token use terminals_symbols dictionary 
        symbol = terminals_symbols[current_token]
        print(symbol)

        # connect top + current token with the parsing table to get the rule number 
        rule_number = parsing_table[top][symbol]
        print(rule_number)
        # get the rule from the rules dictionary
        rule = rules[rule_number-1]
        print(rule)
        # push rule to the stack in reverse order
        for symbol in (rule):
            stack.append(symbol)
        
        # if we reach the end of the input string and the stack is empty, we are done
        if not stack and not input_tokens:
            print("Accept")
            break

        # push the rule to the stack
        #for symbol in reversed(rules[rule]):
        #    stack.append(symbol)


parse(input_tokens)