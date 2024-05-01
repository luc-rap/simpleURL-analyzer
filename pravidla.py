terminals_symbols = {
    "http://": "http",
    "ftp://": "ftp",
    "telnet://": "telnet",
    "mailto::": "mailto",
    "/": "slash",
    "?": "qmark",
    "@": "at",
    ".": "dot",
    ":": "colon",
    "+": "plus"
}

terminals_alpha = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
                   "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z")

terminals_digits = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")



non_terminals = ("url", "httpaddress", "ftpaddress", "telnetaddress", "mailtoaddress", "hostport", "httpaddr_1")

rules = [
    ["httpaddress"], # 1
    ["ftpaddress "], # 2
    ["telnetaddress"], # 3
    ["mailtoaddress"], # 4
    ["http hostport httpaddr_1"], # 5
    ["slash path httpaddr_2"], # 6
    ["qmark search"], # 7
    ["eps"], # 8
    ["qmark search"], # 9
    ["eps"], # 10
    ["ftp login slash path"], # 11
    ["telnet login"], # 12
    ["mailto xalphas at hostname"], # 13
    ["user login_1"], # 14
    ["colon password at hostport"], # 15
    ["at hostport"], # 16
    ["hostname hostport_1"], # 17
    ["colon port"], # 18
    ["eps"], # 19
    ["xalphas hostname_1"], # 20
    ["dot hostname"], # 21
    ["eps"], # 22
    ["digits"], # 23
    ["segment path_1"], # 24
    ["slash path"], # 25
    ["eps"], # 26
    ["xalphas search_1"], # 27
    ["plus search"], # 28 
    ["eps"], # 29
    ["xalphas"], # 30
    ["xalphas"], # 31
    ["xalpha segment"], # 32
    ["eps"], # 33
    ["xalpha xalphas_1"], # 34
    ["xalphas"], # 35 
    ["eps"], # 36
    ["alpha"], # 37
    ["digit"], # 38
    ["digit digits_1"], # 39
    ["digits"], # 40
    ["eps"], # 41
    terminals_alpha, # 42
    terminals_digits # 43

]

parsing_table = {
    "url": {"http": 1, "ftp": 2, "telnet": 3, "mailto": 4},
    "httpaddress": {"http": 5},
    "httpaddr_1": {"slash": 6, "qmark": 7, "$": 8},
    "httpaddr_2": {"qmark": 9, "$": 10},
    "ftpaddress": {"ftp": 11},
    "telnetaddress": {"telnet": 12},
    "mailtoaddress": {"mailto": 13},
    "login": {'letter': 14, 'number': 14},
    "login_1": {"colon": 15, "at": 16},
    "hostport": {'letter': 17, 'number': 17},
    "hostport_1": {"colon": 18, "slash": 19, "qmark": 19, "$": 19},
    "hostname": {'letter': 20, 'number': 20},
    "hostname_1": {"slash": 22, "qmark": 22, "colon": 22, "dot": 21, "$": 22},
    "port": {'number': 23},
    "path": {"slash": 24, "qmark": 24, 'letter': 24, 'number': 24, "$": 24},
    "path_1": {"slash": 25, "qmark": 26, "$": 26},
    "search": {'letter': 27, 'number': 27},
    "search_1": {"plus": 28, "$": 29},
    "user": {'letter': 30, 'number': 30},
    "password": {'letter': 31, 'number': 31},
    "segment": {'letter': 32, 'number': 32, "slash": 33, "qmark": 33, "$": 33},
    "xalphas": {'letter': 34, 'number': 34},
    "xalphas_1": {"slash": 36, "qmark": 36, "plus": 36, "colon": 36, "at": 36, "dot": 36, "$": 36, 'letter': 35, 'number': 35},
    "xalpha": {'letter': 37, 'number': 38},
    "digits": {'number': 39},
    "digits_1": {'number': 40, "$": 41, "slash": 41, "qmark": 41},
    "alpha": {'letter': 42},
    "digit": {'number': 43}

}

# terminals_alpha -> letter
# terminals_digits -> number