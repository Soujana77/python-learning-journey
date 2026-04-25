# A spam commitment is defined as the text containing following keywords: "make a lot of money", "buy now", "Subscribe this", "Click this". Write a program to detect these spams.
text = input("Enter the text: ")

if "make a lot of money" in text:
    print("This is a spam message.")
elif "buy now" in text:
    print("This is a spam message.")
elif "Subscribe this" in text:
    print("This is a spam message.")
elif "Click this" in text:
    print("This is a spam message.")
else:
    print("This is not a spam message.")