"""
Select an arbitrary string method and write a little script that demonstrates it.

Some important points:

- The script should do something useful. Be able to describe the script in a sentence. Put a comment to the beginning of the script and explain what it does.
put the main part of the script in a main() function
- The main() function should be executed only if the script is called directly. If the script is called as a module, then the main() function shouldn't be executed automatically.
"""


def isValidOption (optionNumber):
    validOptions = ['1', '2', '3', '4']
    return (optionNumber in validOptions)


def main ():
    print('Howdy there cowboy! PLease select what functionality you want to use from bellow')
    userInput = input("enter 1 for capitalizing a string\nenter 2 to check if the string is in the title format\nenter 3 to check if the string is written in all uppercase letters\nenter 4 to remove all whitespaces from a string\n your input: ")
    
    if (not isValidOption(userInput)):
        print('Invalid input! Please try again')
        return
        
    print('ok body. u picked:' + userInput)
    stringInput = input('\nAwesome, now please enter the string to pefrom this on?\n')
    print('\nGiven string is: ' + stringInput)
    print('Return is: ')
    if userInput == '1':
        print(stringInput.capitalize())
    elif userInput == '2':
        print(stringInput.istitle())
    elif userInput == '3':
        print(stringInput.isupper())
    elif userInput == '4':
        print(stringInput.replace(' ',''))
        
    

if __name__ == "__main__":
    main()