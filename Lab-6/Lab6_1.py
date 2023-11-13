import time
morse_dict = {
    "A":"*-", "B":"-***", "C":"--","D":"-**","E":"*","F":"*-","G":"--*","H":"****",
    "I":"**","J":"*---","K":"-*-","L":"-*","M":"--","N":"-*","O":"---","P":"--",
    "Q":"--*-","R":"-","S":"***","T":"-","U":"**-","V":"***-","W":"*--","X":"-**-",
    "Y":"-*--","Z":"--**",'1': '*----', '2': '**---', '3': '***--', '4': '****-', '5': '*****',
    '6': '-****-', '7': '--***', '8': '---**', '9': '----*', '0': '-----',
    '.': '--*-', ',': '--**--', ':': '---***', '?': '----**'
}

def sanitizeText(input_string,morse_dict):
    sanitized_Text = ''

    for char in input_string:
        if char.upper() in morse_dict:
            sanitized_Text +=char.upper()

    return sanitized_Text


def textToMorseCode(input_string,morse_dict):
    code_list = []

    for char in input_string:
        if char.upper() in morse_dict:
            code_list.append(morse_dict[char.upper()])

    return code_list

def printMorseCode(code_list, dot = 0.2, dash = 0.5, space=1):
    for code in code_list:
        for symbol in code:
            if symbol =='*':
                print("Ti", end=' ')
                time.sleep(dot)

            elif symbol =='-':
                print("Ta",end=' ')
                time.sleep(dash)

        print(" ",end=" ")
        time.sleep(space)

    print()






input_string =input("enter a text to sanitize: ")
sanitized_text = sanitizeText(input_string,morse_dict)
morsed_text = textToMorseCode(input_string,morse_dict)


print(sanitized_text,morsed_text)
printMorseCode(morsed_text)


