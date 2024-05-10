# pip install automata-lib
from automata.fa.dfa import DFA
import logging as log


dfa = DFA(
    states={ 
        'qZly', 'q0', 'qCOLON', 'qCOLONmailto', 'qSLASH', 'qA',
        'qH1', 'qH2', 'qH3', 'qH4',
        'qT1', 'qT2', 'qT3', 'qT4', 'qT5', 'qT6', 
        'qM1', 'qM2', 'qM3', 'qM4', 'qM5', 'qM6', 
        'qF1', 'qF2', 'qF3'
    },
    input_symbols={
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
        '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
        '/', '?', '@', ':', '.', '+'
    },
    transitions={
        'q0': {
            'A':'qZly', 'B':'qZly', 'C':'qZly', 'D':'qZly', 'E':'qZly', 'F':'qZly', 'G':'qZly', 'H':'qZly', 'I':'qZly', 'J':'qZly', 'K':'qZly', 'L':'qZly', 'M':'qZly', 'N':'qZly', 'O':'qZly', 'P':'qZly', 'Q':'qZly', 'R':'qZly', 'S':'qZly', 'T':'qZly', 'U':'qZly', 'V':'qZly', 'W':'qZly', 'X':'qZly', 'Y':'qZly', 'Z':'qZly', 
            'b':'qZly', 'c':'qZly', 'd':'qZly', 'g':'qZly', 'j':'qZly', 'k':'qZly', 'q':'qZly', 'r':'qZly', 's':'qZly', 'u':'qZly', 'v':'qZly', 'w':'qZly', 'x':'qZly', 'y':'qZly', 'z':'qZly',
            '0':'qZly', '1':'qZly', '2':'qZly', '3':'qZly', '4':'qZly', '5':'qZly', '6':'qZly', '7':'qZly', '8':'qZly', '9':'qZly',
            '/':'qZly', '?':'qZly', '@':'qZly', ':':'qZly', '.':'qZly', '+':'qZly',
            'h': 'qH1', 'f': 'qF1', 't': 'qT1', 'm': 'qM1', 'p': 'qZly', 'e':'qZly', 'l':'qZly', 'n':'qZly', 'a':'qZly', 'i':'qZly', 'o':'qZly',  
        },

        'qZly': {
            'A':'qZly', 'B':'qZly', 'C':'qZly', 'D':'qZly', 'E':'qZly', 'F':'qZly', 'G':'qZly', 'H':'qZly', 'I':'qZly', 'J':'qZly', 'K':'qZly', 'L':'qZly', 'M':'qZly', 'N':'qZly', 'O':'qZly', 'P':'qZly', 'Q':'qZly', 'R':'qZly', 'S':'qZly', 'T':'qZly', 'U':'qZly', 'V':'qZly', 'W':'qZly', 'X':'qZly', 'Y':'qZly', 'Z':'qZly', 
            'b':'qZly', 'c':'qZly', 'd':'qZly', 'g':'qZly', 'j':'qZly', 'k':'qZly', 'q':'qZly', 'r':'qZly', 's':'qZly', 'u':'qZly', 'v':'qZly', 'w':'qZly', 'x':'qZly', 'y':'qZly', 'z':'qZly',
            '0':'qZly', '1':'qZly', '2':'qZly', '3':'qZly', '4':'qZly', '5':'qZly', '6':'qZly', '7':'qZly', '8':'qZly', '9':'qZly',
            '/':'qZly', '?':'qZly', '@':'qZly', ':':'qZly', '.':'qZly', '+':'qZly',
            'h': 'qZly', 'f': 'qZly', 't': 'qZly', 'm': 'qZly', 'p': 'qZly', 'e':'qZly', 'l':'qZly', 'n':'qZly', 'a':'qZly', 'i':'qZly', 'o':'qZly',  
        }, 
        'qCOLON': {
            'A':'qZly', 'B':'qZly', 'C':'qZly', 'D':'qZly', 'E':'qZly', 'F':'qZly', 'G':'qZly', 'H':'qZly', 'I':'qZly', 'J':'qZly', 'K':'qZly', 'L':'qZly', 'M':'qZly', 'N':'qZly', 'O':'qZly', 'P':'qZly', 'Q':'qZly', 'R':'qZly', 'S':'qZly', 'T':'qZly', 'U':'qZly', 'V':'qZly', 'W':'qZly', 'X':'qZly', 'Y':'qZly', 'Z':'qZly', 
            'b':'qZly', 'c':'qZly', 'd':'qZly', 'g':'qZly', 'j':'qZly', 'k':'qZly', 'q':'qZly', 'r':'qZly', 's':'qZly', 'u':'qZly', 'v':'qZly', 'w':'qZly', 'x':'qZly', 'y':'qZly', 'z':'qZly',
            '0':'qZly', '1':'qZly', '2':'qZly', '3':'qZly', '4':'qZly', '5':'qZly', '6':'qZly', '7':'qZly', '8':'qZly', '9':'qZly',
            '/':'qSLASH', '?':'qZly', '@':'qZly', ':':'qZly', '.':'qZly', '+':'qZly',
            'h': 'qZly', 'f': 'qZly', 't': 'qZly', 'm': 'qZly', 'p': 'qZly', 'e':'qZly', 'l':'qZly', 'n':'qZly', 'a':'qZly', 'i':'qZly', 'o':'qZly',  
        },
        'qCOLONmailto': {
            'A':'qZly', 'B':'qZly', 'C':'qZly', 'D':'qZly', 'E':'qZly', 'F':'qZly', 'G':'qZly', 'H':'qZly', 'I':'qZly', 'J':'qZly', 'K':'qZly', 'L':'qZly', 'M':'qZly', 'N':'qZly', 'O':'qZly', 'P':'qZly', 'Q':'qZly', 'R':'qZly', 'S':'qZly', 'T':'qZly', 'U':'qZly', 'V':'qZly', 'W':'qZly', 'X':'qZly', 'Y':'qZly', 'Z':'qZly', 
            'b':'qZly', 'c':'qZly', 'd':'qZly', 'g':'qZly', 'j':'qZly', 'k':'qZly', 'q':'qZly', 'r':'qZly', 's':'qZly', 'u':'qZly', 'v':'qZly', 'w':'qZly', 'x':'qZly', 'y':'qZly', 'z':'qZly',
            '0':'qZly', '1':'qZly', '2':'qZly', '3':'qZly', '4':'qZly', '5':'qZly', '6':'qZly', '7':'qZly', '8':'qZly', '9':'qZly',
            '/':'qZly', '?':'qZly', '@':'qZly', ':':'qA', '.':'qZly', '+':'qZly',
            'h': 'qZly', 'f': 'qZly', 't': 'qZly', 'm': 'qZly', 'p': 'qZly', 'e':'qZly', 'l':'qZly', 'n':'qZly', 'a':'qZly', 'i':'qZly', 'o':'qZly',  
        },
        'qSLASH': {
            'A':'qZly', 'B':'qZly', 'C':'qZly', 'D':'qZly', 'E':'qZly', 'F':'qZly', 'G':'qZly', 'H':'qZly', 'I':'qZly', 'J':'qZly', 'K':'qZly', 'L':'qZly', 'M':'qZly', 'N':'qZly', 'O':'qZly', 'P':'qZly', 'Q':'qZly', 'R':'qZly', 'S':'qZly', 'T':'qZly', 'U':'qZly', 'V':'qZly', 'W':'qZly', 'X':'qZly', 'Y':'qZly', 'Z':'qZly', 
            'b':'qZly', 'c':'qZly', 'd':'qZly', 'g':'qZly', 'j':'qZly', 'k':'qZly', 'q':'qZly', 'r':'qZly', 's':'qZly', 'u':'qZly', 'v':'qZly', 'w':'qZly', 'x':'qZly', 'y':'qZly', 'z':'qZly',
            '0':'qZly', '1':'qZly', '2':'qZly', '3':'qZly', '4':'qZly', '5':'qZly', '6':'qZly', '7':'qZly', '8':'qZly', '9':'qZly',
            '/':'qA', '?':'qZly', '@':'qZly', ':':'qZly', '.':'qZly', '+':'qZly',
            'h': 'qZly', 'f': 'qZly', 't': 'qZly', 'm': 'qZly', 'p': 'qZly', 'e':'qZly', 'l':'qZly', 'n':'qZly', 'a':'qZly', 'i':'qZly', 'o':'qZly',  
        },
        'qA': {
            'A':'qA', 'B':'qA', 'C':'qA', 'D':'qA', 'E':'qA', 'F':'qA', 'G':'qA', 'H':'qA', 'I':'qA', 'J':'qA', 'K':'qA', 'L':'qA', 'M':'qA', 'N':'qA', 'O':'qA', 'P':'qA', 'Q':'qA', 'R':'qA', 'S':'qA', 'T':'qA', 'U':'qA', 'V':'qA', 'W':'qA', 'X':'qA', 'Y':'qA', 'Z':'qA', 
            'b':'qA', 'c':'qA', 'd':'qA', 'g':'qA', 'j':'qA', 'k':'qA', 'q':'qA', 'r':'qA', 's':'qA', 'u':'qA', 'v':'qA', 'w':'qA', 'x':'qA', 'y':'qA', 'z':'qA',
            '0':'qA', '1':'qA', '2':'qA', '3':'qA', '4':'qA', '5':'qA', '6':'qA', '7':'qA', '8':'qA', '9':'qA',
            '/':'qA', '?':'qA', '@':'qA', ':':'qA', '.':'qA', '+':'qA',
            'h': 'qA', 'f': 'qA', 't': 'qA', 'm': 'qA', 'p': 'qA', 'e':'qA', 'l':'qA', 'n':'qA', 'a':'qA', 'i':'qA', 'o':'qA',          
        }, 

        'qH1': {
            'A':'qZly', 'B':'qZly', 'C':'qZly', 'D':'qZly', 'E':'qZly', 'F':'qZly', 'G':'qZly', 'H':'qZly', 'I':'qZly', 'J':'qZly', 'K':'qZly', 'L':'qZly', 'M':'qZly', 'N':'qZly', 'O':'qZly', 'P':'qZly', 'Q':'qZly', 'R':'qZly', 'S':'qZly', 'T':'qZly', 'U':'qZly', 'V':'qZly', 'W':'qZly', 'X':'qZly', 'Y':'qZly', 'Z':'qZly', 
            'b':'qZly', 'c':'qZly', 'd':'qZly', 'g':'qZly', 'j':'qZly', 'k':'qZly', 'q':'qZly', 'r':'qZly', 's':'qZly', 'u':'qZly', 'v':'qZly', 'w':'qZly', 'x':'qZly', 'y':'qZly', 'z':'qZly',
            '0':'qZly', '1':'qZly', '2':'qZly', '3':'qZly', '4':'qZly', '5':'qZly', '6':'qZly', '7':'qZly', '8':'qZly', '9':'qZly',
            '/':'qZly', '?':'qZly', '@':'qZly', ':':'qZly', '.':'qZly', '+':'qZly',
            'h': 'qZly', 'f': 'qZly', 't': 'qH2', 'm': 'qZly', 'p': 'qZly', 'e':'qZly', 'l':'qZly', 'n':'qZly', 'a':'qZly', 'i':'qZly', 'o':'qZly',  
        },
        'qH2': {
            'A':'qZly', 'B':'qZly', 'C':'qZly', 'D':'qZly', 'E':'qZly', 'F':'qZly', 'G':'qZly', 'H':'qZly', 'I':'qZly', 'J':'qZly', 'K':'qZly', 'L':'qZly', 'M':'qZly', 'N':'qZly', 'O':'qZly', 'P':'qZly', 'Q':'qZly', 'R':'qZly', 'S':'qZly', 'T':'qZly', 'U':'qZly', 'V':'qZly', 'W':'qZly', 'X':'qZly', 'Y':'qZly', 'Z':'qZly', 
            'b':'qZly', 'c':'qZly', 'd':'qZly', 'g':'qZly', 'j':'qZly', 'k':'qZly', 'q':'qZly', 'r':'qZly', 's':'qZly', 'u':'qZly', 'v':'qZly', 'w':'qZly', 'x':'qZly', 'y':'qZly', 'z':'qZly',
            '0':'qZly', '1':'qZly', '2':'qZly', '3':'qZly', '4':'qZly', '5':'qZly', '6':'qZly', '7':'qZly', '8':'qZly', '9':'qZly',
            '/':'qZly', '?':'qZly', '@':'qZly', ':':'qZly', '.':'qZly', '+':'qZly',
            'h': 'qZly', 'f': 'qZly', 't': 'qH3', 'm': 'qZly', 'p': 'qZly', 'e':'qZly', 'l':'qZly', 'n':'qZly', 'a':'qZly', 'i':'qZly', 'o':'qZly',  
        },
        'qH3': {
            'A':'qZly', 'B':'qZly', 'C':'qZly', 'D':'qZly', 'E':'qZly', 'F':'qZly', 'G':'qZly', 'H':'qZly', 'I':'qZly', 'J':'qZly', 'K':'qZly', 'L':'qZly', 'M':'qZly', 'N':'qZly', 'O':'qZly', 'P':'qZly', 'Q':'qZly', 'R':'qZly', 'S':'qZly', 'T':'qZly', 'U':'qZly', 'V':'qZly', 'W':'qZly', 'X':'qZly', 'Y':'qZly', 'Z':'qZly', 
            'b':'qZly', 'c':'qZly', 'd':'qZly', 'g':'qZly', 'j':'qZly', 'k':'qZly', 'q':'qZly', 'r':'qZly', 's':'qZly', 'u':'qZly', 'v':'qZly', 'w':'qZly', 'x':'qZly', 'y':'qZly', 'z':'qZly',
            '0':'qZly', '1':'qZly', '2':'qZly', '3':'qZly', '4':'qZly', '5':'qZly', '6':'qZly', '7':'qZly', '8':'qZly', '9':'qZly',
            '/':'qZly', '?':'qZly', '@':'qZly', ':':'qZly', '.':'qZly', '+':'qZly',
            'h': 'qZly', 'f': 'qZly', 't': 'qZly', 'm': 'qZly', 'p': 'qH4', 'e':'qZly', 'l':'qZly', 'n':'qZly', 'a':'qZly', 'i':'qZly', 'o':'qZly',  
        },
        'qH4': {
            'A':'qZly', 'B':'qZly', 'C':'qZly', 'D':'qZly', 'E':'qZly', 'F':'qZly', 'G':'qZly', 'H':'qZly', 'I':'qZly', 'J':'qZly', 'K':'qZly', 'L':'qZly', 'M':'qZly', 'N':'qZly', 'O':'qZly', 'P':'qZly', 'Q':'qZly', 'R':'qZly', 'S':'qZly', 'T':'qZly', 'U':'qZly', 'V':'qZly', 'W':'qZly', 'X':'qZly', 'Y':'qZly', 'Z':'qZly', 
            'b':'qZly', 'c':'qZly', 'd':'qZly', 'g':'qZly', 'j':'qZly', 'k':'qZly', 'q':'qZly', 'r':'qZly', 's':'qZly', 'u':'qZly', 'v':'qZly', 'w':'qZly', 'x':'qZly', 'y':'qZly', 'z':'qZly',
            '0':'qZly', '1':'qZly', '2':'qZly', '3':'qZly', '4':'qZly', '5':'qZly', '6':'qZly', '7':'qZly', '8':'qZly', '9':'qZly',
            '/':'qZly', '?':'qZly', '@':'qZly', ':':'qCOLON', '.':'qZly', '+':'qZly',
            'h': 'qZly', 'f': 'qZly', 't': 'qZly', 'm': 'qZly', 'p': 'qZly', 'e':'qZly', 'l':'qZly', 'n':'qZly', 'a':'qZly', 'i':'qZly', 'o':'qZly',  
        },

        'qT1': {
            'A':'qZly', 'B':'qZly', 'C':'qZly', 'D':'qZly', 'E':'qZly', 'F':'qZly', 'G':'qZly', 'H':'qZly', 'I':'qZly', 'J':'qZly', 'K':'qZly', 'L':'qZly', 'M':'qZly', 'N':'qZly', 'O':'qZly', 'P':'qZly', 'Q':'qZly', 'R':'qZly', 'S':'qZly', 'T':'qZly', 'U':'qZly', 'V':'qZly', 'W':'qZly', 'X':'qZly', 'Y':'qZly', 'Z':'qZly', 
            'b':'qZly', 'c':'qZly', 'd':'qZly', 'g':'qZly', 'j':'qZly', 'k':'qZly', 'q':'qZly', 'r':'qZly', 's':'qZly', 'u':'qZly', 'v':'qZly', 'w':'qZly', 'x':'qZly', 'y':'qZly', 'z':'qZly',
            '0':'qZly', '1':'qZly', '2':'qZly', '3':'qZly', '4':'qZly', '5':'qZly', '6':'qZly', '7':'qZly', '8':'qZly', '9':'qZly',
            '/':'qZly', '?':'qZly', '@':'qZly', ':':'qZly', '.':'qZly', '+':'qZly',
            'h': 'qZly', 'f': 'qZly', 't': 'qZly', 'm': 'qZly', 'p': 'qZly', 'e':'qT2', 'l':'qZly', 'n':'qZly', 'a':'qZly', 'i':'qZly', 'o':'qZly',      
        },
        'qT2': {
            'A':'qZly', 'B':'qZly', 'C':'qZly', 'D':'qZly', 'E':'qZly', 'F':'qZly', 'G':'qZly', 'H':'qZly', 'I':'qZly', 'J':'qZly', 'K':'qZly', 'L':'qZly', 'M':'qZly', 'N':'qZly', 'O':'qZly', 'P':'qZly', 'Q':'qZly', 'R':'qZly', 'S':'qZly', 'T':'qZly', 'U':'qZly', 'V':'qZly', 'W':'qZly', 'X':'qZly', 'Y':'qZly', 'Z':'qZly', 
            'b':'qZly', 'c':'qZly', 'd':'qZly', 'g':'qZly', 'j':'qZly', 'k':'qZly', 'q':'qZly', 'r':'qZly', 's':'qZly', 'u':'qZly', 'v':'qZly', 'w':'qZly', 'x':'qZly', 'y':'qZly', 'z':'qZly',
            '0':'qZly', '1':'qZly', '2':'qZly', '3':'qZly', '4':'qZly', '5':'qZly', '6':'qZly', '7':'qZly', '8':'qZly', '9':'qZly',
            '/':'qZly', '?':'qZly', '@':'qZly', ':':'qZly', '.':'qZly', '+':'qZly',
            'h': 'qZly', 'f': 'qZly', 't': 'qZly', 'm': 'qZly', 'p': 'qZly', 'e':'qZly', 'l':'qT3', 'n':'qZly', 'a':'qZly', 'i':'qZly', 'o':'qZly',  
        },
        'qT3': {
            'A':'qZly', 'B':'qZly', 'C':'qZly', 'D':'qZly', 'E':'qZly', 'F':'qZly', 'G':'qZly', 'H':'qZly', 'I':'qZly', 'J':'qZly', 'K':'qZly', 'L':'qZly', 'M':'qZly', 'N':'qZly', 'O':'qZly', 'P':'qZly', 'Q':'qZly', 'R':'qZly', 'S':'qZly', 'T':'qZly', 'U':'qZly', 'V':'qZly', 'W':'qZly', 'X':'qZly', 'Y':'qZly', 'Z':'qZly', 
            'b':'qZly', 'c':'qZly', 'd':'qZly', 'g':'qZly', 'j':'qZly', 'k':'qZly', 'q':'qZly', 'r':'qZly', 's':'qZly', 'u':'qZly', 'v':'qZly', 'w':'qZly', 'x':'qZly', 'y':'qZly', 'z':'qZly',
            '0':'qZly', '1':'qZly', '2':'qZly', '3':'qZly', '4':'qZly', '5':'qZly', '6':'qZly', '7':'qZly', '8':'qZly', '9':'qZly',
            '/':'qZly', '?':'qZly', '@':'qZly', ':':'qZly', '.':'qZly', '+':'qZly',
            'h': 'qZly', 'f': 'qZly', 't': 'qZly', 'm': 'qZly', 'p': 'qZly', 'e':'qZly', 'l':'qZly', 'n':'qT4', 'a':'qZly', 'i':'qZly', 'o':'qZly',  
        },
        'qT4': {
            'A':'qZly', 'B':'qZly', 'C':'qZly', 'D':'qZly', 'E':'qZly', 'F':'qZly', 'G':'qZly', 'H':'qZly', 'I':'qZly', 'J':'qZly', 'K':'qZly', 'L':'qZly', 'M':'qZly', 'N':'qZly', 'O':'qZly', 'P':'qZly', 'Q':'qZly', 'R':'qZly', 'S':'qZly', 'T':'qZly', 'U':'qZly', 'V':'qZly', 'W':'qZly', 'X':'qZly', 'Y':'qZly', 'Z':'qZly', 
            'b':'qZly', 'c':'qZly', 'd':'qZly', 'g':'qZly', 'j':'qZly', 'k':'qZly', 'q':'qZly', 'r':'qZly', 's':'qZly', 'u':'qZly', 'v':'qZly', 'w':'qZly', 'x':'qZly', 'y':'qZly', 'z':'qZly',
            '0':'qZly', '1':'qZly', '2':'qZly', '3':'qZly', '4':'qZly', '5':'qZly', '6':'qZly', '7':'qZly', '8':'qZly', '9':'qZly',
            '/':'qZly', '?':'qZly', '@':'qZly', ':':'qZly', '.':'qZly', '+':'qZly',
            'h': 'qZly', 'f': 'qZly', 't': 'qZly', 'm': 'qZly', 'p': 'qZly', 'e':'qT5', 'l':'qZly', 'n':'qZly', 'a':'qZly', 'i':'qZly', 'o':'qZly',  
        },
        'qT5': {
            'A':'qZly', 'B':'qZly', 'C':'qZly', 'D':'qZly', 'E':'qZly', 'F':'qZly', 'G':'qZly', 'H':'qZly', 'I':'qZly', 'J':'qZly', 'K':'qZly', 'L':'qZly', 'M':'qZly', 'N':'qZly', 'O':'qZly', 'P':'qZly', 'Q':'qZly', 'R':'qZly', 'S':'qZly', 'T':'qZly', 'U':'qZly', 'V':'qZly', 'W':'qZly', 'X':'qZly', 'Y':'qZly', 'Z':'qZly', 
            'b':'qZly', 'c':'qZly', 'd':'qZly', 'g':'qZly', 'j':'qZly', 'k':'qZly', 'q':'qZly', 'r':'qZly', 's':'qZly', 'u':'qZly', 'v':'qZly', 'w':'qZly', 'x':'qZly', 'y':'qZly', 'z':'qZly',
            '0':'qZly', '1':'qZly', '2':'qZly', '3':'qZly', '4':'qZly', '5':'qZly', '6':'qZly', '7':'qZly', '8':'qZly', '9':'qZly',
            '/':'qZly', '?':'qZly', '@':'qZly', ':':'qZly', '.':'qZly', '+':'qZly',
            'h': 'qZly', 'f': 'qZly', 't': 'qT6', 'm': 'qZly', 'p': 'qZly', 'e':'qZly', 'l':'qZly', 'n':'qZly', 'a':'qZly', 'i':'qZly', 'o':'qZly',  
        },
        'qT6': {
            'A':'qZly', 'B':'qZly', 'C':'qZly', 'D':'qZly', 'E':'qZly', 'F':'qZly', 'G':'qZly', 'H':'qZly', 'I':'qZly', 'J':'qZly', 'K':'qZly', 'L':'qZly', 'M':'qZly', 'N':'qZly', 'O':'qZly', 'P':'qZly', 'Q':'qZly', 'R':'qZly', 'S':'qZly', 'T':'qZly', 'U':'qZly', 'V':'qZly', 'W':'qZly', 'X':'qZly', 'Y':'qZly', 'Z':'qZly', 
            'b':'qZly', 'c':'qZly', 'd':'qZly', 'g':'qZly', 'j':'qZly', 'k':'qZly', 'q':'qZly', 'r':'qZly', 's':'qZly', 'u':'qZly', 'v':'qZly', 'w':'qZly', 'x':'qZly', 'y':'qZly', 'z':'qZly',
            '0':'qZly', '1':'qZly', '2':'qZly', '3':'qZly', '4':'qZly', '5':'qZly', '6':'qZly', '7':'qZly', '8':'qZly', '9':'qZly',
            '/':'qZly', '?':'qZly', '@':'qZly', ':':'qCOLON', '.':'qZly', '+':'qZly',
            'h': 'qZly', 'f': 'qZly', 't': 'qZly', 'm': 'qZly', 'p': 'qZly', 'e':'qZly', 'l':'qZly', 'n':'qZly', 'a':'qZly', 'i':'qZly', 'o':'qZly',  
        }, 
        
        'qM1': {
            'A':'qZly', 'B':'qZly', 'C':'qZly', 'D':'qZly', 'E':'qZly', 'F':'qZly', 'G':'qZly', 'H':'qZly', 'I':'qZly', 'J':'qZly', 'K':'qZly', 'L':'qZly', 'M':'qZly', 'N':'qZly', 'O':'qZly', 'P':'qZly', 'Q':'qZly', 'R':'qZly', 'S':'qZly', 'T':'qZly', 'U':'qZly', 'V':'qZly', 'W':'qZly', 'X':'qZly', 'Y':'qZly', 'Z':'qZly', 
            'b':'qZly', 'c':'qZly', 'd':'qZly', 'g':'qZly', 'j':'qZly', 'k':'qZly', 'q':'qZly', 'r':'qZly', 's':'qZly', 'u':'qZly', 'v':'qZly', 'w':'qZly', 'x':'qZly', 'y':'qZly', 'z':'qZly',
            '0':'qZly', '1':'qZly', '2':'qZly', '3':'qZly', '4':'qZly', '5':'qZly', '6':'qZly', '7':'qZly', '8':'qZly', '9':'qZly',
            '/':'qZly', '?':'qZly', '@':'qZly', ':':'qZly', '.':'qZly', '+':'qZly',
            'h': 'qZly', 'f': 'qZly', 't': 'qZly', 'm': 'qZly', 'p': 'qZly', 'e':'qZly', 'l':'qZly', 'n':'qZly', 'a':'qM2', 'i':'qZly', 'o':'qZly',      
        },
        'qM2': {
            'A':'qZly', 'B':'qZly', 'C':'qZly', 'D':'qZly', 'E':'qZly', 'F':'qZly', 'G':'qZly', 'H':'qZly', 'I':'qZly', 'J':'qZly', 'K':'qZly', 'L':'qZly', 'M':'qZly', 'N':'qZly', 'O':'qZly', 'P':'qZly', 'Q':'qZly', 'R':'qZly', 'S':'qZly', 'T':'qZly', 'U':'qZly', 'V':'qZly', 'W':'qZly', 'X':'qZly', 'Y':'qZly', 'Z':'qZly', 
            'b':'qZly', 'c':'qZly', 'd':'qZly', 'g':'qZly', 'j':'qZly', 'k':'qZly', 'q':'qZly', 'r':'qZly', 's':'qZly', 'u':'qZly', 'v':'qZly', 'w':'qZly', 'x':'qZly', 'y':'qZly', 'z':'qZly',
            '0':'qZly', '1':'qZly', '2':'qZly', '3':'qZly', '4':'qZly', '5':'qZly', '6':'qZly', '7':'qZly', '8':'qZly', '9':'qZly',
            '/':'qZly', '?':'qZly', '@':'qZly', ':':'qZly', '.':'qZly', '+':'qZly',
            'h': 'qZly', 'f': 'qZly', 't': 'qZly', 'm': 'qZly', 'p': 'qZly', 'e':'qZly', 'l':'qZly', 'n':'qZly', 'a':'qZly', 'i':'qM3', 'o':'qZly',  
        },
        'qM3': {
            'A':'qZly', 'B':'qZly', 'C':'qZly', 'D':'qZly', 'E':'qZly', 'F':'qZly', 'G':'qZly', 'H':'qZly', 'I':'qZly', 'J':'qZly', 'K':'qZly', 'L':'qZly', 'M':'qZly', 'N':'qZly', 'O':'qZly', 'P':'qZly', 'Q':'qZly', 'R':'qZly', 'S':'qZly', 'T':'qZly', 'U':'qZly', 'V':'qZly', 'W':'qZly', 'X':'qZly', 'Y':'qZly', 'Z':'qZly', 
            'b':'qZly', 'c':'qZly', 'd':'qZly', 'g':'qZly', 'j':'qZly', 'k':'qZly', 'q':'qZly', 'r':'qZly', 's':'qZly', 'u':'qZly', 'v':'qZly', 'w':'qZly', 'x':'qZly', 'y':'qZly', 'z':'qZly',
            '0':'qZly', '1':'qZly', '2':'qZly', '3':'qZly', '4':'qZly', '5':'qZly', '6':'qZly', '7':'qZly', '8':'qZly', '9':'qZly',
            '/':'qZly', '?':'qZly', '@':'qZly', ':':'qZly', '.':'qZly', '+':'qZly',
            'h': 'qZly', 'f': 'qZly', 't': 'qZly', 'm': 'qZly', 'p': 'qZly', 'e':'qZly', 'l':'qM4', 'n':'qZly', 'a':'qZly', 'i':'qZly', 'o':'qZly',  
        },
        'qM4': {
            'A':'qZly', 'B':'qZly', 'C':'qZly', 'D':'qZly', 'E':'qZly', 'F':'qZly', 'G':'qZly', 'H':'qZly', 'I':'qZly', 'J':'qZly', 'K':'qZly', 'L':'qZly', 'M':'qZly', 'N':'qZly', 'O':'qZly', 'P':'qZly', 'Q':'qZly', 'R':'qZly', 'S':'qZly', 'T':'qZly', 'U':'qZly', 'V':'qZly', 'W':'qZly', 'X':'qZly', 'Y':'qZly', 'Z':'qZly', 
            'b':'qZly', 'c':'qZly', 'd':'qZly', 'g':'qZly', 'j':'qZly', 'k':'qZly', 'q':'qZly', 'r':'qZly', 's':'qZly', 'u':'qZly', 'v':'qZly', 'w':'qZly', 'x':'qZly', 'y':'qZly', 'z':'qZly',
            '0':'qZly', '1':'qZly', '2':'qZly', '3':'qZly', '4':'qZly', '5':'qZly', '6':'qZly', '7':'qZly', '8':'qZly', '9':'qZly',
            '/':'qZly', '?':'qZly', '@':'qZly', ':':'qZly', '.':'qZly', '+':'qZly',
            'h': 'qZly', 'f': 'qZly', 't': 'qM5', 'm': 'qZly', 'p': 'qZly', 'e':'qZly', 'l':'qZly', 'n':'qZly', 'a':'qZly', 'i':'qZly', 'o':'qZly',  
        },
        'qM5': {
            'A':'qZly', 'B':'qZly', 'C':'qZly', 'D':'qZly', 'E':'qZly', 'F':'qZly', 'G':'qZly', 'H':'qZly', 'I':'qZly', 'J':'qZly', 'K':'qZly', 'L':'qZly', 'M':'qZly', 'N':'qZly', 'O':'qZly', 'P':'qZly', 'Q':'qZly', 'R':'qZly', 'S':'qZly', 'T':'qZly', 'U':'qZly', 'V':'qZly', 'W':'qZly', 'X':'qZly', 'Y':'qZly', 'Z':'qZly', 
            'b':'qZly', 'c':'qZly', 'd':'qZly', 'g':'qZly', 'j':'qZly', 'k':'qZly', 'q':'qZly', 'r':'qZly', 's':'qZly', 'u':'qZly', 'v':'qZly', 'w':'qZly', 'x':'qZly', 'y':'qZly', 'z':'qZly',
            '0':'qZly', '1':'qZly', '2':'qZly', '3':'qZly', '4':'qZly', '5':'qZly', '6':'qZly', '7':'qZly', '8':'qZly', '9':'qZly',
            '/':'qZly', '?':'qZly', '@':'qZly', ':':'qZly', '.':'qZly', '+':'qZly',
            'h': 'qZly', 'f': 'qZly', 't': 'qZly', 'm': 'qZly', 'p': 'qZly', 'e':'qZly', 'l':'qZly', 'n':'qZly', 'a':'qZly', 'i':'qZly', 'o':'qM6',  
        },
        'qM6': {
            'A':'qZly', 'B':'qZly', 'C':'qZly', 'D':'qZly', 'E':'qZly', 'F':'qZly', 'G':'qZly', 'H':'qZly', 'I':'qZly', 'J':'qZly', 'K':'qZly', 'L':'qZly', 'M':'qZly', 'N':'qZly', 'O':'qZly', 'P':'qZly', 'Q':'qZly', 'R':'qZly', 'S':'qZly', 'T':'qZly', 'U':'qZly', 'V':'qZly', 'W':'qZly', 'X':'qZly', 'Y':'qZly', 'Z':'qZly', 
            'b':'qZly', 'c':'qZly', 'd':'qZly', 'g':'qZly', 'j':'qZly', 'k':'qZly', 'q':'qZly', 'r':'qZly', 's':'qZly', 'u':'qZly', 'v':'qZly', 'w':'qZly', 'x':'qZly', 'y':'qZly', 'z':'qZly',
            '0':'qZly', '1':'qZly', '2':'qZly', '3':'qZly', '4':'qZly', '5':'qZly', '6':'qZly', '7':'qZly', '8':'qZly', '9':'qZly',
            '/':'qZly', '?':'qZly', '@':'qZly', ':':'qCOLONmailto', '.':'qZly', '+':'qZly',
            'h': 'qZly', 'f': 'qZly', 't': 'qZly', 'm': 'qZly', 'p': 'qZly', 'e':'qZly', 'l':'qZly', 'n':'qZly', 'a':'qZly', 'i':'qZly', 'o':'qZly',  
        }, 
        
        'qF1': {
            'A':'qZly', 'B':'qZly', 'C':'qZly', 'D':'qZly', 'E':'qZly', 'F':'qZly', 'G':'qZly', 'H':'qZly', 'I':'qZly', 'J':'qZly', 'K':'qZly', 'L':'qZly', 'M':'qZly', 'N':'qZly', 'O':'qZly', 'P':'qZly', 'Q':'qZly', 'R':'qZly', 'S':'qZly', 'T':'qZly', 'U':'qZly', 'V':'qZly', 'W':'qZly', 'X':'qZly', 'Y':'qZly', 'Z':'qZly', 
            'b':'qZly', 'c':'qZly', 'd':'qZly', 'g':'qZly', 'j':'qZly', 'k':'qZly', 'q':'qZly', 'r':'qZly', 's':'qZly', 'u':'qZly', 'v':'qZly', 'w':'qZly', 'x':'qZly', 'y':'qZly', 'z':'qZly',
            '0':'qZly', '1':'qZly', '2':'qZly', '3':'qZly', '4':'qZly', '5':'qZly', '6':'qZly', '7':'qZly', '8':'qZly', '9':'qZly',
            '/':'qZly', '?':'qZly', '@':'qZly', ':':'qZly', '.':'qZly', '+':'qZly',
            'h': 'qZly', 'f': 'qZly', 't': 'qF2', 'm': 'qZly', 'p': 'qZly', 'e':'qZly', 'l':'qZly', 'n':'qZly', 'a':'qZly', 'i':'qZly', 'o':'qZly',  
        },
        'qF2': {
            'A':'qZly', 'B':'qZly', 'C':'qZly', 'D':'qZly', 'E':'qZly', 'F':'qZly', 'G':'qZly', 'H':'qZly', 'I':'qZly', 'J':'qZly', 'K':'qZly', 'L':'qZly', 'M':'qZly', 'N':'qZly', 'O':'qZly', 'P':'qZly', 'Q':'qZly', 'R':'qZly', 'S':'qZly', 'T':'qZly', 'U':'qZly', 'V':'qZly', 'W':'qZly', 'X':'qZly', 'Y':'qZly', 'Z':'qZly', 
            'b':'qZly', 'c':'qZly', 'd':'qZly', 'g':'qZly', 'j':'qZly', 'k':'qZly', 'q':'qZly', 'r':'qZly', 's':'qZly', 'u':'qZly', 'v':'qZly', 'w':'qZly', 'x':'qZly', 'y':'qZly', 'z':'qZly',
            '0':'qZly', '1':'qZly', '2':'qZly', '3':'qZly', '4':'qZly', '5':'qZly', '6':'qZly', '7':'qZly', '8':'qZly', '9':'qZly',
            '/':'qZly', '?':'qZly', '@':'qZly', ':':'qZly', '.':'qZly', '+':'qZly',
            'h': 'qZly', 'f': 'qZly', 't': 'qZly', 'm': 'qZly', 'p': 'qF3', 'e':'qZly', 'l':'qZly', 'n':'qZly', 'a':'qZly', 'i':'qZly', 'o':'qZly',  
        
        },
        'qF3': {
            'A':'qZly', 'B':'qZly', 'C':'qZly', 'D':'qZly', 'E':'qZly', 'F':'qZly', 'G':'qZly', 'H':'qZly', 'I':'qZly', 'J':'qZly', 'K':'qZly', 'L':'qZly', 'M':'qZly', 'N':'qZly', 'O':'qZly', 'P':'qZly', 'Q':'qZly', 'R':'qZly', 'S':'qZly', 'T':'qZly', 'U':'qZly', 'V':'qZly', 'W':'qZly', 'X':'qZly', 'Y':'qZly', 'Z':'qZly', 
            'b':'qZly', 'c':'qZly', 'd':'qZly', 'g':'qZly', 'j':'qZly', 'k':'qZly', 'q':'qZly', 'r':'qZly', 's':'qZly', 'u':'qZly', 'v':'qZly', 'w':'qZly', 'x':'qZly', 'y':'qZly', 'z':'qZly',
            '0':'qZly', '1':'qZly', '2':'qZly', '3':'qZly', '4':'qZly', '5':'qZly', '6':'qZly', '7':'qZly', '8':'qZly', '9':'qZly',
            '/':'qZly', '?':'qZly', '@':'qZly', ':':'qCOLON', '.':'qZly', '+':'qZly',
            'h': 'qZly', 'f': 'qZly', 't': 'qZly', 'm': 'qZly', 'p': 'qZly', 'e':'qZly', 'l':'qZly', 'n':'qZly', 'a':'qZly', 'i':'qZly', 'o':'qZly',  
        }
    },
    initial_state='q0',
    final_states={'qA', 'qZly'}
)


