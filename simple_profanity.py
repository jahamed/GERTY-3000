# The following section is meant for authorship
__title__   = 'simple_profanity'
__author__  = 'https://github.com/AlanCPSC'
__version__ = '1.0.0'

# The following section is meant for importing
import re
import os
import json
import random

# here we are preparing relative asset loading
CURRENT = os.path.dirname(os.path.abspath(__file__))
DESIRED = os.path.join(CURRENT, 'dictionary.json')

# here we are performing relative asset loading
with open(DESIRED, 'r') as file_handle:
    WORDLIST = json.load(file_handle)

ILLEGAL_WORDS = sorted(WORDLIST, key=len, reverse=True)
ILLEGAL_WORDS = '|'.join(re.escape(x) for x in ILLEGAL_WORDS)
ILLEGAL_WORDS = re.compile(ILLEGAL_WORDS, re.IGNORECASE)
REPLACE_WORDS = '!@#$%'

def censor(text, callback=None):
    """
    given some input text, censor all found profanity

    text     [string]   - target text message
    callback [callable] - replacement callback

    return: string
    """
    if callback is None:
        return ILLEGAL_WORDS.sub(__replace, text)

    else:
        return ILLEGAL_WORDS.sub(callback, text)

def extract(text):
    """
    given some input text, extract all found profanity

    text [string] - target text message

    return: list
    """
    return ILLEGAL_WORDS.findall(text)

def check(text):
    """
    given some input text, check if there is profanity

    text [string] - target text message

    return: boolean
    """
    return bool(ILLEGAL_WORDS.search(text))

def __replace(match):
    """
    helper function as a default replacement callback
    """
    return ''.join(random.choice(REPLACE_WORDS) for _ in range(len(match.group(0))))