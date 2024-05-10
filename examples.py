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
    13: 'http://softverovejazyky:2324/su/najlepsi/predmet/na/svete/frfr',
    14: 'ftp://lucien@vanhohenheim.fr/islands/',
    15: 'ftp://username:password@ftp.example.com/',
    16: 'ftp://username:password@ftp.example.com:21',
    17: 'mailto::example@example.com',
    18: 'http://example.com/page1/page2',
    19: 'http://example.com:8080/page',
    20: 'telnet://username:password@example.com'
}

examples_wrong_lexical = {
    0: 'http:/',
    1: 'http:/google.com',
    2: 'akjsdkfj',
    3: '°˖✧◝(⁰▿⁰)◜✧˖° ٩(｡•́‿•̀｡)۶ *:･ﾟ✧',   
    4: 'telnet::lucien',
    5: 'mail@to///::lucien',
    6: 'ft*p://login',
}

examples_wrong_syntax = {
    0: 'http://google.', # rejectne lebo za bodkou musi byt aspon jeden alfanumericky znak
    1: 'mailto::lucien', # zotavenie 4 doplni @, ale stale rejected, lebo chyba alfanumer. znak. bez zotavenia chyba @ tak rejectne
    2: 'telnet://vanhohenheim', # lebo chyba login a zavinac hostport, nic to nebude recoverovat 
    3: 'http://website.com?search/wrongorder',  # 3 - accepted (skpine /wrongorder lebo caka + alebo eps), 4 - rejected, nic sa nedoplni, nevie rozpoznat /
    '3.1': 'http://w.c?s/a+b',  # zotavenie 3 preskoci slash a natrafi na + ktore vie akceptovat (cize pokracuje v citani od +), 4 rejectne, lebo nepozna /
    4: 'ftp://lucien:@hostport',  # zotavenie 3 preskoci @ (kedze ocakava password po :), docita to hostport ale rejectne, lebo chyba @hostport/
    '4.5': 'ftp://lucien:@hostport@nieco/', # zotavenie 3 preskorci @ a akceptuje vstup
    5: 'ftp://lucien:password',  # 4 doplni @, ale stale to rejectne
    6: 'http://hostname:port',  # nemozeme mat alphabeticky port
    7: 'ftp://:lucien@gmail.com', # ftp preskoci : ale chyba slash tak to stale bude zle  (3) (3 - preskoci :, chyba slash, 4 - : navyse)
    8: 'telnet://lucien:password@vanhoheinheim:1311.1988',  # :3
    9: 'ftp://cantsearchthis.com/donttrythisathome?howtopassschoolandnotpassaway', # ftp ocakava :password alebo @ bez passwordu 
    10: 'ftp://lucien@vanhohenheim.fr', # 4 - chyba slash - mozeme pridat v recovery slash 
    11: 'ftp://lucien:password@hostport', # 4 - chyba slash 
    12: 'mailto::example@example.com?subject',  # v mailto nie je ?search
    13: 'telnet://example.com:23',  # telnet potrebuje login a v logine je vzdy @hostname 
    14: 'telnet://example.com',  # tiez ako 13
    15: 'http://example.com:80:8080',  # viac portov po sebe nejde, 3 - preskoci :, port bude 808080
    16: 'http://username:password@example.com',  # v http nie je ziadny login. : to este zoberie lebo to moze ocakavat iba port (digits) 
}

examples_wrong_both = {
    1: 'fttp://lucien@vh.fr',  # znak navyse (1) + chybajuci / (4)
    2: 'htttp://google.com:abc80',  # znak navyse (1) + symboly navyse (3) (abc v porte nie su digits)
    3: 'mailto:lucia@rapanova@.com',  # doplnenie chybajuceho : (2) + skip @  navyse (pred .com) (3)
    4: 'ftp/examples@py',  # chybajuce znaky :/ (2) + chybajuci / na konci(4)
}