def reject_input(tokens):
    log.error("Input rejected")
    log.info(f"Tokens: {tokens}")
    return None, 'qZly'  # return next_state, current_state

def tokenize(user_input, dfa, recovery_mode=None):
    if recovery_mode:
        log.info(f"Error recovery is turned on: {recovery_mode}")
    else:
        log.info("Error recovery is turned off")
        
    tokens = []
    current_state = 'q0'
    current_token = ''

    for symbol in user_input:
        log.info('\n')
        log.info(f"Currently reading: {symbol}, current_token: {current_token}")

        # check if a symbol is valid
        if symbol in dfa.input_symbols:
            next_state = dfa.transitions[current_state].get(symbol)
            log.info(f"Current state: {current_state}")
            log.info(f"Next state: {next_state}")

        else:
            log.warning("Invalid symbol found: " + symbol)

            # ! ERROR RECOVERY MODE 1 -- preskocenie chybnych znakov (nie je v input_symbols)
            if recovery_mode == "ignore":
                log.info("In error recovery mode ignore")
                log.info("Skipping incorrect symbol...")
                continue
            else:
                next_state, current_state = reject_input(tokens)
                break
            
        # check if we didn't get into an invalid state (qZly) -- kym stale citame vstup
        if next_state is not None:

            # ! ERROR RECOVERY MODE 1 -- preskocenie chybnych znakov (znaky su v input symbols, ale nie su ocakavane v protokole)
            if next_state == 'qZly':
                if recovery_mode == 'ignore':
                    continue
                elif recovery_mode == 'insert':
                    pass
                else:
                    break

            # citame protokol az kym nenarazime na qA
            if next_state != 'qA':

                # ! ERROR RECOVERY MODE 2 - insert pridanie chybajuce znaku do protocolu
                if recovery_mode == "insert":
                    while next_state == 'qZly' and current_state != None: 
                        log.info("In error recovery mode insert.\n(start of the while loop)")
                        log.info(f'symbol - {symbol} / current state = {current_state} / next_state = {next_state} / current_toekn = {current_token}')
                        if current_state == 'qM6':
                            current_token += ':'
                            current_state = 'qCOLONmailto'

                        elif current_state in ['qH4','qT6', 'qF3']:
                            current_token += ':'
                            current_state = 'qCOLON'

                        elif current_state == 'qCOLON':
                            current_token += '/'
                            current_state = 'qSLASH'

                        elif current_state == 'qCOLONmailto':
                            current_token += ':'
                            current_state = 'qA'

                        elif current_state == 'qSLASH':
                            current_token += '/'
                            current_state = 'qA'

                        else:
                            next_state, current_state = reject_input(tokens)
                            break
                        
                        next_state = dfa.transitions[current_state].get(symbol)
                        log.info(f'symbol - {symbol} / current state = {current_state} / next_state = {next_state} / current_toekn = {current_token}')
                        log.info('(end of the while loop)')

                    if next_state == 'qA':
                        tokens.append(current_token)
                    elif next_state == None:
                        break
                    else:
                        current_token += symbol

                else:
                    log.info("Appending protocol symbols")
                    log.info(f"'next state': {current_state} / next state: {next_state}")
                    current_token += symbol # znaky protokolu appendujeme do current_token
                    log.info(f'Appending: {symbol}')
                    log.info(f'Current state: {current_state}')

            # we've finished reading the protocol  
            if current_state in ['qCOLONmailto', 'qSLASH'] and next_state == 'qA': # precitali sme protokol, znaky ulozime ako jeden token
                log.info("Finished reading the protocol token")
                current_token += symbol
                tokens.append(current_token)
                log.info(f"Tokens: {tokens}")
                current_token = ''
        
            elif next_state == 'qA': # uz sme precitali protokol a uz len citame jednotlive znaky a ukladame ich po jednom ako tokeny 
                log.info("Tokenizing symbols...")
                tokens.append(symbol)
                log.info(f"Tokens: {tokens}")
                current_token = ''
    
        current_state = next_state
            
    if current_state in ['qA']: # ak nemame dalsie znaky na vstupe a sme vo finalnom stave, tak sme skoncili a akceptujeme vstup ako spravny 
        print("Input accepted")
        return tokens
    
    else:
        log.error("Input rejected")
        return None
