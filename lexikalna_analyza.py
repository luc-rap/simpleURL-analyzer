# pip install automata-lib
from automata.fa.dfa import DFA

examples_correct = {
    0: 'http://google',
    1: 'http://google.com',
    2: 'http://123sj.sk/path/file?search+hello',
    3: 'ftp://lucien@vanhohenheim.fr/islands',
    4: 'ftp://lucien:password@hostport/why',
    5: 'http://fiit.stuba.sk',
    6: 'telnet://lucia:password@gmail.com',
    12: 'mailto::sofia@shatokhina',
    7: 'mailto::lucia@rapanova.com',
    8: 'http://abc.abc/whatever/whatever?hladanie+hladanie+zase',
    9: 'http://youtu.be/dQw4w9WgXcQ',
    10: 'http://hostname:12345',
    11: 'telnet://lucien:password@vanhohenheim:13111988',
    13: 'http://softverovejazyky:2324/su/najlepsi/predmet/na/svete/frfr'
}

examples_wrong_lexical = {
    0: 'http:/',
    1: 'http:/google.com',
    2: 'akjsdkfj',
    3: '°˖✧◝(⁰▿⁰)◜✧˖° ٩(｡•́‿•̀｡)۶ *:･ﾟ✧',   
    4: 'telnet::lucien'
}

examples_wrong_syntax = {
    0: 'http://google.',
    1: 'mailto::lucien',
    2: 'telnet://vanhohenheim',
    3: 'http://website.com?search/wrongorder',
    4: 'ftp://lucien:@hostport',
    5: 'ftp://lucien:password',
    6: 'http://hostname:port',
    7: 'ftp://:lucien@gmail.com',
    8: 'telnet://lucien:password@vanhoheinheim:1311.1988',
    9: 'ftp://cantsearchthis.com/donttrythisathome?howtopassschoolandnotpassaway',
    10: 'ftp://lucien@vanhohenheim.fr/islands/',
    11: 'ftp://lucien:password@hostport'
}


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

# todo: zotavenie 1 == odstranenie chybneho znaku (break -> continue)
# todo: zotavenie 2 == doplnenie chybajuceho znaku (http:/google.com -> http://google.com)
# todo: vypinac / zapinac zotaveni
# todo: break out of the loop immediately when we stumble upon qZly (so it doesn't run til the end of the string)


def tokenize(user_input, dfa, recovery_mode=None):
    if recovery_mode:
        print("Zotavovanie z chyb je zapnute")
        print(recovery_mode)
    else:
        print("Zotavovanie z chyb je vypnute")
    tokens = []
    #user_input = int(input('Please enter the example id: '))
    #user_input = examples_correct[user_input]
    current_state = 'q0'
    current_token = ''
    for symbol in user_input:
        print("Currently reading: " + symbol)
        if symbol in dfa.input_symbols:
            next_state = dfa.transitions[current_state].get(symbol)
            print("Current state: " + current_state)
            print("Next state: " + next_state)
        else:
            #if current_token != '':
            #    tokens.append(current_token)

            print("Invalid symbol found: " + symbol)
            if recovery_mode == "ignore":
                print("Skipping incorrect symbol...")
                print(f"Tokens: {tokens}")
                continue
            else:
                next_state = None
                current_state = 'qZly'
                print("Rejected")
                print(f"Tokens: {tokens}")
                break
            
        if next_state is not None: # kym stale citame vstup 

            if next_state != 'qA': # citame protokol az kym nenarazime na qA
                print(f"next state: {current_state} --- Appendujeme")
                current_token += symbol # znaky protokolu appendujeme do current_token
                print(current_token)
            
            if current_state in ['qCOLONmailto', 'qSLASH'] and next_state == 'qA': # precitali sme protokol, znaky ulozime ako jeden token
                print("Precitali sme protokol")
                current_token += symbol
                tokens.append(current_token) 
                print(f"Tokens: {tokens}")
                current_token = ''
            
            # error recovery mode 2 - insert pridanie chybajuce znaku do protocolu
            # ak sme v qCOLON a next je qZLY, tak pridame / a pokracujeme... nieco na ten styl? 
            # if recovery_mode == "insert":
            #   pass 
        
            elif next_state == 'qA': # uz sme precitali protokol a uz len citame jednotlive znaky a ukladame ich po jednom ako tokeny 
                print("next_state == qA, Tokenizujeme")
                tokens.append(symbol)
                print(f"Tokens: {tokens}")
                current_token = ''
    
        current_state = next_state
            
    if current_state in ['qA']: # ak nemame dalsie znaky na vstupe a sme vo finalnom stave, tak sme skoncili a akceptujeme vstup ako spravny 
        print(f"Input akceptovany - current_state == {current_state}")
        return tokens
    
    else:
        print("Input redžektovaný :(")
        return None
    
                
