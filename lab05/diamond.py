
height = int(input('Enter the height of the diamond: '))
while(height%2 == 0):
    print('Height cannot be even. Please enter an odd number')
    height = int(input('Enter the height of the diamond: '))
    if height%2 != 0:
        break

print('\nok, heres a diamond for you!')
print(height)
mid = (height//2) + 1 
for i in range(height):
    if (i+1) == mid:
        print('*'*height)
    else:
        print('*'.center(height - mid - i))