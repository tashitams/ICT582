print("""
+-------------------------------------------+
|    Program Name: Count words in Sentence  |      
|    Coded by: Tashi Dorji Tamang           |
|    Language used: Python (3.11.3)         |
|    Remark: Lab05 (Exercise 4)             |
+-------------------------------------------+
""")

def count_word_in_sentence():

    word_in_sentence = input("Write a English sentence: ")

    word_list = word_in_sentence.split(" ")

    print(f"The word list is: {word_list}")

    print(f"There are {len(word_list)} words inside the sentence.")


count_word_in_sentence()




