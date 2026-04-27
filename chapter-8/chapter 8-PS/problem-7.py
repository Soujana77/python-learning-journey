# Q7. Write a python function to remove a given word from a list and strip it.

def remove_word(lst, word):
    result = []
    for item in lst:
        if item.strip() != word:
            result.append(item.strip())
    return result

words = ["apple", " banana ", "mango", " banana"]
print(remove_word(words, "banana"))