"""
SymbolTable Module for Hack Assembler
"""

def create_symbol_table():
    """Creates the symbol table with predefined symbols"""
    symbols = {}
    
    # R0-R15
    for i in range(16):
        symbols[f'R{i}'] = i
    
    # Special symbols
    symbols['SP'] = 0
    symbols['LCL'] = 1
    symbols['ARG'] = 2
    symbols['THIS'] = 3
    symbols['THAT'] = 4
    symbols['SCREEN'] = 16384
    symbols['KBD'] = 24576
    
    return symbols
