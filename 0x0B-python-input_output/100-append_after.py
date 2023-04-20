#!/usr/bin/python3
""" Module contains a function that insert a line of text
    to a file, after each line containing a specific string
"""


def append_after(filename="", search_string="", new_string=""):
    """ Inserts a line of text to a file after each line containing
        a specific string. It accept three arguments:
        filename-> represents the file to write to
        search_string-> specific string thats looked for before adding
        the new string
        new_string-> is added below the searched string
    """
    with open(filename, mode="r+", encoding="utf-8") as MyFile:
        new_text = ""
        for line in MyFile:
            new_text += line
            if search_string in line:
                new_text += new_string
        MyFile.seek(0)
        MyFile.write(new_text)
