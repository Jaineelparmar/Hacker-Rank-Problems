#The textwrap module can be used for wrapping and formatting of plain text. This module provides formatting of text by adjusting the line breaks in the input paragraph.
#You are given a string  and width .Your task is to wrap the string into a paragraph of width .


import textwrap 
  
value = """This function wraps the input paragraph such that each line in the paragraph is at most width characters long.
The wrap method returns a list of output lines. The returned list is empty if the wrapped output has no content."""
  
# TextWrapper() = Object for wrapping/filling text
# Wrap this text. 
wrapper = textwrap.TextWrapper(width = 100) 
  
# fill() = Reformat the single paragraph in 'text' to fit in lines of no more than 'self.width' columns, and return a new string containing the entire wrapped paragraph
word_list = wrapper.fill(text = value) 
print(word_list)


#OR  


import textwrap 
  
value = """This function wraps the input paragraph such that each line in the paragraph is at most width characters long.
The wrap method returns a list of output lines. The returned list is empty if the wrapped output has no content."""
  
# TextWrapper() = Object for wrapping/filling text
# Wrap this text. 
wrapper = textwrap.TextWrapper(width = 100) 

# wrap() = Reformat the single paragraph in 'text' so it fits in lines of no more than 'self.width' columns, and return a list of wrapped lines.
# Tabs in 'text' are expanded with string.expandtabs(), and all other whitespace characters (including newline) are converted to space.
word_list = wrapper.wrap(text = value) 

#Print each line. 
for element in word_list: 
    print(element) 
    


#OR

import textwrap

def wrap(string, max_width):
    return textwrap.fill(string, max_width)


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)