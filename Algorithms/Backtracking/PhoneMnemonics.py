def phone_mnemonics(phone_number):
    MAP = ('0', '1', 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ')
    output = []
    partial_mnemonic = [0] * len(phone_number)

    def backtrack(digit):
        if digit == len(phone_number):
            output.append(''.join(partial_mnemonic))
        else:
            for char in MAP[int(phone_number[digit])]:
                partial_mnemonic[digit] = char
                backtrack(digit+1)

    backtrack(0)
    return output

if __name__ == '__main__':
    print(phone_mnemonics("234"))