def count_word_occurrences(text, word):
    text = text.lower()  # Convert the text to lowercase for case-insensitive matching
    word = word.lower()  # Convert the target word to lowercase
    return text.count(word) if text else 0

    """
def count_word_occurrences(text, word): This line defines a function named count_word_occurrences with two parameters: text (the text to search within) and word (the word to search for).

text = text.lower(): This converts the entire text to lowercase. It ensures that the search is case-insensitive, meaning it doesn’t differentiate between uppercase and lowercase letters.

word = word.lower(): Similarly, this converts the word to lowercase for the same reason.

return text.count(word) if text else 0: This line uses the count method to find the number of occurrences of word in text. If text is not empty, it returns the count. If text is empty, it returns 0.

The function is useful for text analysis, such as finding the frequency of a word in a document or a string. It’s important to note that the count method matches exact words, so partial matches are not counted. For example, if the word is “cat” and the text contains “concatenate”, it will not be counted. The function also does not account for word boundaries, so “cat” will be counted in both “the cat” and “the caterpillar”.
    """
