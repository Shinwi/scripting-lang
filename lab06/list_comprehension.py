# Solve the following exercises with list comprehensions.

# Exercise 1
# ['car', 'tram', 'metro'] → ['CAR!', 'TRAM!', 'METRO!']
inputList1 = ['car', 'tram', 'metro']
result1 = [ word.upper() for word in inputList1]
print(result1)

# Exercise 2
# ['mario', 'luigi', 'peach'] → ['Mario', 'Luigi', 'Peach']
inputList2 = ['mario', 'luigi', 'peach']
result2 = [ word.capitalize() for word in inputList2]
print(result2)

# Exercise 3
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], that is initialize a list with ten 0s
result3 = [0 for i in range(10)]
print(result3)

# Exercise 4
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] → [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
inputList4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result4 = [i*2 for i in inputList4]
print(result4)

# Exercise 5
# ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'] → [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] (notice that there are strings in the first list)
inputList5 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
result5 = [ int(s) for s in inputList4]
print(result5)

# Exercise 6
# "1234567" → [1, 2, 3, 4, 5, 6, 7], that is we have a number as a string and we want to put its digits to a list (as numbers)
input6 = "1234567"
result6 = [ int(s) for s in list(input6) ]
print(result6)

# Exercise 7
# 'The quick brown fox jumps over the lazy dog' → [3, 5, 5, 3, 5, 4, 3, 4, 3], that is store the length of each word
input7 = 'The quick brown fox jumps over the lazy dog'
result7 = [ len(word) for word in input7.split()]
print(result7)

# Exercise 8
# "python is an awesome language" → ['p', 'i', 'a', 'a', 'l'], that is collect the first character of every word in a list
input8 = 'The quick brown fox jumps over the lazy dog'
result8 = [ word[0] for word in input8.split()]
print(result8)

# Exercise 9
# 'The quick brown fox jumps over the lazy dog' → [('The', 3), ('quick', 5), ('brown', 5), ('fox', 3), ('jumps', 5), ('over', 4), ('the', 3), ('lazy', 4), ('dog', 3)], that is create a list of tuples, where a tuple consists of two parts: (word, length_of_word).
input9 = 'The quick brown fox jumps over the lazy dog'
result9 = [ (word, len(word)) for word in input7.split()]
print(result9)

# Exercise 10
# [0, 2, 4, 6, 8], that is store even numbers less than 10 in a list (including 0 too)
result10 = [i for i in range(10) if i%2==0] 
print(result10)

# Exercise 11
# Take the whole numbers less than 20 and calculate their squares. Keep only the even square numbers ([0, 4, 16, 36, 64, 100, 144, 196, 256, 324]).
result11 = sum([i*i for i in range(20) if i%2==0])
print(result11)

# Exercise 12
# Take the whole numbers less than 20 and calculate their squares. Keep only those square numbers whose last digit is "4" ([4, 64, 144, 324]).
result12 = sum([i*i for i in range(20) if str(i*i)[-1] == '4'])
print(result12)

# Exercise 13
# Collect the upper case letters of the English alphabet in a list (use the chr function), and then concatenate the elements to form one string: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.
uppercase_string = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
uppercase_list = list(uppercase_string)
# turn it to a string again
new_uppercase_string = ''.join(uppercase_list)

# Exercise 14
# [' apple ', ' banana ', ' kiwi'] → ['apple', 'banana', 'kiwi'], that is remove whitespaces from both sides of each word
inputList14 = [' apple ', ' banana ', ' kiwi']
result14 = [ word.replace(' ', '') for word in inputList14]
print(result14)

# Exercise 15
# [1, 0, 1, 1, 0, 1, 0, 0] → "10110100", that is concatenate the digits in the list to form a string
inputList15 = [1, 0, 1, 1, 0, 1, 0, 0]
result15 = ''.join([str(i) for i in inputList15])
print(result15)