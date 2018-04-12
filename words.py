'''Retrive and Print words form URL

Usage:
    python3 words.py 'url'
'''

import sys
from urllib.request import urlopen


def fetch_words(url):
    '''Grabbing a list of words from a URL..
    Args:
        url: URL of a UTF-8 doc
    Returns:
        A list of strings containg the words from a doc

    '''
    with urlopen(url) as story:
        story_words = []
        for line in story:
            line_words = line.decode('utf-8').split()
            for word in line_words:
                story_words.append(word)
    return story_words


def print_items(items):
    '''Prints the objects out to screen
    Args:
        an iterable series of printable stuff
    '''
    for item in items:
        print(item)


def main(url):
    '''Print each word from a text document form a URL
    Args:
        url: where the text be at yo!
    '''
    words = fetch_words(url)
    print_items(words)


if __name__ == '__main__':
    main(sys.argv[1])
