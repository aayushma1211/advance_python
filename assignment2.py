#QUESTION
#Variables and Input:
# 1. Create a variable my_age and assign your age to it. print a message using this variable.
my_age = 21 
print("My age is", my_age) 
# Output: My age is 21

# 2. Ask the user to enter their favorite food and print a message incorporating this input.
favorite_food = input("Enter your favorite food: ")
print("Your favorite food is", favorite_food)
# output: Your favorite food is <user_input>

# Type Conversion:
#1. Convert the string "42" to an integer and print the result.
string = "42"
print("The integer value is", int(string)) 
# Output: the integer value is 42

#2. Convert the floating-oitn number 3.14159 to a string and print the result.
float_number = 3.14159
print("The string value is", str(float_number))
 # Output: The string value is 3.14159, it only change the type not the value

 #String:
 #1. Concatenate the strings "Hello" and "World!" and print the result.
string1 = "Hello"
string2 ="World!"
print("The concatenated string is", string1 +" "+ string2) 
# Output: The concatenated string is Hello World!

#2. Use string indexing to extract the third character from the string "python".
string = "python"
print("The third character is", string[2])
# Output: The third character is t

#3. Take a sentence as input and print only the first five words.
sentence = input("Enter a sentence: ")
print("The first five words are:",(sentence.split()[:5]))
# Output: The first five words are: ['hello', 'it', 'me', 'aayushma', 'ghale.']

sentence = input("Enter a sentence: ")
print("The first five words are:"," ".join(sentence.split()[:5]))
# Output: The first five words are: hello it me aayushma ghale.