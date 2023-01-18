


#create a function
#class str(object)

def is_palindrome(string):
 string=input("Введіть слово :")
 # enter the string you want to check
 reversed_string = ""

 # cut the string
 reversed = string[::-1]

 #check if the string is equal to its reverse
 if string==reversed:
    return (True)
            
 else:

   return (False)
            
if __name__ == "__main__":
   
 print (is_palindrome(""))
   


    
