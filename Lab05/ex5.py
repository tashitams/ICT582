print("""
+-------------------------------------------------------------+
|             Program Name: Capitalise word                   |      
|             Coded by: Tashi Dorji Tamang                    |
|             Language used: Python (3.11.3)                  |
|             Remark: Lab05 (Exercise 5)                      |
+-------------------------------------------------------------+
""")

without_side_effect_code_explanation = """
+-------------------------------------------------------------+
|          Code explanation for without side effect           |
+-------------------------------------------------------------+
As you can see the function does not have side effects because 
it doesn't modify the original list L. Instead, it creates a 
new list capitalized_word_list  with the capitalized versions
of the words, leaving the original list L unchanged.
"""

with_side_effect_code_explanation = """
+-------------------------------------------------------------+
|              Code explanation for side effect               |
+-------------------------------------------------------------+
As you can see the function does have side effects because the 
original list L is modified directly by the function. 
"""
def main():
    count = 0
    L = []

    while True:
        try:
            number_of_word_in_list = int(input("How many words do you want in the list? "))

        except ValueError:
            print("Invalid input, please enter number. \n")

        else:
            while count < number_of_word_in_list:
                word = input("Enter the word: ")

                if len(word.split()) > 1:
                    print("Sorry enter only ONE WORD at a time.")
                else:
                    L.append(word)
                    count += 1
            break

    print(f"\nOriginal word list: {L} \n")

    print(f"Capitalized words without side effect:\n{L, capitalize_words_in_list_without_side_effect(L)}", end="")

    print(without_side_effect_code_explanation)

    print(f"Capitalized words with side effect:\n{L, capitalize_words_in_list_with_side_effect(L)}", end="")

    print(with_side_effect_code_explanation)


# Without side effect
# The original list L remains unchanged.
def capitalize_words_in_list_without_side_effect(word_list):
    capitalized_word_list = []

    for word in word_list:
        capitalized_word_list.append(word.capitalize())

    """
        +-----------------------------------------+
        |  Using python list comprehension        |
        |  above for loop can also be written as  |
        +-----------------------------------------+

        capitalized_word_list = [word.capitalize() for word in words]
    """

    return capitalized_word_list


# With side effect
# The original list L is modified directly by the function.
def capitalize_words_in_list_with_side_effect(word_list):
    for i in range(len(word_list)):
        word_list[i] = word_list[i].capitalize()

    return word_list


main()
