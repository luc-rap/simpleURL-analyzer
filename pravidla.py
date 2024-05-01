terminals_symbols = {
    "http": "http://",
    "ftp": "ftp://",
    "telnet": "telnet://",
    "mailto": "mailto::",
    "slash": "/",
    "qmark": "?",
    "at": "@",
    "dot": ".",
    "colon": ":",
    "plus": "+"
}

terminals_alpha = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
                   "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

terminals_digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

terminals = terminals_symbols.keys() + terminals_alpha + terminals_digits

non_terminals = ("url", "httpaddress", "ftpaddress", "telnetaddress", "mailtoaddress", "hostport", "httpaddr_1")

rules = {
    "url": ["httpaddress", "ftpaddress ", "telnetaddress", "mailtoaddress"],
    "httpaddress": ["http", "hostport", "httpaddr_1"],
    "httpaddr_1" : ["slash", "path", "httpaddr_2"],
    "httpaddr_1" : ["qmark", "search"],
    "httpaddr_1" : ["eps"],
    "httpaddr_2" : ["qmark", "search"],
    "httpaddr_2" : ["eps"],
    "ftpaddress" : ["ftp", "login", "slash", "path"],
    "telnetaddress" : ["telnet", "login"],
    "mailtoaddress" : ["mailto", "xalphas", "at", "hostname"],
    "login" : ["user", "login_1"],
    "login_1" : ["colon", "password", "at", "hostport"],
    "login_1" : ["at", "hostport"],
    "hostport" : ["hostname", "hostport_1"],
    "hostport_1" : ["colon", "port"],
    "hostport_1" : ["eps"],
    "hostname" : ["xalphas", "hostname_1"],
    "hostname_1" : ["dot", "hostname"],
    "hostname_1" : ["eps"],
    "port" : ["digits"],
    "path" : ["segment", "path_1"],
    "path_1" : ["slash", "path"],
    "path_1" : ["eps"],
    "search" : ["xalphas", "search_1"],
    "search_1" : ["plus", "search"], 
    "search_1" : ["eps"],
    "user" : ["xalphas"],
    "password" : ["xalphas"],
    "segment" : ["xalpha", "segment"],
    "segment" : ["eps"],
    "xalphas" : ["xalpha", "xalphas_1"],
    "xalphas_1" : ["xalphas"], 
    "xalphas_1" : ["eps"],
    "xalpha" : ["alpha"],
    "xalpha" : ["digit"],
    "digits" : ["digit", "digits_1"],
    "digits_1" : ["digits"],
    "digits_1" : ["eps"],
    "alpha" : terminals_alpha,
    "digit" : terminals_digits

}

parsing_table = {
    "url": {"http": 1, "ftp": 2, "telnet": 3, "mailto": 4},
    "httpaddress": {"http": 5},
    "httpaddr_1": {"slash": 6, "qmark": 7, "$": 8},
    "httpaddr_2": {"qmark": 9, "$": 10},
    "ftpaddress": {"ftp": 11},
    "telnetaddress": {"telnet": 12},
    "mailtoaddress": {"mailto": 13},
    "login": {terminals_alpha: 14},
    "login_1": {"colon": 15, "at": 16},
    "hostport": {terminals_alpha: 17, terminals_digits: 17},
    "hostport_1": {"colon": 18, "slash": 19, "qmark": 19, "$": 19},
    "hostname": {terminals_alpha: 20, terminals_digits: 20},
    "hostname_1": {"slash": 22, "qmark": 22, "colon": 22, "dot": 21, "$": 22},
    "port": {terminals_digits: 23},
    "path": {"slash": 24, "qmark": 24, terminals_alpha: 24, terminals_digits: 24, "$": 24},
    "path_1": {"slash": 25, "qmark": 26, "$": 26},
    "search": {terminals_alpha: 27, terminals_digits: 27},
    "search_1": {"plus": 28, "$": 29},
    "user": {terminals_alpha: 30, terminals_digits: 30},
    "password": {terminals_alpha: 31, terminals_digits: 31},
    "segment": {terminals_alpha: 32, terminals_digits: 32, "slash": 33, "qmark": 33, "$": 33},
    "xalphas": {terminals_alpha: 34, terminals_digits: 34},
    "xalphas_1": {"slash": 36, "qmark": 36, "plus": 36, "colon": 36, "at": 36, "dot": 36, "$": 35, terminals_alpha: 35, terminals_digits: 35},
    "xalpha": {terminals_alpha: 37, terminals_digits: 38},
    "digits": {terminals_digits: 39},
    "digits_1": {terminals_digits: 40, "$": 41, "slash": 41, "qmark": 41},
    "alpha": {terminals_alpha: 42},
    "digit": {terminals_digits: 43}

}