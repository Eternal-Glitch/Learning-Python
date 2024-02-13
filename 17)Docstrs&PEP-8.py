#Doc-strings are literals which come after definitions of functions, method, class or module

def square(n):
    #A doc-string is written in the top of the body in a function, it's a special type of string, NOT A COMMENT! 
    '''This is a funtion which takes n, and returns it's square'''  #This is a Doc-string
    print(n**2)
square(5)
print(square.__doc__)   #This is how to see a Doc-string


#PEP 8 (Python enchancement Proposal)
""""It was made to make the python code more readable, maintainable etc.
It's a type of document"""