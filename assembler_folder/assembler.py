import sys
from symbol_table import create_symbol_table
from code import DEST, COMP, JUMP
from Parser import *


def assemble(input_file):
    """Main assembly function"""
    
    # Setup
    symbols = create_symbol_table()
    output = []
    
    # Reads file
    with open(input_file, 'r') as f:
        lines = f.readlines()
    
    # Clean all lines
    clean_lines = []
    for line in lines:
        cleaned = clean_line(line)
        if cleaned:  # Skip empty lines
            clean_lines.append(cleaned)
    
    # Finds labels
    line_number = 0
    for line in clean_lines:
        cmd_type = get_command_type(line)
        
        if cmd_type == 'L':
            label = parse_l_command(line)
            symbols[label] = line_number
        else:
            line_number += 1
    
    # SECOND PASS: Generate code
    next_variable = 16
    
    for line in clean_lines:
        cmd_type = get_command_type(line)
        
        if cmd_type == 'A':
            # A-instruction
            symbol = parse_a_command(line)
            
            if symbol.isdigit():
                address = int(symbol)
            else:
                # Check if symbol exists
                if symbol not in symbols:
                    symbols[symbol] = next_variable
                    next_variable += 1
                address = symbols[symbol]
            
            # Convert to binary
            binary = format(address, '016b')
            output.append(binary)
        
        elif cmd_type == 'C':
            # C-instruction
            dest, comp, jump = parse_c_command(line)
            
            # Look up binary codes
            dest_code = DEST[dest]
            comp_code = COMP[comp]
            jump_code = JUMP[jump]
            
            # Assemble: 111 + comp + dest + jump
            binary = '111' + comp_code + dest_code + jump_code
            output.append(binary)
        
        # Makes it so that Labels don't generate code
    
    return output


def main():
    # Get filename
    if len(sys.argv) != 2:
        print("Usage: python assembler.py file.asm")
        return
    
    input_file = sys.argv[1]
    output_file = input_file.replace('.asm', '.hack')
    
    # Assemble
    binary_code = assemble(input_file)
    
    # Write output
    with open(output_file, 'w') as f:
        for line in binary_code:
            f.write(line + '\n')
    
    print(f"✓ Created {output_file}")


if __name__ == '__main__':
    main()