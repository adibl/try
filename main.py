# -*- coding: utf-8 -*-
import sys

NO_WORD = [",", ".", "\n", " ", "-", "_", ")", "(", "!", "?", ":", ";", ""]


def read_from_file(path):
    """
    read all thee file to string
    :path:the file place+name.
    :return: string of the file
    """
    with open(path, 'r') as file_index:
        text = file_index.read()
    return text


def printer(words_frequency):
    """
    chose the printing method
    :words_frequency: the dictionary of the letters frequency
    :return:printing method

    """
    string = ""
    if sys.argv[1] == "--topcount":
        words = sorted(words_frequency.items(), reverse=True, key=lambda x: x[1])
        for word in words[:20]:
            string += word[0]+": "+str(word[1])+"\n"
    else:
        for word in words_frequency.items():
            string += word[0]+": "+str(word[1])+"\n"
    return string


def is_valid():
    """
    check if the parameters are valid
    :return: True if it si and false if not
    """
    return '--count' == sys.argv[1] or '--topcount' == sys.argv[1]


def main():
    """
    get file name and print method and print methode.
    print methods:
    --count:print the count of all the words in the text
    --topcount:print the count of the 20 words that showed the most on the file
    """
    if not is_valid():
        return
    text = read_from_file(sys.argv[2])
    text = text.lower()
    words_frequency = {}
    word = ""
    for char in text:
        if char in NO_WORD:
            if word in NO_WORD or word in ("'", '"', ""):
                pass
            else:
                if word[0] in ("'", '"'):
                    word = word[1:]
                if word[-1] in ("'", '"'):
                    word = word[:-1]
                if word in words_frequency:
                    words_frequency[word] += 1
                else:
                    words_frequency[word] = 1
            word = ""
        else:
            word += char
    print printer(words_frequency)


if __name__ == '__main__':
    main()