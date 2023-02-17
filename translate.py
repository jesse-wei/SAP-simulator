instr_to_num = {'NOP': 0, 'LDA': 1, 'ADD': 2, 'SUB': 3, 'STA': 4, 'LDI': 5, 'JMP': 6, 'JC': 7, 'JZ': 8, 'OUT': 14, 'HLT': 15}

def main():
    prog = input("Enter a list of instructions and args separated by spaces:\n")
    prog_list = prog.split(' ')
    for token in prog_list:
        if token.upper() in instr_to_num:       # If token is an instruction, append the hex code
            print(hex(instr_to_num[token.upper()]).upper()[2:], end='') # Remove the first 2 chars '0x'
            if token.upper() == 'HLT':
                print('F\n')
        else:
            print(hex(int(token)).upper()[2:], end='\n')        # Remove the first 2 chars '0x', and print a newline

if __name__ == "__main__":
    main()
