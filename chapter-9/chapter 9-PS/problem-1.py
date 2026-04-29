# Write a program to read the text from a given file poems.Txt and find out whether it contains the word 'twinkle'
with open("chapter-9/chapter 9-PS/poem.txt", "r") as f:
    content = f.read()
if("twinkle" in content):
    print("The word 'twinkle' is present in the file.")
else:
    print("The word 'twinkle' is not present in the file.")
f.close()
