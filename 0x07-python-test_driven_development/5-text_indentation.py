#!/usr/bin/python3
"""
New lines after dots, question marks, and colons.
"""

def text_indentation(text):
    """
    I'll pretty it up with new lines after '.', '?', and ':'.
    Args:
        text (str): A string of words.
    Returns:
        Nada. Just prints the fancy text.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for char in '.?:':
        text = text.replace(char, char + "\n\n")
    print("\n".join([line.strip() for line in text.split("\n")]))
