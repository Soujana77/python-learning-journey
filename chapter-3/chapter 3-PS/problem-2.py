#Write a program to fill in a letter template which looks like below:
letter = '''Dear <|Name|>,
You are selected!
Date: <|Date|>'''

print(letter.replace("<|Name|>", "Sanvi").replace("<|Date|>", "9th August 2024")) #replace() is a string method that replaces a specified value with another value in a string.