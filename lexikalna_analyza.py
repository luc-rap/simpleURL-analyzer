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
    states={'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7'},
    input_symbols={'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
                   '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '?', '@', '.', ':', '+', 'http://', 'ftp://', 'telnet://', 'mailto:', '/'},
    transitions={
    }
)

try:
    while True:
        if my_dfa.accepts_input(input('Please enter your input: ')):
            print('Accepted')
        else:
            print('Rejected')
except KeyboardInterrupt:
    print('')