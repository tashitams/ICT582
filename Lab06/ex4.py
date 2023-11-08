print("""
+-----------------------------------------------+
|        Program Name: Result System            |      
|        Coded by: Tashi Dorji Tamang           |
|        Language used: Python (3.11.3)         |
|        Remark: Lab06 (Exercise 4)             |
+-----------------------------------------------+
""")


def main():
    song_lyric = get_song_lyric_from_user()
    word_count = count_word(song_lyric)
    count_highest_frequency_word(word_count)
    count_lowest_frequency_word(word_count)


"""
This function is responsible for
getting the multiple line
song lyric from the user
"""


def get_song_lyric_from_user():
    song_lyric = ""

    while True:
        lyric = input("Type the lyric of a song (or 'done' to exit): ")

        if lyric == 'done':
            break

        song_lyric += lyric + '\n'

    return song_lyric


"""
This function accepts lyric
from the get_song_lyric_from_user()
and count the frequency of each word
"""


def count_word(lyrics):
    word_count = {}
    words = lyrics.split()

    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    return word_count


"""
This function accepts count of each
word from count_word() and find the 
word with highest occurrence
in the lyric
"""


def count_highest_frequency_word(words):
    highest_word_frequency = {}

    # Get the maximum value inside word_count dictionary
    max_value = max(words.values())

    for key, value in words.items():
        if value == max_value:
            highest_word_frequency[key] = value

    print("+-----------------------------------------------+")
    print("|             Highest Frequency Words           |")
    print("+-----------------------------------------------+")
    for word, value in highest_word_frequency.items():
        print(f"Word: {word}, Frequency: {value}")
    print()


"""
This function accepts count of each
word from count_word() and find the 
word with lowest occurrence
in the lyric
"""


def count_lowest_frequency_word(words):
    lowest_word_frequency = {}

    # Get the minimum value inside word_count dictionary
    min_value = min(words.values())

    for key, value in words.items():
        if value == min_value:
            lowest_word_frequency[key] = value

    print("+-----------------------------------------------+")
    print("|             Lowest Frequency Words            |")
    print("+-----------------------------------------------+")
    for word, value in lowest_word_frequency.items():
        print(f"Word: {word}, Frequency: {value}")


main()
