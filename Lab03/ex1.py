print("""
+-------------------------------------------+
|      Program Name: Reverse a string       |      
|      Coded by: Tashi Dorji Tamang         |
|      Language used: Python (3.11.3)       |
+-------------------------------------------+
""")

word = input("Enter a word to revese: ")

reversed_word = ''  # initialize to empty string

for i in range(len(word)):
    # print(i) 01234
    reversed_word = word[i] + reversed_word

sliced_reversed_word = word[::-1]

if reversed_word == sliced_reversed_word:
    print(f"""
+-------------------------------------------------------------+
|                     Program Output                          |
+-------------------------------------------------------------+
- The reversed word using FOR LOOP of "{word}" is "{reversed_word}"
- The reversed word produced using "{word}[::-1]" is "{sliced_reversed_word}"
- Therefore "{word}" looks SAME using For Loop and Negative Indexing
""")

else:
    print("Sorry the word doesn't match")
