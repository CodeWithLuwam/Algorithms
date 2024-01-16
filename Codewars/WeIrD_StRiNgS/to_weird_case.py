def to_weird_case(words):
    index = 0
    result = ""
    for letter in words:
        if letter == ' ':
            index = 0
            result += ' '
            continue
        if index % 2 == 0:
            result += letter.upper()
        else:
            result += letter.lower()
        index +=1
    return result

# ************************************************************

# Write a function that accepts a string, and returns the same string with all even indexed characters in each word upper cased, and all odd indexed characters in each word lower cased. 
#The indexing just explained is zero based, so the zero-ith index is even, therefore that character should be upper cased and you need to start over for each word.

# The passed in string will only consist of alphabetical characters and spaces(' '). Spaces will only be present if there are multiple words. Words will be separated by a single space(' ').
# Examples:

# "String" => "StRiNg"
# "Weird string case" => "WeIrD StRiNg CaSe"

def to_weird_case1(words):
    
    results= ""
    for i in range (len(words)):
        if i % 2 ==0:
            results += words[i].upper()
        else:
            results += words[i].lower()
    return results

print(to_weird_case1("test"))

# ************************************************************

def convert_string1(input_string):
    words = input_string.split()  # Split the input string into words
  # .split spits into a list of words [Weird, string, case]
    result_words = []

    for word in words:
        modified_word = ""
        for i in range(len(word)):
            if i % 2 == 0:
                modified_word += word[i].upper()
            else:
                modified_word += word[i].lower()
        result_words.append(modified_word)

    result_string = " ".join(result_words)  # Join the modified words back into a string
    return result_string

# Test cases
print(convert_string1("String"))  # Output: "StRiNg"
print(convert_string1("Weird string case"))  # Output: "WeIrD StRiNg CaSe"

# ************************************************************
def convert_string(input_string):
    modified_word = ""
    for i in range(len(input_string)):
        if i % 2 == 0:
            modified_word += input_string[i].upper()
        else:
            modified_word += input_string[i].lower()
    return modified_word

# Test case
print(convert_string("String"))  # Output: "StRiNg"

# ************************************************************

my_tuple = ("red", "green", "blue")
result = " | ".join(my_tuple)
print(result)

#output
# red | green | blue

# ************************************************************

input_string = "This is an example"
words = input_string.split()
print(words)

#output
#['This', 'is', 'an', 'example']

