#!/usr/bin/python3
# 5-text_indentation.py
"""This difines a function that prints indented text"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each occurrence of '.', '?', and ':' characters.

    Args:
        text (str): The input text.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    sentences = []
    current_sentence = ""
    for char in text:
        current_sentence += char
        if char in [".", "?", ":"]:
            sentences.append(current_sentence.strip())
            current_sentence = ""
    for sentence in sentences:
        print(sentence)
        print()
