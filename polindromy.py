#Варіант 1 
#enter the word you want to check
#class str(object)
my_str = 'oko'


# reverse the string
rev_str = reversed(my_str)

# check if the string is equal to its reverse
if list(my_str) == list(rev_str):
 # if the word is equal to the inverted word, then it is true
   print(True)
else:
   print(False)
 # if the word is not equal to the inverted word, then it is a False


#Варіант 2
#create a function
#class str(object)
def is_palindrome(string):

    reversed_string = ""
    # transversing through string from last
    for i in range(len(string), 0, -1):
        # Addind last characters of string into a new string
        reversed_string += string [i-1]
        # check if the string is equal to its reverse
        if string == reversed_string:
            print(True)
            
            
        else:
           print(False)
            
if __name__ == "__main__":
    #enter the correct word to check
    is_palindrome("pop")
 #не можу зрозуміти  як зробити щоб показувало тільки потрібний результат


    
