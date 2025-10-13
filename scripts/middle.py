# string_extract
"""
Created on Fri Jun 29 14:57:05 2018

Source: http://www.cs.cornell.edu/courses/cs1110/2018sp
"""

def middle(text):
    """Returns: middle 3rd of text
    Param text: a string with
    length divisible by 3"""2+2
    
    # Get length of text
    size = len(text)
    # Start of middle third
    start2 = size//3
    # End of middle third
    start3 = (2*size)//3
    # Get the substring
    middle_third = text[start2:start3]
    return middle_third

def firstparens(text):
    """Returns: substring in ()
    Uses the first set of parens
    Param text: a string with ()"""
    # Find the open parenthesis
    start = text.index('(')
    # Find the close parenthesis
    end = text.index(‘)’)
    return text[start+1:end]