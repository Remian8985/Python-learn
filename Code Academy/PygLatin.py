"""
Break It Down
Now let's take what we've learned so far and write a Pig Latin translator.

Pig Latin is a language game, where you move the first letter of the word 
to the end and add "ay." So "Python" becomes "ythonpay." To write a 
Pig Latin translator in Python, here are the steps we'll need to take:

1) Ask the user to input a word in English.
2) Make sure the user entered a valid word.
3) Convert the word from English to Pig Latin.
4) Display the translation result.
"""
######################################################################################
# Written in Python 2.7.x : 

print 'Welcome to the Pig Latin Translator!' 
pyg = 'ay' 

original = "" 

while True:
    # check if the variable is empty: 
    if len(original) > 0 and original.isalpha(): 
        print original 
        break 

    else: 
        original = raw_input('Enter a word in English.\n') # prompt and get input 
 
word = original.lower()
first = word[0] 
new_word = word + first + pyg 
new_word = new_word[1:len(new_word)]  
print 'Translated to PygLatin: %s' %(new_word) 

