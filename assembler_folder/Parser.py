"""Cleans and parses assembly lines"""

def clean_line(line):
    """Remove comments and whitespace"""
    # Removes comments
    if '//' in line:
        line = line[:line.index('//')]
    # Removes whitespace
    return line.strip()


def get_command_type(line):
    """Returns 'A', 'C', or 'L' for command type"""
    if line.startswith('@'):
        return 'A'
    elif line.startswith('('):
        return 'L'
    else:
        return 'C'


def parse_a_command(line):
    """Returns symbol/number from @xxx"""
    return line[1:]  # Removes @


def parse_l_command(line):
    """Returns label from (LABEL)"""
    return line[1:-1]  # Removes ( and )


def parse_c_command(line):
    """Returns (dest, comp, jump) from C-command"""
    dest = ''
    jump = ''
    
    # Split by = to get dest
    if '=' in line:
        dest, line = line.split('=')
    
    # Split by ; to get jump
    if ';' in line:
        line, jump = line.split(';')
    
    comp = line
    
    return dest, comp, jump