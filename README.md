# Lexical and Syntax Analyzer simpleURL

### Software Languages FIIT STU, Summer Semester 2023/2024

### Authors: Lucia Rapánová, Sofia Shatokhina 

````
usage: main.py [-h] [-lex LEXICAL_ANALYSIS_RECOVERY] [-syn SYNTAX_ANALYSIS_RECOVERY] [-f FILE_NAME_TREE] [-v]

options:
  -h, --help            show this help message and exit
  -lex LEXICAL_ANALYSIS_RECOVERY, --lexical_analysis_recovery LEXICAL_ANALYSIS_RECOVERY
                        Choose Lexical Analysis Method 0: No recovery, 1: Skip incorrect symbols, 2: Insert expected symbols
  -syn SYNTAX_ANALYSIS_RECOVERY, --syntax_analysis_recovery SYNTAX_ANALYSIS_RECOVERY
                        Choose Syntax Analysis Method 0: No recovery, 3: Panic Mode Recovery, 4: Phrase Level Recovery
  -f FILE_NAME_TREE, --file_name_tree FILE_NAME_TREE
                        Enter the name of the file where to save the syntax tree graphviz visualization code (a new file will be created). If    
                        no name provided, graphviz visualization omitted.
  -v, --verbose         Verbose Mode
````

Program launch example:
````
main.py -lex 1 -syn 0 -f syntax_tree_data - v
````

Functions: 
1. `rules.py` contains a list of terminal and non-terminal symbols, a table of transitions and a list of rules. We used a dictionary data structure to represent the parsing table 
2. `syntax_analysis.py` uses stack for lexical analysis
3. `lexical_analysis.py` uses DFA for tokenization
4. `main.py` is used to run the main program
