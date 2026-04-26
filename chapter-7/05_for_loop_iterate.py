for item in sequence:
    print(item)

    #Example 1: Iterating over a list
    numbers = [10, 20, 30, 40]

for num in numbers:
    print(num)

#Example 2: Iterating over a string
name = "Python"

for ch in name:
    print(ch)

    #Example 3: Iterating using range()
    for i in range(1, 6):
     print(i)

    # Example 4: Iterating with index (important)
    fruits = ["apple", "banana", "mango"]

for i in range(len(fruits)):
    print(i, fruits[i])

   # Example 5: Iterating and checking condition
nums = [1, 2, 3, 4, 5]

for n in nums:
    if n % 2 == 0:
        print(n)