#!/usr/bin/python3
def text_indentation(text):
    """
    A function that prints a text with 2 new lines after each
    of these characters: '.', '?', ':'

    Args:
        text: string

    Returns: None

    Raises:
        TypeError: if text is not a string

    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    words = text[:]

    for i in ".?:":
        list_text = words.split(i)
        words = ""
        for j in list_text:
            j = j.strip(" ")
            words = j + i if words is "" else words + "\n\n" + j + i

    print(words[:-3], end="")
