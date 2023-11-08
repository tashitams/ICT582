print("""
+-------------------------------------------+
|      Program Name: Word Finder            |      
|      Coded by: Tashi Dorji Tamang         |
|      Language used: Python (3.11.3)       |
+-------------------------------------------+
""")

quit_message = """
+-------------------------------------------+
|            Program terminated             |
+-------------------------------------------+
- You entered quit.
- Exiting the program..."""

while True:
    sentence = input("Write a sentence: ")

    if sentence == "quit":
        print(quit_message)
        break

    word = input("Write a word: ")

    result = sentence.find(word)

    if result == -1:
        print(f"Sorry {word} in not present in the sentence. \n")

    else:
        print(f"{word} is present at index {result}. \n")



    
