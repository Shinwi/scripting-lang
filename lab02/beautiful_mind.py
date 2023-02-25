TEXT = """
PY7H0N 15 4 W1D3LY U53D G3N3R4L-PURP053, H1GH-L3V3L PR0GR4MM1NG
L4NGU4G3. 175 D351GN PH1L050PHY 3MPH451Z35 C0D3 R34D4B1L17Y,
4ND 175 5YN74X 4LL0W5 PR0GR4MM3R5 70 3XPR355 C0NC3P75 1N F3W3R L1N35 0F
C0D3 7H4N W0ULD B3 P0551BL3 1N L4NGU4G35 5UCH 45 C++ 0R J4V4.
7H3 L4NGU4G3 PR0V1D35 C0N57RUC75 1N73ND3D 70 3N4BL3 CL34R PR0GR4M5 0N
B07H 4 5M4LL 4ND L4RG3 5C4L3
"""

# translates the TEXT variable using a dictionary where we store the key value pairs needed to do the translations
def translateText():
    translationDictionary = {
        '0': 'O',
        '1': 'I',
        '3': 'E',
        '4': 'A',
        '5': 'S',
        '7': 'T'
    }

    ans = ''
    for i in TEXT:
        if i in translationDictionary.keys():
            ans += translationDictionary[i]
        else:
            ans += i
    
    return ans


# uses the string method ".replace()" to translate the text
def translateTextWithReplace():
    translatedText = TEXT.replace('0', 'O').replace('1','I').replace('3','E').replace('4', 'A').replace('5','S').replace('7','T')
    return translatedText

def main():
    print('Translating the text with string method replace:')
    readableText = translateTextWithReplace()
    print(readableText)
    print('\nNow the translation with the help of a dictionary:')
    readableText2 = translateText()
    print(readableText2)

##############################################################################

if __name__ == "__main__":
    main()