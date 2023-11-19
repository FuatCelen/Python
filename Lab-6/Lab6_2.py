import time

from adafruit_circuitplayground import cp




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



def CPMorseCode(code_list, dot_duration=0.2, dash_duration=0.6, space_duration=0.2, word_space_duration=1.4):
    for code in code_list:
        for symbol in code:
            if symbol == '*':
                for i in range(10):
                    cp.pixels[i] = (255, 0, 0)  # Red LED
                    time.sleep(dot_duration)
                    cp.pixels.fill((0, 0, 0))  # Turn off LED
                    time.sleep(space_duration)
            elif symbol == '-':
                for i in range(10):
                    cp.pixels[i] = (0, 0, 255)  # Blue LED
                    time.sleep(dash_duration)
                    cp.pixels.fill((0, 0, 0))  # Turn off LED
                    time.sleep(space_duration)
        time.sleep(word_space_duration)
        cp.pixels.fill((0, 0, 0))  # Turn off all LEDs





input_string =input("enter a text to sanitize: ")
sanitized_text = sanitizeText(input_string,morse_dict)
morsed_text = textToMorseCode(input_string,morse_dict)


print(sanitized_text,morsed_text)
printMorseCode(morsed_text)
CPMorseCode(morsed_text)



            
            


