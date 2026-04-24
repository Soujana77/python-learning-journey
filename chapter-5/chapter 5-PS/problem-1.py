#Write aprogram to create a dictonary of hindi works with values as their English translation. Provide user an option to lokk it up!.
words = {
    "namaste": "hello",
    "shukriya": "thank you",    
    "pyaar": "love",
    "dost": "friend",
}

word = input("Enter a hindi word to look up its english translation: ")
print(words[word])